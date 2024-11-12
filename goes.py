import os
from datetime import datetime
def get_goes_data():
    # Define the folder path containing all files
    folder_path = './2023_events'
    data_by_date = {}  # Dictionary to hold data with date as key

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            # Extract the date from the filename, assuming it follows the 'YYYYMMDD' format
            date = filename[:8]  # Adjust if filename has different format

            # Define the full path to the file
            file_path = os.path.join(folder_path, filename)

            # List to hold each row's split data without '+'
            rows_data = []
            begin_end_times = []  # List to store beginning and ending times and the ninth element if condition is met

            # Open and process each line in the file
            start=False
            with open(file_path, 'r') as file:
                for line in file:
                    # print('<', line, '>')
                    if len(line)>1 :
                        if start:
                            # print(line)
                            start_time = datetime.strptime(line[11:15], "%H%M").time()
                            end_time = datetime.strptime(line[28:32], "%H%M").time()
                            flare_class = line[58]
                            if flare_class in ['A', 'B', 'C', 'M', 'X', 'S'] and line[59]!='T':
                                begin_end_times.append([start_time, end_time, flare_class])
                        else :
                            start = not(line[0] in ['#', ':'])
                        
                    
            if date in data_by_date:
                data_by_date[date].extend(begin_end_times)
            else:
                data_by_date[date] = begin_end_times

   
    return data_by_date
# get_goes_data()