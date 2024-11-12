import os
from astropy.io import fits
import geopandas as gpd
from shapely.geometry import Polygon

# Function to load data and generate polygons for each FITS file
def load_data_and_generate_polygons(directory):
    polygons = []
    ids = []
    metadata = {
        'EXPOSURE': [],
        'FILTER': [],
        'GAIN': []
        # Add more metadata fields as needed
    }

    for filename in os.listdir(directory):
        if filename.endswith(".fits"):
            file_path = os.path.join(directory, filename)
            with fits.open(file_path) as hdul:
                # Extract latitude and longitude corner data
                latitudes = [
                    hdul[1].header['V0_LAT'],
                    hdul[1].header['V1_LAT'],
                    hdul[1].header['V2_LAT'],
                    hdul[1].header['V3_LAT']
                ]
                longitudes = [
                    hdul[1].header['V0_LON'],
                    hdul[1].header['V1_LON'],
                    hdul[1].header['V2_LON'],
                    hdul[1].header['V3_LON']
                ]
                
                # Create polygon from corner coordinates
                polygon_coords = [
                    (longitudes[0], latitudes[0]),
                    (longitudes[1], latitudes[1]),
                    (longitudes[2], latitudes[2]),
                    (longitudes[3], latitudes[3]),
                    (longitudes[0], latitudes[0])
                ]
                polygon = Polygon(polygon_coords)
                polygons.append(polygon)
                ids.append(filename)  # Use the filename as an ID

                # Extract additional metadata fields
                metadata['EXPOSURE'].append(hdul[0].header.get('EXPOSURE', None))
                metadata['FILTER'].append(hdul[0].header.get('FILTER', None))
                metadata['GAIN'].append(hdul[0].header.get('GAIN', None))

    return polygons, ids, metadata

# Function to generate shapefile from collected polygons and metadata
def generate_shapefile(polygons, ids, metadata):
    # Create a GeoDataFrame with additional metadata columns
    gdf = gpd.GeoDataFrame({
        "id": ids,
        "EXPOSURE": metadata['EXPOSURE'],
        "FILTER": metadata['FILTER'],
        "GAIN": metadata['GAIN']
    }, geometry=polygons, crs="EPSG:4326")
    
    # Save shapefile
    gdf.to_file("lunar_quads.shp", driver="ESRI Shapefile")
    print("Shapefile saved as lunar_quads.shp")

# Main execution
directory = './input'  # Replace with your actual directory path
polygons, ids, metadata = load_data_and_generate_polygons(directory)
generate_shapefile(polygons, ids, metadata)
