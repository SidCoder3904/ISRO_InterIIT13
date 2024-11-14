import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon
import os
from simplekml import Kml
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans
import numpy as np

# Function to determine color based on cluster index
def get_color_for_cluster(cluster_index, cmap_name='tab20'):
    cmap = plt.get_cmap(cmap_name)
    norm = mcolors.Normalize(vmin=0, vmax=10)  # Set number of clusters in the color map range
    return mcolors.to_hex(cmap(norm(cluster_index)))

# Function to perform clustering and create shapefiles and KML files
def generate_cluster_shapefile_and_kml_from_csv(csv_file, output_dir):
    # Load CSV data
    data = pd.read_csv(csv_file)

    # Extract the ratios for clustering
    ratios = []
    for _, row in data.iterrows():
        ratio_Al_Si = row['ratio_Al'] / row['ratio_Si']
        ratio_Mg_Si = row['ratio_Mg'] / row['ratio_Si']
        ratios.append([ratio_Al_Si, ratio_Mg_Si])

    ratios = np.array(ratios)

    # Perform clustering (e.g., KMeans)
    num_clusters = 5  # You can adjust the number of clusters
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(ratios)
    labels = kmeans.labels_

    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Prepare data for shapefile and KML
    polygons = []
    cluster_labels = []

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
        cluster_labels.append(labels[_])  # Assign the cluster label to the polygon

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame({
        'geometry': polygons,
        'cluster': cluster_labels
    }, crs="EPSG:4326")

    # Create directory for clusters
    cluster_dir = os.path.join(output_dir, "clusters")
    os.makedirs(cluster_dir, exist_ok=True)

    # Save shapefile
    shapefile_output = os.path.join(cluster_dir, "clustered_shapefile.shp")
    gdf.to_file(shapefile_output, driver="ESRI Shapefile")
    print(f"Clustered shapefile saved as {shapefile_output}")

    # Save KML file
    kml = Kml()
    for _, row in gdf.iterrows():
        cluster_color = get_color_for_cluster(row['cluster'])
        pol = kml.newpolygon(name=f"Cluster {row['cluster']}")
        pol.outerboundaryis = [(coord[0], coord[1]) for coord in row['geometry'].exterior.coords]
        pol.style.polystyle.color = cluster_color
    
    kml_output = os.path.join(cluster_dir, "clustered.kml")
    kml.save(kml_output)
    print(f"Clustered KML file saved as {kml_output}")

    # Optional: Plot to visualize clusters
    fig, ax = plt.subplots()
    gdf.plot(column='cluster', ax=ax, legend=True, cmap='tab20')
    plt.title("Clustering of Element Ratios")
    plt.show()

# Usage
csv_file = "output.csv"  # CSV file with FITS file data
output_dir = "./output_cluster"  # Output folder for clustered shapefile/KML
generate_cluster_shapefile_and_kml_from_csv(csv_file, output_dir)
