from astropy.io import fits
import csv
import os
from datetime import datetime


def parse_filename_time(file_name):
    print("file_name")
    # Extract start and end time from the filename in the format yyyymmddTHHMMSS_yyyymmddTHHMMSS
    start_time = datetime.strptime(file_name[11:29], "%Y%m%dT%H%M%S%f")
    end_time = datetime.strptime(file_name[30:-5], "%Y%m%dT%H%M%S%f")

    return start_time, end_time
def extract_coordinates(header):
    # Assuming metadata keys are formatted for coordinates, like 'V0_LON', 'V0_LAT' up to 'V3_LON', 'V3_LAT'
    try:
        v0 = (header['V0_LON'], header['V0_LAT'])
        v1 = (header['V1_LON'], header['V1_LAT'])
        v2 = (header['V2_LON'], header['V2_LAT'])
        v3 = (header['V3_LON'], header['V3_LAT'])
        return v0 + v1 + v2 + v3
    except KeyError:
        print("Coordinate metadata is missing in FITS file header.")
        return (None,) * 8


def write_to_csv(file_path, ratio_dict, solar_class, output_csv='output.csv'):
    # Extract file name and times
    file_name = file_path.split('/')[-1]
    print(file_name)
    start_time, end_time = parse_filename_time(file_name)

    # Open the FITS file and extract required data
    with fits.open(file_path) as hdul:
        header = hdul[1].header
        coordinates = extract_coordinates(header)

    # Prepare data for CSV
    row = [file_name, start_time, end_time] + list(coordinates)

    # Append ratios with respect to Silicon
    for element, ratio in ratio_dict.items():
        row.append(ratio)

    # Add solar class
    row.append(solar_class)

    # Write to CSV file
    header_row = ['file_name', 'start_time', 'end_time', 'v0_lon', 'v0_lat', 'v1_lon', 'v1_lat',
                  'v2_lon', 'v2_lat', 'v3_lon', 'v3_lat'] + [f'ratio_{el}' for el in ratio_dict.keys()] + [
                     'solar_class']

    try:
        with open(output_csv, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # If the file is empty, write the header row
            if os.stat(output_csv).st_size == 0:
                writer.writerow(header_row)
            
            # Write the data row
            writer.writerow(row)

    except IOError:
        print("I/O error when writing to CSV file.")

def process_fits_file(file_path):
    # Function to process the FITS file (example: print the header)
    with fits.open(file_path) as hdul:
        # Access the header of the first HDU (Header Data Unit)
        ratios = {"Al": 20, "Ca": 10, "Si": 40, "O": 15, "Fe": 15, "Mg": 30} # function call
        solar_class = file_path[7]
        write_to_csv(file_path, ratios, solar_class)


import os

def process_fits_files_in_directory(directory_path):
    # List all files in the directory
    for solar_class in os.listdir(directory_path):
        class_path = os.path.join(directory_path, solar_class)
        
        # Ensure that the path is a directory before proceeding
        if os.path.isdir(class_path):
            for file_name in os.listdir(class_path):
                file_path = os.path.join(class_path, file_name)
                
                # Process only .fits files (assuming you want to process FITS files specifically)
                if file_path.endswith('.fits'):
                    process_fits_file(file_path)
                else:
                    print(f"Skipping non-FITS file: {file_path}")
        else:
            print(f"Skipping non-directory item: {class_path}")


directory_path = './fits'  # Replace with the actual path

process_fits_files_in_directory(directory_path)