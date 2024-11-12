import os
from astropy.io import fits
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon

# Define the user-specified time range
utc_start_user = '2024-03-01T00:00:00.114'
utc_end_user = '2024-04-01T00:45:12.114'

# Convert start and end times to datetime objects for easy comparison
utc_start = datetime.strptime(utc_start_user, '%Y-%m-%dT%H:%M:%S.%f')
utc_end = datetime.strptime(utc_end_user, '%Y-%m-%dT%H:%M:%S.%f')

# Function to extract start and end times from filenames
def extract_time_from_filename(filename):
    parts = filename.split('_')
    start_time_str = parts[3]  # Example: '20200201T000000114'
    end_time_str = parts[4].replace('.fits', '')  # Example: '20200201T000008114'
    
    # Convert to datetime format
    start_time = datetime.strptime(start_time_str, '%Y%m%dT%H%M%S%f')
    end_time = datetime.strptime(end_time_str, '%Y%m%dT%H%M%S%f')
    
    return start_time, end_time

# Function to create the output filename based on the specified start and end times
def create_output_filename(start_time, end_time):
    start_time_str = start_time.strftime('%Y%m%dT%H%M%S%f')[:-3]
    end_time_str = end_time.strftime('%Y%m%dT%H%M%S%f')[:-3]
    return f'ch2_cla_l1_{start_time_str}_{end_time_str}.fits'

# Function to load and filter the data based on time range
def load_and_filter_data(directory):
    combined_spectra = None  # To hold the sum of spectra
    total_exposure = 0  # To accumulate exposure time
    
    latitudes = []
    longitudes = []

    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".fits"):
            file_path = os.path.join(directory, filename)
            start_time, end_time = extract_time_from_filename(filename)
            
            # Check if the file's time range overlaps with the user-defined time range
            if start_time <= utc_end and end_time >= utc_start:
                with fits.open(file_path) as hdul:
                    # Get the channel and counts data from the binary table
                    channels = hdul[1].data['CHANNEL']
                    counts = hdul[1].data['COUNTS']
                    exposure = hdul[1].header['EXPOSURE']  # Assuming exposure time is in the header
                    
                    # Collect latitude and longitude corner data
                    latitudes.extend([hdul[1].header['V0_LAT'], hdul[1].header['V1_LAT'],
                                      hdul[1].header['V2_LAT'], hdul[1].header['V3_LAT']])
                    longitudes.extend([hdul[1].header['V0_LON'], hdul[1].header['V1_LON'],
                                       hdul[1].header['V2_LON'], hdul[1].header['V3_LON']])
                    
                    # Initialize combined_spectra if it's the first file being added
                    if combined_spectra is None:
                        combined_spectra = np.zeros_like(counts)

                    # Sum up the spectra and exposure times
                    combined_spectra += counts
                    total_exposure += exposure
    
    # Normalize the combined spectrum by total exposure time to get counts per second
    normalized_spectrum = combined_spectra / total_exposure if total_exposure > 0 else combined_spectra

    # Calculate max/min latitude and longitude bounds
    max_latitude = max(latitudes)
    min_latitude = min(latitudes)
    max_longitude = max(longitudes)
    min_longitude = min(longitudes)

    return channels, normalized_spectrum, total_exposure, (min_latitude, max_latitude), (min_longitude, max_longitude)

