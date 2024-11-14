import pandas as pd
import matplotlib.pyplot as plt
import os

# Conversion factors dictionary
conversion_factors = {
    'SiO2': 0.4675,
    'Al2O3': 0.5293,
    'FeO': 0.7773,
    'MgO': 0.6031,
    'CaO': 0.7147
}

# Folder containing CSV files
data_folder = './data'

# Load the output.csv file with your data
output_file = 'output.csv'
output_data = pd.read_csv(output_file)

# Extract your data columns (these are already factored, so no conversion is needed)
output_ratios = output_data[['ratio_Al', 'ratio_Ca', 'ratio_Si', 'ratio_O', 'ratio_Fe', 'ratio_Mg']]

# Initialize empty dictionary to store data from all missions
mission_data = {}

# Load all CSV files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        mission_name = filename.replace('.csv', '')
        filepath = os.path.join(data_folder, filename)
        
        # Read CSV file
        df = pd.read_csv(filepath)
        
        # Set the first column as index for easier access to Composition Type
        df.set_index('Composition Type', inplace=True)
        
        # Convert all data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')
        
        # Apply conversion factors without replacing NaN with 0
        for compound, factor in conversion_factors.items():
            if compound in df.index:
                df.loc[compound] = df.loc[compound] * factor  # Do not fill NaN, just multiply
        
        # Store in dictionary
        mission_data[mission_name] = df

# Plot SiO2 vs Al2O3
plt.figure(figsize=(8, 6))
for mission_name, df in mission_data.items():
    if 'SiO2' in df.index and 'Al2O3' in df.index:
        # Filter out NaN values from both SiO2 and Al2O3
        siO2_values = df.loc['SiO2'].dropna()
        al2O3_values = df.loc['Al2O3'].dropna()
        
        # Only plot if both SiO2 and Al2O3 have matching valid (non-NaN) values
        valid_siO2 = siO2_values[siO2_values.index.isin(al2O3_values.index)]  # Ensure matching indices
        valid_al2O3 = al2O3_values[al2O3_values.index.isin(valid_siO2.index)]  # Ensure matching indices
        
        if not valid_siO2.empty and not valid_al2O3.empty:
            plt.scatter(valid_siO2, valid_al2O3, label=mission_name)

# Plot your data (output.csv)
plt.scatter(output_ratios['ratio_Si'], output_ratios['ratio_Al'], label='Your Data', color='red', marker='x', s=100)

plt.xlabel('Si (%)')
plt.ylabel('Al (%)')
plt.legend()
plt.title('Si vs Al')
plt.show()

# Plot SiO2 vs MgO
plt.figure(figsize=(8, 6))
for mission_name, df in mission_data.items():
    if 'SiO2' in df.index and 'MgO' in df.index:
        # Filter out NaN values from both SiO2 and MgO
        siO2_values = df.loc['SiO2'].dropna()
        MgO_values = df.loc['MgO'].dropna()
        
        # Only plot if both SiO2 and MgO have matching valid (non-NaN) values
        valid_siO2 = siO2_values[siO2_values.index.isin(MgO_values.index)]  # Ensure matching indices
        valid_mgo = MgO_values[MgO_values.index.isin(valid_siO2.index)]  # Ensure matching indices
        
        if not valid_siO2.empty and not valid_mgo.empty:
            plt.scatter(valid_siO2, valid_mgo, label=mission_name)

# Plot your data (output.csv)
plt.scatter(output_ratios['ratio_Si'], output_ratios['ratio_Mg'], label='Your Data', color='red', marker='x', s=100)

plt.xlabel('Si (%)')
plt.ylabel('Mg (%)')
plt.legend()
plt.title('Si vs Mg')
plt.show()

# Plot Al2O3 vs MgO
plt.figure(figsize=(8, 6))
for mission_name, df in mission_data.items():
    if 'Al2O3' in df.index and 'MgO' in df.index:
        # Filter out NaN values from both Al2O3 and MgO
        al2o3_values = df.loc['Al2O3'].dropna()
        mgo_values = df.loc['MgO'].dropna()
        
        # Only plot if both Al2O3 and MgO have matching valid (non-NaN) values
        valid_al2o3 = al2o3_values[al2o3_values.index.isin(mgo_values.index)]  # Ensure matching indices
        valid_mgo = mgo_values[mgo_values.index.isin(valid_al2o3.index)]  # Ensure matching indices
        
        if not valid_al2o3.empty and not valid_mgo.empty:
            plt.scatter(valid_al2o3, valid_mgo, label=mission_name)

# Plot your data (output.csv)
plt.scatter(output_ratios['ratio_Al'], output_ratios['ratio_Mg'], label='Your Data', color='red', marker='x', s=100)

plt.xlabel('Al (%)')
plt.ylabel('Mg (%)')
plt.legend()
plt.title('Al vs Mg')
plt.show()
