import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import os
from simplekml import Kml
import matplotlib.colors as mcolors

# Function to determine color based on ratio value
def get_color_for_ratio(value, cmap_name='viridis'):
    cmap = plt.get_cmap(cmap_name)
    norm = mcolors.Normalize(vmin=0, vmax=1.5)
    return mcolors.to_hex(cmap(norm(value)))

# Function to create shapefiles and KML files with color-coded polygons
def generate_shapefile_and_kml_from_csv(csv_file, output_dir):
    # Load CSV data
    data = pd.read_csv(csv_file)

    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Initialize list to hold the overall ratios and polygons
    overall_polygons = []
    overall_ratios = []

    for ratio_name in ['Al_Si', 'Mg_Si']:
        polygons = []
        colors = []
        ratios = []

        # Loop through each row in the CSV to create polygons and assign colors
        for _, row in data.iterrows():
            coordinates = [
                (row['V0_LON'.lower()], row['V0_LAT'.lower()]),
                (row['V1_LON'.lower()], row['V1_LAT'.lower()]),
                (row['V2_LON'.lower()], row['V2_LAT'.lower()]),
                (row['V3_LON'.lower()], row['V3_LAT'.lower()]),
                (row['V0_LON'.lower()], row['V0_LAT'.lower()])  
            ]

            polygon = Polygon(coordinates)
            polygons.append(polygon)

            if ratio_name == 'Al_Si':
                ratio_value = row['ratio_Al'] / row['ratio_Si']
            else:
                ratio_value = row['ratio_Mg'] / row['ratio_Si']
                
            ratios.append(ratio_value)
            colors.append(get_color_for_ratio(ratio_value))

            # Add to overall list (to be used in Overall shapefile)
            overall_ratios.append({
                'geometry': polygon,
                'Al_Si_ratio': row['ratio_Al'] / row['ratio_Si'],
                'Mg_Si_ratio': row['ratio_Mg'] / row['ratio_Si'],
            })

        # Create a GeoDataFrame for each ratio
        gdf = gpd.GeoDataFrame({
            'geometry': polygons,
            f'{ratio_name}_ratio': ratios,
            'color': colors
        }, crs="EPSG:4326")

        # Create directory for the current ratio
        ratio_dir = os.path.join(output_dir, ratio_name)
        os.makedirs(ratio_dir, exist_ok=True)

        # Save shapefile
        shapefile_output = os.path.join(ratio_dir, f"{ratio_name}_ratio.shp")
        gdf.to_file(shapefile_output, driver="ESRI Shapefile")
        print(f"Shapefile saved as {shapefile_output}")

        # Save KML file
        kml = Kml()
        for _, row in gdf.iterrows():
            pol = kml.newpolygon(name=f"{ratio_name}_ratio_{row[ratio_name + '_ratio']:.2f}")
            pol.outerboundaryis = [(coord[0], coord[1]) for coord in row['geometry'].exterior.coords]
            pol.style.polystyle.color = get_color_for_ratio(row[ratio_name + '_ratio'])
        
        kml_output = os.path.join(ratio_dir, f"{ratio_name}_ratio.kml")
        kml.save(kml_output)
        print(f"KML file saved as {kml_output}")

        # Optional: Plot to visualize color-coding
        fig, ax = plt.subplots()
        gdf.plot(column='color', ax=ax, legend=True, color=colors)
        plt.show()

    # Create "Overall" directory and save shapefile with all ratios (without colors)
    overall_dir = os.path.join(output_dir, "Overall")
    os.makedirs(overall_dir, exist_ok=True)

    overall_gdf = gpd.GeoDataFrame(overall_ratios, crs="EPSG:4326")
    overall_shapefile_output = os.path.join(overall_dir, "overall_ratios.shp")
    overall_gdf.to_file(overall_shapefile_output, driver="ESRI Shapefile")
    print(f"Overall shapefile saved as {overall_shapefile_output}")

# Usage
csv_file = "output.csv"                 # CSV file with FITS file data
output_dir = "./output"                 # Output folder
generate_shapefile_and_kml_from_csv(csv_file, output_dir)
