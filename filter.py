import os
from datetime import datetime
from goes import get_goes_data
# Lists to hold files by flare class
A, B, C, X, M, S = [], [], [], [], [], []

def filter_fits_files(fits_files, start_time, end_time, goes_date, flare_class):
    """
    Filter FITS files based on time range, date, and flare class.

    Parameters:
    - fits_files (list): List of FITS file names.
    - start_time (str): Start time in 'HHMM' format.
    - end_time (str): End time in 'HHMM' format.
    - goes_date (str): Date in 'YYYYMMDD' format.
    - flare_class (str): Flare class filter ('a', 'b', 'c', 'x', 'm').
    
    Returns:
    - None (adds files to appropriate lists based on flare class).
    """
    
    # Convert start and end times to datetime.time objects for comparison
    # start_dt = start_time
    # end_dt = end_time
    
    # Convert goes_date to datetime.date
    date = datetime.strptime(goes_date, "%Y%m%d").date()
    
    # Ensure flare_class is uppercase for consistent matching
    # flare_class = flare_class.upper()
    
    for file_name in fits_files:
        date_time_str = file_name.split('_')[3]
        
        # Extract and parse time and date from filename
        file_time = datetime.strptime(date_time_str[9:13], "%H%M").time()
        file_date = datetime.strptime(date_time_str[:8], "%Y%m%d").date()
        print(start_time, end_time, file_time, file_date, date)
        # Check if file time and date fall within the specified range
        if start_time <= file_time and file_time <= end_time and date == file_date:
            # Add file to the list based on flare_class
            print(flare_class)
            if flare_class == 'A':
                A.append(file_name)
            elif flare_class == 'B':
                B.append(file_name)
            elif flare_class == 'C':
                C.append(file_name)
            elif flare_class == 'X':
                X.append(file_name)
            elif flare_class == 'M':
                M.append(file_name)
            elif flare_class == 'S':
                S.append(file_name)


# Function to get all .fits files in the folder
def get_fits_files(folder_path):
    """
    Get all FITS files in the specified folder and add their names to a list.

    Parameters:
    - folder_path (str): Path to the folder containing the FITS files.

    Returns:
    - List of FITS file names in the folder.
    """
    fits_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".fits"):
            fits_files.append(file_name)
    return fits_files

# Example usage
folder_path = "./01"  # Update this with the path to your FITS files
fits_files = get_fits_files(folder_path)
# print("FITS files:", fits_files)
goes_data = get_goes_data()
# start_time = "0000"  # Start time in HHMM
# end_time = "1200"    # End time in HHMM
# goes_date = "20200201"  # Example date in 'YYYYMMDD' format
# flare_class = "C"    # Flare class to filter by

# Filter the FITS files
for date, data in goes_data.items():
    for event in data:
        start_time = event[0]
        end_time = event[1]
        flare_class = event[2]
        # print(event)
        # print(date)
        filter_fits_files(fits_files, start_time, end_time, date, flare_class)

# Print categorized files
print("Files in flare class A:", len(A))
print("Files in flare class B:", len(B))
print("Files in flare class C:", len(C))
print("Files in flare class X:", len(X))
print("Files in flare class M:", len(M))