# Save the resulting normalized spectrum to a new FITS file with all headers included
def save_result_to_fits(channels, normalized_spectrum, total_exposure, start_time, end_time,
                         lat_bounds, lon_bounds, output_directory='./output'):
    
    output_filename = create_output_filename(start_time, end_time)
    output_path = os.path.join(output_directory, output_filename)

    col1 = fits.Column(name='CHANNEL', format='1I', array=channels)
    col2 = fits.Column(name='COUNTS', format='1E', array=normalized_spectrum)
    cols = fits.ColDefs([col1, col2])
    
    hdu = fits.BinTableHDU.from_columns(cols)

    # Add all necessary headers from original FITS file structure
    hdu.header['XTENSION'] = ('BINTABLE', 'Written by IDL:  Sun Oct 27 02:00:25 2024')
    hdu.header['BITPIX'] = 8
    hdu.header['NAXIS'] = 2
    hdu.header['NAXIS1'] = 6
    hdu.header['NAXIS2'] = 2048
    hdu.header['PCOUNT'] = 0
    hdu.header['GCOUNT'] = 1
    hdu.header['TFIELDS'] = 2
    hdu.header['TFORM1'] = '1I'
    hdu.header['TFORM2'] = '1E'
    hdu.header['TTYPE1'] = 'CHANNEL'
    hdu.header['TTYPE2'] = 'COUNTS'
    hdu.header['TUNIT2'] = 'count'
    
    # Other essential headers for scientific accuracy
    hdu.header.update({
        'EXTNAME': 'SPECTRUM',
        'HDUCLASS': 'OGIP',
        'HDUCLAS1': 'SPECTRUM',
        'HDUVERS1': '1.1.0',
        'HDUVERS': '1.1.0',
        'HDUCLAS2': 'TOTAL',
        'HDUCLAS3': 'COUNT',
        'TLMIN1': 0,
        'TLMAX1': len(channels) - 1,
        'TELESCOP': 'CHANDRAYAAN-2',
        'INSTRUME': 'CLASS',
        'FILTER': 'none',
        'AREASCAL': 1.0,
        'BACKFILE': 'NONE',
        'BACKSCAL': 1.0,
        'CORRFILE': 'NONE',
        'CORRSCAL': 1.0,
        'RESPFILE': '',
        'ANCRFILE': '',
        'PHAVERSN': '1992a',
        'DETCHANS': len(channels),
        'CHANTYPE': 'PHA',
        'POISSERR': True,
        'STAT_ERR': 0,
        'SYS_ERR': 0,
        'GROUPING': 0,
        'QUALITY': 0,
        'EQUINOX': 2000.00,
        'DATE': datetime.now().strftime('%a %b %d %H:%M:%S %Y'),
        'PROGRAM': 'CLASS_add_scds.pro',

        'EXPOSURE': total_exposure,

        'SW_VERSN': 2.1,
        'IPFILE': 'CLA01D32CHO2168503016024187051735564_05.pld',
        'DATASET': 553,
        'STARTIME': start_time.strftime('%Y%m%dT%H%M%S%f')[:-3],
        'ENDTIME': end_time.strftime('%Y%m%dT%H%M%S%f')[:-3],
        'TEMP': -33.5,
        'GAIN': 13.5,
        'SCD_FLTR': 0,
        'SCD_USED': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,',
        'MID_UTC': '2024-07-04T23:38:47.796',
        'SAT_ALT': 77.1897,
        'SAT_LAT': -68.1979,
        'SAT_LON': 9.513,
        'LST_HR': 23,
        'LST_MIN': 30,
        'LST_SEC': 38,
        'BORE_LAT': -68.1965,
        'BORE_LON': 9.5143,

        'SOLARANG': 113.147,
        'PHASEANG': 113.147,
        'EMISNANG': 5.1430132e-09,


        
        # Coordinates of corners for shapefile generation:
        "V0_LAT": lat_bounds[0],
        "V0_LON": lon_bounds[0],
        "V1_LAT": lat_bounds[1],
        "V1_LON": lon_bounds[0],
        "V2_LAT": lat_bounds[1],
        "V2_LON": lon_bounds[1],
        "V3_LAT": lat_bounds[0],
        "V3_LON": lon_bounds[1]
        
       

        
        
     })

    os.makedirs(output_directory, exist_ok=True)
    
    # Write to FITS file
    hdu.writeto(output_path, overwrite=True)

    print(f'Result saved to {output_path}')

# Directory containing the FITS files
directory = './input'  # Replace with your actual directory path

# Load and process the data
channels, result_spectrum, total_exposure, lat_bounds, lon_bounds = load_and_filter_data(directory)

# Plotting (optional)
plt.figure(figsize=(10, 6))
plt.plot(channels * 13.5 * 0.001, result_spectrum, color='blue', linestyle='-', linewidth=1.5)
plt.xlabel('Energy (keV)')
plt.ylabel('Counts per Second')
plt.title('Normalized X-ray Spectrum')
plt.grid(True)
plt.show()

# Save result as a FITS file using calculated bounds for naming purposes.
save_result_to_fits(channels, result_spectrum, total_exposure,
                     utc_start, utc_end,
                     lat_bounds,
                     lon_bounds)

# Generate Shapefile from coordinates extracted from FITS header
def generate_shapefile(lat_bounds, lon_bounds):
   polygon_coords = [
       (lon_bounds[0], lat_bounds[0]), 
       (lon_bounds[0], lat_bounds[1]), 
       (lon_bounds[1], lat_bounds[1]), 
       (lon_bounds[1], lat_bounds[0]), 
       (lon_bounds[0], lat_bounds[0])  
   ]
   for i in polygon_coords:
       print(i[0], " ", i[1], "\n")

   polygon = Polygon(polygon_coords)
   gdf = gpd.GeoDataFrame({"id": [1]}, geometry=[polygon], crs="EPSG:4326")
   
   gdf.to_file("lunar_area.shp", driver="ESRI Shapefile")
   print("Shapefile saved as lunar_area.shp")

generate_shapefile(lat_bounds, lon_bounds)