import pandas as pd
import matplotlib.pyplot as plt
import os


# Folder containing CSV files
data_folder = './data'

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
plt.xlabel('SiO2 (%)')
plt.ylabel('Al2O3 (%)')
plt.legend()
plt.title('SiO2 vs Al2O3')
plt.show()

# Plot SiO2 vs MgO
plt.figure(figsize=(8, 6))
for mission_name, df in mission_data.items():
    if 'SiO2' in df.index and 'MgO' in df.index:
        # Filter out NaN values from both SiO2 and Al2O3
        siO2_values = df.loc['SiO2'].dropna()
        mgo_values = df.loc['MgO'].dropna()
        
        # Only plot if both SiO2 and Al2O3 have matching valid (non-NaN) values
        valid_siO2 = siO2_values[siO2_values.index.isin(mgo_values.index)]  # Ensure matching indices
        valid_mgo = mgo_values[mgo_values.index.isin(valid_siO2.index)]  # Ensure matching indices
        
        if not valid_siO2.empty and not valid_mgo.empty:
            plt.scatter(valid_siO2, valid_mgo, label=mission_name)
plt.xlabel('SiO2 (%)')
plt.ylabel('MgO (%)')
plt.legend()
plt.title('SiO2 vs MgO')
plt.show()

# Plot SiO2 vs FeO
plt.figure(figsize=(8, 6))
for mission_name, df in mission_data.items():
    if 'SiO2' in df.index and 'FeO' in df.index:
        # Filter out NaN values from both SiO2 and FeO
        siO2_values = df.loc['SiO2'].dropna()
        feO_values = df.loc['FeO'].dropna()
        
        # Only plot if both SiO2 and FeO have matching valid (non-NaN) values
        valid_siO2 = siO2_values[siO2_values.index.isin(feO_values.index)]  # Ensure matching indices
        valid_feO = feO_values[feO_values.index.isin(valid_siO2.index)]  # Ensure matching indices
        
        if not valid_siO2.empty and not valid_feO.empty:
            plt.scatter(valid_siO2, valid_feO, label=mission_name)
plt.xlabel('SiO2 (%)')
plt.ylabel('FeO (%)')
plt.legend()
plt.title('SiO2 vs FeO')
plt.show()

# Plot SiO2 vs MgO vs CaO
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
for mission_name, df in mission_data.items():
    if 'SiO2' in df.index and 'MgO' in df.index and 'CaO' in df.index:
        # Filter out NaN values from all three columns
        al2o3_values = df.loc['Al2O3'].dropna()
        mgO_values = df.loc['MgO'].dropna()
        siO2_values = df.loc['SiO2'].dropna()
        
        # Only plot if all three values (SiO2, MgO, CaO) have matching valid (non-NaN) values
        valid_siO2 = siO2_values[siO2_values.index.isin(mgO_values.index) & siO2_values.index.isin(al2o3_values.index)]  # Ensure matching indices
        valid_mgO = mgO_values[mgO_values.index.isin(valid_siO2.index) & mgO_values.index.isin(al2o3_values.index)]  # Ensure matching indices
        valid_al2o3 = al2o3_values[al2o3_values.index.isin(valid_siO2.index) & al2o3_values.index.isin(valid_mgO.index)]  # Ensure matching indices
        
        if not valid_siO2.empty and not valid_mgO.empty and not valid_al2o3.empty:
            ax.scatter(valid_siO2, valid_mgO, valid_al2o3, label=mission_name)
ax.set_xlabel('Al2O3 (%)')
ax.set_ylabel('MgO (%)')
ax.set_zlabel('SiO2 (%)')
plt.legend()
plt.title('SiO2 vs MgO vs Al2O3')
plt.show()
