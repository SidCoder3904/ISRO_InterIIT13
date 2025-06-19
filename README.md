# ISRO InterIIT 13.0: Lunar Elemental Analysis using X-Ray Fluorescence Spectroscopy

**Project Overview**: This project processes X-Ray Fluorescence (XRF) spectroscopy data from Chandrayaan-2's CLASS instrument to generate elemental abundance maps of the lunar surface with geospatial integration and machine learning-based compositional analysis.

## Table of Contents
- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Methodology](#methodology)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Data Processing Pipeline](#data-processing-pipeline)
- [File Format Specifications](#file-format-specifications)
- [Algorithm Details](#algorithm-details)
- [Results & Analysis](#results--analysis)
- [Performance Optimization](#performance-optimization)

## Overview

This project processes X-Ray Fluorescence (XRF) data from the Chandrayaan-2 CLASS instrument to generate elemental abundance maps of the lunar surface. The analysis focuses on major rock-forming elements including Silicon (Si), Aluminum (Al), Iron (Fe), Magnesium (Mg), and Calcium (Ca).

### Key Features:
- **FITS File Processing**: Automated processing of CLASS instrument FITS files
- **Solar Flare Classification**: Categorization of data based on solar flare activity levels (A, B, C, M, X classes)
- **Elemental Ratio Analysis**: Conversion of XRF spectra to elemental abundance ratios
- **Geospatial Mapping**: Generation of shapefiles and KML files for spatial visualization
- **Clustering Analysis**: K-means clustering for compositional grouping
- **Validation**: Comparison with Apollo and Luna mission ground truth data

## Project Architecture

### Directory Structure

```
ISRO_InterIIT13/                    # Main project directory
├── data/                           # Ground truth validation datasets
│   ├── apollo_11.csv              # Mare Tranquillitatis basalt samples (13 analyses)
│   ├── apollo_12.csv              # Oceanus Procellarum high-Ti basalts (13 analyses)
│   ├── apollo_14.csv              # Fra Mauro breccia samples (14 analyses)
│   ├── apollo_15.csv              # Hadley-Apennine anorthosite samples (13 analyses)
│   ├── apollo_16.csv              # Descartes highlands samples (13 analyses)
│   ├── luna_16.csv                # Mare Fecunditatis regolith samples (13 analyses)
│   ├── luna_20.csv                # Apollonius highlands samples (13 analyses)
│   └── luna_24.csv                # Mare Crisium samples (13 analyses)
├── Add Fits/                       # FITS file combination utilities
│   ├── add_fits.py                # Combines multiple FITS files into time-averaged spectra
│   ├── input/                     # Input FITS files
│   └── requirements.txt
├── Shapefile Generator/           # Geospatial data generation
│   ├── shape_add.py              # Converts FITS metadata to shapefiles
│   └── input/
├── RatioMapping/                  # Core elemental analysis pipeline
│   ├── catalogue.py              # Main FITS processing and cataloguing
│   ├── catalogue_to_shp.py       # Converts analysis results to shapefiles
│   ├── cluster.py                # K-means clustering analysis
│   ├── compostional_groups.py    # Compositional group visualization
│   ├── flux_fraction_data.csv    # XRF calibration data
│   ├── lunar_data.csv            # Processed lunar surface data
│   ├── output.csv                # Final elemental ratio results
│   └── fits/                     # Organized FITS files by solar class
├── final/                         # Analysis and visualization scripts
│   ├── elements_plot.py          # Element correlation plotting
│   ├── oxides_plot.py            # Oxide abundance visualization
│   ├── cluster.py                # Final clustering analysis
│   ├── catalogue_to_shp.py       # Final shapefile generation
│   └── output.csv                # Consolidated results
├── goes.py                        # GOES solar flare data processing
├── filter.py                      # FITS file filtering by solar activity
└── README.md
```

### Data Flow Architecture

```
Raw FITS Files → Solar Activity Classification → Spectral Processing → 
Elemental Ratios → Geospatial Maps → Validation
```

## Methodology

### 1. Solar Activity Classification System

The project uses GOES satellite data to classify solar flare activity:
- **Class A**: Background levels (1.0 to 9.9 × 10⁻⁸ W/m²)
- **Class B**: Low level (1.0 to 9.9 × 10⁻⁷ W/m²)
- **Class C**: Minor (1.0 to 9.9 × 10⁻⁶ W/m²)
- **Class M**: Moderate (1.0 to 9.9 × 10⁻⁵ W/m²)
- **Class X**: Major (≥ 1.0 × 10⁻⁴ W/m²)

### 2. XRF Data Processing
1. **FITS File Loading**: Load astronomical data files containing spectral information
2. **Spectral Analysis**: Extract characteristic X-ray peaks for each element
3. **Background Subtraction**: Remove continuum and noise components
4. **Peak Integration**: Calculate net peak areas for elemental lines
5. **Ratio Calculation**: Normalize elemental abundances relative to Silicon

### 3. Geospatial Processing
- **Coordinate Extraction**: Extract lunar coordinates from FITS headers (V0-V3 corner points)
- **Polygon Generation**: Create observation footprints
- **Shapefile Creation**: Generate ESRI format files for GIS analysis
- **KML Export**: Create Google Earth visualization format

### 4. Compositional Analysis
- **Clustering**: K-means algorithm for grouping similar compositions
- **Validation**: Compare with Apollo/Luna sample data
- **Visualization**: Generate multi-element correlation plots

## Installation & Setup

### Prerequisites
```bash
# Python 3.8 or higher
# Required packages
pip install -r requirements.txt
```

### Required Python Packages
```
astropy>=5.0
geopandas>=0.12.0
pandas>=1.4.0
matplotlib>=3.5.0
numpy>=1.21.0
scikit-learn>=1.1.0
shapely>=1.8.0
simplekml>=1.3.0
```

### Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Place FITS files in appropriate input directories
4. Configure file paths in processing scripts

## Usage Guide

### 1. Solar Flare Data Processing
```python
from goes import get_goes_data
from filter import filter_fits_files

# Process GOES data and classify FITS files
goes_data = get_goes_data()
# Files are automatically categorized by solar class (A, B, C, M, X)
```

### 2. FITS File Combination
```bash
cd "Add Fits"
python add_fits.py
# Combines multiple FITS files into time-averaged spectra
# Generates combined spectral data with proper exposure normalization
```

### 3. Elemental Analysis Pipeline
```bash
cd RatioMapping
python catalogue.py
# Processes all FITS files and generates elemental ratios
# Output: output.csv with elemental abundance data
```

### 4. Geospatial Analysis
```python
python catalogue_to_shp.py
# Generates shapefiles for different elemental ratios
# Creates Al/Si and Mg/Si ratio maps
```

### 5. Clustering Analysis
```python
python cluster.py
# Performs K-means clustering on elemental ratios
# Generates clustered shapefiles and visualizations
```

### 6. Visualization and Validation
```bash
cd final
python elements_plot.py  # Element correlation plots
python oxides_plot.py    # Oxide abundance comparisons
python compostional_groups.py  # Apollo mission comparisons
```

## Data Processing Pipeline

### Stage 1: Data Acquisition & Classification
```
FITS Files → Solar Activity Classification → Filtered Dataset
```

### Stage 2: Spectral Processing
```
Filtered FITS → Peak Detection → Background Subtraction → Net Peak Areas
```

### Stage 3: Geospatial Integration
```
Elemental Ratios → Coordinate Mapping → Polygon Generation → Shapefiles/KML
```

### Stage 4: Analysis & Validation
```
Geospatial Data → Clustering Analysis → Compositional Groups → Validation
```

## File Format Specifications

### 1. FITS File Structure

#### Primary HDU (Header Data Unit)
```
SIMPLE  = T               / Standard FITS format
BITPIX  = 8               / 8-bit data
NAXIS   = 0               / No primary data array
EXTEND  = T               / Contains extensions
ORIGIN  = 'ISRO'          / Data origin
TELESCOP= 'CHANDRAYAAN-2' / Mission name
INSTRUME= 'CLASS'         / Instrument name
OBJECT  = 'LUNAR_SURFACE' / Target object
DATE-OBS= '2024-03-23T17:07:42.389' / Observation date
EXPTIME = 8.0             / Exposure time in seconds
```

#### Required Keywords for Analysis
```python
required_keywords = {
    'EXPOSURE': float,      # Integration time (seconds)
    'GAIN': float,          # Energy calibration gain (eV/channel)
    'OFFSET': float,        # Energy calibration offset (eV)
    'TEMP': float,          # Detector temperature (°C)
    'V0_LAT': float,        # Corner 0 latitude
    'V0_LON': float,        # Corner 0 longitude
    'V1_LAT': float,        # Corner 1 latitude
    'V1_LON': float,        # Corner 1 longitude
    'V2_LAT': float,        # Corner 2 latitude
    'V2_LON': float,        # Corner 2 longitude
    'V3_LAT': float,        # Corner 3 latitude
    'V3_LON': float,        # Corner 3 longitude
    'STARTIME': str,        # Start time (UTC)
    'ENDTIME': str,         # End time (UTC)
}
```

### 2. Output CSV Schema (output.csv)
```python
csv_schema = {
    'file_name': 'str',           # Source FITS filename
    'start_time': 'datetime64',   # Observation start time (UTC)
    'end_time': 'datetime64',     # Observation end time (UTC)
    'v0_lon': 'float64',          # Corner 0 longitude (degrees)
    'v0_lat': 'float64',          # Corner 0 latitude (degrees)
    'v1_lon': 'float64',          # Corner 1 longitude (degrees)
    'v1_lat': 'float64',          # Corner 1 latitude (degrees)
    'v2_lon': 'float64',          # Corner 2 longitude (degrees)
    'v2_lat': 'float64',          # Corner 2 latitude (degrees)
    'v3_lon': 'float64',          # Corner 3 longitude (degrees)
    'v3_lat': 'float64',          # Corner 3 latitude (degrees)
    'ratio_Al': 'float64',        # Aluminum abundance ratio
    'ratio_Ca': 'float64',        # Calcium abundance ratio
    'ratio_Si': 'float64',        # Silicon abundance ratio (reference)
    'ratio_O': 'float64',         # Oxygen abundance ratio
    'ratio_Fe': 'float64',        # Iron abundance ratio
    'ratio_Mg': 'float64',        # Magnesium abundance ratio
    'solar_class': 'str'          # Solar activity classification
}
```

## Algorithm Details

### 1. Peak Detection and Integration

```python
def integrate_elemental_peaks(energies, net_counts, element_lines):
    """
    Integrates characteristic X-ray peaks for each element
    
    Peak integration windows (keV):
    - Mg Kα: 1.20-1.30 keV
    - Al Kα: 1.44-1.54 keV  
    - Si Kα: 1.69-1.79 keV
    - Ca Kα: 3.64-3.74 keV
    - Fe Kα: 6.35-6.45 keV
    """
    peak_areas = {}
    peak_errors = {}
    
    for element, line_energy in element_lines.items():
        # Define integration window (±50 eV around line center)
        window_low = line_energy - 0.05
        window_high = line_energy + 0.05
        
        # Integrate counts within window
        mask = (energies >= window_low) & (energies <= window_high)
        peak_area = np.sum(net_counts[mask])
        
        # Calculate statistical uncertainty (Poisson statistics)
        peak_error = np.sqrt(peak_area) if peak_area > 0 else 0
        
        peak_areas[element] = peak_area
        peak_errors[element] = peak_error
    
    return peak_areas, peak_errors
```

### 2. Background Subtraction

```python
def background_subtraction(energies, counts, bg_windows):
    """
    Performs background subtraction using linear interpolation
    
    Background windows typically:
    - Low energy: 1.0-1.3 keV (below Mg Kα)
    - High energy: 8.5-10.0 keV (above Fe Kβ)
    """
    # Linear background model
    bg_low = np.mean(counts[(energies >= bg_windows[0][0]) & 
                           (energies <= bg_windows[0][1])])
    bg_high = np.mean(counts[(energies >= bg_windows[1][0]) & 
                            (energies <= bg_windows[1][1])])
    
    # Interpolate background across energy range
    background = np.interp(energies, 
                          [np.mean(bg_windows[0]), np.mean(bg_windows[1])],
                          [bg_low, bg_high])
    
    net_counts = counts - background
    return net_counts, background
```

### 3. K-means Clustering Implementation

```python
def perform_clustering(elemental_ratios, n_clusters=5):
    """
    K-means clustering for compositional analysis
    
    Features used:
    - Al/Si ratio (highland/mare discrimination)
    - Mg/Si ratio (mafic mineral content)
    - Fe/Si ratio (iron enrichment)
    - Ca/Si ratio (plagioclase abundance)
    """
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    
    # Prepare feature matrix
    features = np.column_stack([
        elemental_ratios['Al'] / elemental_ratios['Si'],
        elemental_ratios['Mg'] / elemental_ratios['Si'],
        elemental_ratios['Fe'] / elemental_ratios['Si'],
        elemental_ratios['Ca'] / elemental_ratios['Si']
    ])
    
    # Standardize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # Perform clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(features_scaled)
    
    return cluster_labels, kmeans.cluster_centers_
```

## Results & Analysis

The analysis generates several key outputs:

### 1. Elemental Abundance Maps
- **Al/Si Ratio Maps**: Highland vs. mare discrimination
- **Mg/Si Ratio Maps**: Mafic mineral abundance
- **Fe/Al Ratio Maps**: Iron enrichment patterns
- **Ca/Si Ratio Maps**: Plagioclase distribution

### 2. Compositional Classifications
- **Cluster 1**: Anorthositic highlands (high Al/Si)
- **Cluster 2**: Basaltic maria (high Fe/Si, Mg/Si)
- **Cluster 3**: Mixed compositions (transition zones)
- **Cluster 4**: Impact-modified materials
- **Cluster 5**: Evolved compositions

### 3. Data Products
- **CSV Files**: Tabulated elemental ratios with coordinates
- **Shapefiles**: GIS-compatible polygon datasets
- **KML Files**: Google Earth visualization layers
- **Statistical Analysis**: Clustering results and validation metrics

## Performance Optimization

### 1. Memory Management

```python
def optimize_memory_usage():
    """
    Memory optimization techniques for large dataset processing
    """
    # Use efficient data types
    dtype_mapping = {
        'coordinates': np.float32,    # Sufficient precision for coordinates
        'ratios': np.float64,         # High precision for elemental ratios
        'counts': np.uint32,          # Integer counts
        'energies': np.float32        # Energy values
    }
    
    # Process data in chunks to avoid memory overflow
    chunk_size = 1000  # Process 1000 files at a time
```

### 2. Parallel Processing

```python
def parallel_fits_processing(file_list, n_processes=4):
    """
    Implements multiprocessing for FITS file analysis
    """
    from multiprocessing import Pool, cpu_count
    import functools
    
    # Determine optimal number of processes
    n_processes = min(n_processes, cpu_count())
    
    # Create partial function with fixed parameters
    process_func = functools.partial(
        process_single_fits_file,
        background_windows=[(1.0, 1.3), (8.5, 10.0)],
        element_lines={'Al': 1.487, 'Si': 1.740, 'Fe': 6.404, 'Mg': 1.254, 'Ca': 3.692}
    )
    
    # Process files in parallel
    with Pool(processes=n_processes) as pool:
        results = pool.map(process_func, file_list)
    
    return results
```

## Validation & Comparison

The project validates results against ground truth data from:

### Apollo Missions:
- **Apollo 11**: Mare Tranquillitatis (basaltic composition)
- **Apollo 12**: Oceanus Procellarum (high-Ti basalts)
- **Apollo 14**: Fra Mauro Formation (impact breccias)
- **Apollo 15**: Hadley-Apennine (anorthositic highlands)
- **Apollo 16**: Descartes Highlands (anorthositic composition)

### Luna Missions:
- **Luna 16**: Mare Fecunditatis sample return
- **Luna 20**: Apollonius Highlands sample return
- **Luna 24**: Mare Crisium sample return

### Conversion Factors (Oxide to Element):
```python
conversion_factors = {
    'SiO2': 0.4675,   # Silicon extraction
    'Al2O3': 0.5293,  # Aluminum extraction  
    'FeO': 0.7773,    # Iron extraction
    'MgO': 0.6031,    # Magnesium extraction
    'CaO': 0.7147     # Calcium extraction
}
```

## License & Acknowledgments

This project was developed for Inter IIT Tech Meet 13.0 ISRO Problem Statement.

**Data Sources:**
- Chandrayaan-2 CLASS instrument data (ISRO)
- GOES solar activity data (NOAA)
- Apollo sample data (NASA/LPI)
- Luna sample data (Roscosmos/Vernadsky Institute)
