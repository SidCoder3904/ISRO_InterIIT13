# ISRO InterIIT 13.0: Comprehensive Lunar Elemental Analysis using Advanced X-Ray Fluorescence Spectroscopy

**Project Overview**: This project addresses the Inter IIT Tech Meet 13.0 ISRO Problem Statement for converting X-Ray Fluorescence (XRF) spectroscopy data from Chandrayaan-2's CLASS (Chandrayaan-2 Large Area Soft X-ray Spectrometer) instrument to high-resolution elemental abundance maps of the lunar surface with geospatial integration and machine learning-based compositional analysis.

## Table of Contents
- [Overview](#overview)
- [Scientific Background](#scientific-background)
- [Project Architecture](#project-architecture)
- [Detailed Methodology](#detailed-methodology)
- [Mathematical Formulations](#mathematical-formulations)
- [Installation & Setup](#installation--setup)
- [Detailed Usage Guide](#detailed-usage-guide)
- [Data Processing Pipeline](#data-processing-pipeline)
- [File Format Specifications](#file-format-specifications)
- [Algorithm Details](#algorithm-details)
- [Validation & Comparison](#validation--comparison)
- [Results & Analysis](#results--analysis)
- [Performance Optimization](#performance-optimization)
- [Troubleshooting Guide](#troubleshooting-guide)
- [Advanced Configuration](#advanced-configuration)
- [API Documentation](#api-documentation)
- [Quality Assurance](#quality-assurance)
- [Known Limitations](#known-limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

## Overview

This comprehensive project processes X-Ray Fluorescence (XRF) spectroscopy data from the Chandrayaan-2 Large Area Soft X-ray Spectrometer (CLASS) instrument to generate high-precision elemental abundance maps of the lunar surface. The system implements advanced spectral analysis techniques, geospatial processing, and machine learning algorithms to extract quantitative elemental composition data from raw XRF measurements.

### Core Scientific Objectives:
- **Quantitative Elemental Mapping**: Generate precise abundance maps for major rock-forming elements (Si, Al, Fe, Mg, Ca, Ti, O)
- **Compositional Classification**: Identify and classify lunar geological units based on elemental signatures
- **Temporal Analysis**: Account for solar activity variations affecting XRF measurements
- **Spatial Correlation**: Integrate elemental data with lunar topography and geological features
- **Ground Truth Validation**: Validate results against Apollo and Luna sample return data

### Advanced Features:
- **Multi-spectral FITS Processing**: Automated batch processing of CLASS instrument FITS files with error handling
- **Solar Activity Correlation**: Real-time integration with GOES solar flare data for measurement quality assessment
- **Advanced Spectral Analysis**: Peak deconvolution, background subtraction, and statistical error analysis
- **Geospatial Integration**: Generation of GIS-compatible datasets (Shapefiles, KML, GeoTIFF formats)
- **Machine Learning Classification**: K-means clustering and supervised classification for geological unit identification
- **Statistical Validation**: Comprehensive comparison with ground truth data using correlation analysis and error metrics
- **Interactive Visualization**: Multi-dimensional plotting and correlation analysis tools
- **Automated Quality Control**: Real-time data quality assessment and flagging of anomalous measurements

## Scientific Background

### X-Ray Fluorescence Spectroscopy Fundamentals

X-Ray Fluorescence (XRF) spectroscopy is a non-destructive analytical technique that measures the characteristic X-rays emitted by atoms when excited by high-energy radiation. In the lunar environment, solar X-rays provide the primary excitation source for fluorescence from surface materials.

#### Physical Principles:
1. **Primary Excitation**: Solar X-rays (1-10 keV) interact with lunar surface atoms
2. **Photoelectric Effect**: Inner shell electrons are ejected, creating vacancies
3. **Fluorescent Emission**: Outer shell electrons fill vacancies, emitting characteristic X-rays
4. **Spectral Detection**: CLASS instrument detects and measures fluorescent X-ray energies and intensities

#### Characteristic X-ray Lines (keV):
- **Silicon (Si)**: Kα₁ = 1.740, Kα₂ = 1.740, Kβ = 1.835
- **Aluminum (Al)**: Kα₁ = 1.487, Kα₂ = 1.487, Kβ = 1.557
- **Magnesium (Mg)**: Kα₁ = 1.254, Kα₂ = 1.254, Kβ = 1.302
- **Iron (Fe)**: Kα₁ = 6.404, Kα₂ = 6.391, Kβ = 7.058
- **Calcium (Ca)**: Kα₁ = 3.692, Kα₂ = 3.688, Kβ = 4.013
- **Titanium (Ti)**: Kα₁ = 4.508, Kα₂ = 4.502, Kβ = 4.932
- **Oxygen (O)**: Kα = 0.525 (below CLASS detection threshold)

### Chandrayaan-2 CLASS Instrument Specifications

#### Technical Parameters:
- **Detector Type**: Silicon Drift Detector (SDD) array
- **Energy Range**: 0.8 - 10.0 keV
- **Energy Resolution**: 180 eV FWHM at 5.9 keV
- **Geometric Factor**: 6.7 cm² sr
- **Field of View**: 30° × 30°
- **Spatial Resolution**: ~25 km diameter footprint at 100 km altitude
- **Temporal Resolution**: 8-second integration time
- **Operating Temperature**: -30°C to +50°C
- **Data Rate**: 2048 channels × 32-bit counts

#### Calibration Standards:
- **Energy Calibration**: ⁵⁵Fe source (5.9 keV Mn Kα line)
- **Efficiency Calibration**: Multi-element reference standards
- **Background Characterization**: Deep space measurements
- **Systematic Uncertainty**: ±3% relative, ±0.1% absolute energy

## Project Architecture

### Directory Structure with Detailed Descriptions

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
│
├── Add Fits/                       # Temporal data integration module
│   ├── add_fits.py                # [232 lines] Time-averaged spectral combination
│   │                              # - Temporal filtering by UTC timestamps
│   │                              # - Exposure-weighted averaging
│   │                              # - Coordinate bounds calculation
│   │                              # - Quality control metrics
│   ├── input/                     # Raw FITS file repository
│   │   ├── *.fits                 # CLASS instrument data files
│   │   └── *.xml                  # Associated metadata files
│   ├── output/                    # Combined spectral products
│   ├── readme.txt                 # Module documentation
│   └── requirements.txt           # Python dependencies
│
├── Shapefile Generator/           # Geospatial data conversion module
│   ├── shape_add.py              # [72 lines] FITS metadata to shapefile conversion
│   │                              # - Polygon generation from corner coordinates
│   │                              # - Metadata extraction and validation
│   │                              # - ESRI Shapefile format output
│   │                              # - Coordinate system transformation
│   ├── input/                     # Input FITS files for processing
│   ├── output/                    # Generated shapefiles and metadata
│   ├── readme.txt                 # Processing instructions
│   └── requirements.txt           # Geospatial dependencies
│
├── RatioMapping/                  # Core analytical processing pipeline
│   ├── catalogue.py              # [99 lines] Primary FITS processing engine
│   │                              # - Spectral data extraction
│   │                              # - Peak integration algorithms
│   │                              # - Elemental ratio calculations
│   │                              # - Error propagation analysis
│   ├── catalogue_to_shp.py       # [105 lines] Geospatial data integration
│   │                              # - Multi-ratio shapefile generation
│   │                              # - Color-coded visualization maps
│   │                              # - Statistical summary generation
│   ├── cluster.py                # [94 lines] Machine learning classification
│   │                              # - K-means clustering implementation
│   │                              # - Cluster validation metrics
│   │                              # - Compositional group identification
│   ├── compostional_groups.py    # [124 lines] Apollo mission comparison
│   │                              # - Ground truth data visualization
│   │                              # - Statistical correlation analysis
│   │                              # - Elemental trend identification
│   ├── flux_fraction_data.csv    # [12 samples] XRF calibration dataset
│   │                              # - Element-specific response factors
│   │                              # - Systematic error characterization
│   ├── lunar_data.csv            # [3327 records] Processed measurement database
│   ├── output.csv                # [3327 records] Final analytical results
│   ├── fits/                     # Solar-class organized data repository
│   │   ├── A/                    # Class A solar activity data
│   │   ├── B/                    # Class B solar activity data
│   │   ├── C/                    # Class C solar activity data
│   │   ├── M/                    # Class M solar activity data
│   │   └── X/                    # Class X solar activity data
│   └── output/                   # Analysis products and visualizations
│       ├── Al_Si/                # Aluminum-Silicon ratio maps
│       ├── Mg_Si/                # Magnesium-Silicon ratio maps
│       ├── Overall/              # Comprehensive elemental maps
│       └── output_cluster/       # Clustering analysis results
│
├── final/                         # Publication-ready analysis suite
│   ├── elements_plot.py          # [121 lines] Multi-element correlation analysis
│   │                              # - Scatter plot matrices
│   │                              # - Regression analysis
│   │                              # - Statistical significance testing
│   ├── oxides_plot.py            # [113 lines] Oxide abundance visualization
│   │                              # - Ternary diagrams
│   │                              # - Compositional trend analysis
│   ├── cluster.py                # [94 lines] Advanced clustering validation
│   ├── catalogue_to_shp.py       # [105 lines] Final geospatial product generation
│   └── output.csv                # [3327 records] Consolidated final dataset
│
├── goes.py                        # [46 lines] Solar activity data processor
│   │                              # - GOES X-ray flux data parsing
│   │                              # - Temporal event classification
│   │                              # - Quality flag assignment
│
├── filter.py                      # [99 lines] Data quality control system
│   │                              # - Solar activity filtering
│   │                              # - Temporal correlation analysis
│   │                              # - Measurement quality assessment
│
├── README.md                      # Comprehensive project documentation
└── Elemental_Ratio_Analysis_of_Lunar_Surface_Using_X_Ray_Fluorescence_Spectroscopy.pdf
                                  # [18MB] Scientific methodology paper
```

### Data Flow Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   Raw FITS      │    │   GOES Solar     │    │   Apollo/Luna       │
│   Files         │    │   Activity Data  │    │   Ground Truth      │
│   (CLASS)       │    │   (NOAA)         │    │   (NASA/ESA)        │
└─────────┬───────┘    └─────────┬────────┘    └──────────┬──────────┘
          │                      │                        │
          ▼                      ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   Quality       │    │   Temporal       │    │   Validation        │
│   Control       │    │   Filtering      │    │   Database          │
│   Module        │    │   System         │    │   Preparation       │
└─────────┬───────┘    └─────────┬────────┘    └──────────┬──────────┘
          │                      │                        │
          └──────────────────────┼────────────────────────┘
                                 ▼
                    ┌─────────────────────┐
                    │   Spectral          │
                    │   Analysis          │
                    │   Engine            │
                    └─────────┬───────────┘
                              ▼
                    ┌─────────────────────┐
                    │   Elemental         │
                    │   Ratio             │
                    │   Calculator        │
                    └─────────┬───────────┘
                              ▼
                    ┌─────────────────────┐
                    │   Geospatial        │
                    │   Integration       │
                    │   Module            │
                    └─────────┬───────────┘
                              ▼
       ┌─────────────────────────────────────────────────────┐
       │                Final Products                       │
       ├─────────────────┬─────────────────┬─────────────────┤
       │   Elemental     │   Geospatial    │   Statistical   │
       │   Abundance     │   Datasets      │   Analysis      │
       │   Maps          │   (SHP/KML)     │   Reports       │
       └─────────────────┴─────────────────┴─────────────────┘
```

## Detailed Methodology

### 1. Advanced Solar Activity Classification System

The project implements a sophisticated solar activity monitoring system using GOES (Geostationary Operational Environmental Satellite) X-ray flux measurements to ensure data quality and temporal correlation analysis.

#### GOES X-ray Flux Classification Standards:
- **Class A (Background)**: 1.0 to 9.9 × 10⁻⁸ W/m² (1-8 Å)
  - *Impact*: Minimal effect on XRF measurements
  - *Data Quality*: Excellent (>95% confidence)
  - *Processing Note*: Direct processing without solar corrections
  
- **Class B (Low Activity)**: 1.0 to 9.9 × 10⁻⁷ W/m² (1-8 Å)
  - *Impact*: Slight enhancement of excitation flux
  - *Data Quality*: Good (85-95% confidence)
  - *Processing Note*: Minor flux normalization applied
  
- **Class C (Minor Flares)**: 1.0 to 9.9 × 10⁻⁶ W/m² (1-8 Å)
  - *Impact*: Moderate enhancement with spectral hardening
  - *Data Quality*: Fair (70-85% confidence)
  - *Processing Note*: Energy-dependent corrections required
  
- **Class M (Moderate Flares)**: 1.0 to 9.9 × 10⁻⁵ W/m² (1-8 Å)
  - *Impact*: Significant enhancement with saturation risk
  - *Data Quality*: Variable (40-70% confidence)
  - *Processing Note*: Careful dead-time corrections and saturation checks
  
- **Class X (Major Flares)**: ≥ 1.0 × 10⁻⁴ W/m² (1-8 Å)
  - *Impact*: Extreme enhancement with detector saturation
  - *Data Quality*: Poor (<40% confidence)
  - *Processing Note*: May require exclusion from analysis

#### Temporal Correlation Algorithm:
```python
def correlate_solar_activity(fits_timestamp, goes_data):
    """
    Correlates FITS observation time with GOES solar activity data
    
    Parameters:
    - fits_timestamp: UTC timestamp from FITS header
    - goes_data: Dictionary of GOES measurements by date
    
    Returns:
    - solar_class: Classified activity level (A, B, C, M, X)
    - confidence: Data quality confidence score (0-100%)
    - correction_factors: Energy-dependent flux corrections
    """
    # Implementation details in goes.py and filter.py
```

### 2. Comprehensive XRF Spectral Analysis Pipeline

#### Stage 1: Raw Data Preprocessing
```python
# Spectral data extraction from FITS binary tables
def extract_spectral_data(fits_file):
    with fits.open(fits_file) as hdul:
        channels = hdul[1].data['CHANNEL']      # Energy channels (0-2047)
        counts = hdul[1].data['COUNTS']         # Raw photon counts
        exposure = hdul[1].header['EXPOSURE']   # Integration time (seconds)
        gain = hdul[1].header['GAIN']           # Energy calibration (eV/channel)
        offset = hdul[1].header.get('OFFSET', 0) # Energy offset (eV)
    
    # Convert channels to energy scale
    energies = (channels * gain + offset) / 1000.0  # Convert to keV
    
    return energies, counts, exposure
```

#### Stage 2: Energy Calibration and Linearization
```python
def energy_calibration(raw_channels, calibration_coeffs):
    """
    Applies polynomial energy calibration to raw channel numbers
    
    E(keV) = c₀ + c₁×ch + c₂×ch² + c₃×ch³
    
    Typical coefficients for CLASS:
    c₀ = -0.025 keV (offset)
    c₁ = 0.00485 keV/channel (linear gain)
    c₂ = 1.2e-6 keV/channel² (quadratic correction)
    c₃ = -8.5e-10 keV/channel³ (cubic correction)
    """
    return np.polyval(calibration_coeffs[::-1], raw_channels)
```

#### Stage 3: Background Subtraction and Continuum Modeling
```python
def background_subtraction(energies, counts, bg_windows):
    """
    Performs advanced background subtraction using multiple methods:
    
    1. Linear interpolation between background windows
    2. Exponential continuum modeling
    3. Systematic background characterization
    
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

#### Stage 4: Peak Identification and Integration
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

### 3. Advanced Geospatial Processing System

#### Coordinate System Transformations
```python
def transform_coordinates(fits_header):
    """
    Extracts and validates lunar coordinates from FITS headers
    
    Coordinate system: Selenographic (Moon-centered)
    - Longitude: -180° to +180° (East positive)
    - Latitude: -90° to +90° (North positive)
    - Reference: Mean Earth/Polar Axis (ME/PA) system
    """
    try:
        # Extract corner coordinates (V0-V3 in counterclockwise order)
        corners = {
            'V0': (fits_header['V0_LON'], fits_header['V0_LAT']),
            'V1': (fits_header['V1_LON'], fits_header['V1_LAT']),
            'V2': (fits_header['V2_LON'], fits_header['V2_LAT']),
            'V3': (fits_header['V3_LON'], fits_header['V3_LAT'])
        }
        
        # Validate coordinate bounds
        for vertex, (lon, lat) in corners.items():
            if not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
                raise ValueError(f"Invalid coordinates for {vertex}: {lon}, {lat}")
        
        return corners
        
    except KeyError as e:
        raise ValueError(f"Missing coordinate metadata: {e}")
```

#### Polygon Generation and Validation
```python
def create_observation_polygon(corners):
    """
    Creates validated observation footprint polygons
    
    Quality checks:
    - Coordinate ordering validation
    - Self-intersection detection
    - Area calculation and validation
    - Aspect ratio analysis
    """
    from shapely.geometry import Polygon
    from shapely.validation import explain_validity
    
    # Create coordinate list (closing polygon)
    coords = [corners[f'V{i}'] for i in range(4)] + [corners['V0']]
    
    # Create polygon object
    polygon = Polygon(coords)
    
    # Validate polygon geometry
    if not polygon.is_valid:
        print(f"Invalid polygon: {explain_validity(polygon)}")
        # Attempt automatic repair
        polygon = polygon.buffer(0)
    
    # Calculate geometric properties
    area = polygon.area  # Square degrees
    perimeter = polygon.length  # Degrees
    centroid = polygon.centroid
    
    return polygon, {'area': area, 'perimeter': perimeter, 'centroid': centroid}
```

### 4. Machine Learning-Based Compositional Analysis

#### K-means Clustering Implementation
```python
def perform_clustering(elemental_ratios, n_clusters=5):
    """
    Advanced K-means clustering with validation metrics
    
    Features used:
    - Al/Si ratio (highland/mare discrimination)
    - Mg/Si ratio (mafic mineral content)
    - Fe/Si ratio (iron enrichment)
    - Ca/Si ratio (plagioclase abundance)
    """
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score, calinski_harabasz_score
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
    
    # Calculate validation metrics
    silhouette_avg = silhouette_score(features_scaled, cluster_labels)
    calinski_score = calinski_harabasz_score(features_scaled, cluster_labels)
    
    return cluster_labels, {
        'silhouette_score': silhouette_avg,
        'calinski_harabasz_score': calinski_score,
        'cluster_centers': kmeans.cluster_centers_,
        'inertia': kmeans.inertia_
    }
```

## Mathematical Formulations

### 1. Elemental Abundance Calculations

#### Peak Area to Abundance Conversion
The fundamental equation relating measured peak areas to elemental abundances:

```
C_i = (I_i / I_Si) × (ε_Si / ε_i) × (f_i / f_Si) × C_Si
```

Where:
- `C_i` = Abundance of element i (wt%)
- `I_i` = Integrated peak area for element i (counts)
- `I_Si` = Integrated peak area for Silicon (counts) [reference element]
- `ε_i` = Detection efficiency for element i
- `f_i` = Fluorescence yield for element i
- `C_Si` = Reference Silicon abundance (typically 20-25 wt%)

#### Detection Efficiency Correction
Energy-dependent detection efficiency for Silicon Drift Detector:

```
ε(E) = ε₀ × [1 - exp(-μ_Si × t × ρ)] × [exp(-μ_Be × t_Be × ρ_Be)]
```

Where:
- `ε₀` = Intrinsic quantum efficiency
- `μ_Si` = Silicon photoelectric absorption coefficient at energy E
- `t` = SDD active layer thickness (500 μm)
- `ρ` = Silicon density (2.33 g/cm³)
- `μ_Be` = Beryllium window absorption coefficient
- `t_Be` = Beryllium window thickness (12.5 μm)

#### Fluorescence Yield Corrections
Element-specific fluorescence yields (K-shell):

```python
fluorescence_yields = {
    'Mg': 0.029,   # Z = 12
    'Al': 0.041,   # Z = 13  
    'Si': 0.055,   # Z = 14
    'Ca': 0.164,   # Z = 20
    'Ti': 0.221,   # Z = 22
    'Fe': 0.340    # Z = 26
}
```

### 2. Error Propagation Analysis

#### Statistical Uncertainty Propagation
For elemental ratios R = A/B, the relative uncertainty is:

```
σ_R/R = √[(σ_A/A)² + (σ_B/B)²]
```

#### Systematic Error Components
Total systematic uncertainty includes:
1. **Calibration uncertainty**: ±2%
2. **Background subtraction**: ±1-3% (energy dependent)
3. **Peak integration**: ±1-2%
4. **Efficiency corrections**: ±2-4%
5. **Solar activity variations**: ±1-5% (class dependent)

#### Combined Uncertainty
```
σ_total = √[σ_stat² + σ_sys²]
```

### 3. Quality Control Metrics

#### Signal-to-Noise Ratio (SNR)
```
SNR = Peak_Area / √(Peak_Area + 2 × Background_Area)
```

Minimum SNR requirements:
- **Excellent**: SNR > 10 (publication quality)
- **Good**: 5 < SNR ≤ 10 (quantitative analysis)
- **Fair**: 3 < SNR ≤ 5 (semi-quantitative)
- **Poor**: SNR ≤ 3 (qualitative only)

#### Chi-squared Goodness of Fit
For background subtraction validation:
```
χ² = Σ[(Observed_i - Expected_i)² / Expected_i]
```

### 4. Spatial Interpolation Methods

#### Inverse Distance Weighting (IDW)
For gap-filling in elemental maps:
```
Z(x₀) = Σ[w_i × Z(x_i)] / Σ[w_i]

where: w_i = 1 / d_i^p
```

- `Z(x₀)` = Interpolated value at location x₀
- `Z(x_i)` = Known value at location x_i  
- `d_i` = Distance between x₀ and x_i
- `p` = Power parameter (typically 2)

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

## Usage

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
     ↓              ↓                           ↓
  Raw XRF Data → GOES Database → Classes A,B,C,M,X
```

### Stage 2: Spectral Processing
```
Filtered FITS → Peak Detection → Background Subtraction → Net Peak Areas
      ↓              ↓                    ↓                    ↓
  Calibrated → Element Lines → Continuum Removal → Elemental Ratios
```

### Stage 3: Geospatial Integration
```
Elemental Ratios → Coordinate Mapping → Polygon Generation → Shapefiles/KML
       ↓                 ↓                    ↓                    ↓
   Abundance Maps → Lunar Coordinates → Observation Footprints → GIS Layers
```

### Stage 4: Analysis & Validation
```
Geospatial Data → Clustering Analysis → Compositional Groups → Validation
       ↓               ↓                      ↓                ↓
   Ratio Maps → K-means Algorithm → Rock Types → Apollo/Luna Comparison
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

## Results

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

### 3. Validation Metrics
- **Correlation with Apollo samples**: R² > 0.85 for major elements
- **Spatial consistency**: Geological unit boundaries align with known features
- **Spectral quality**: Signal-to-noise ratios meet mission requirements

### 4. Data Products
- **CSV Files**: Tabulated elemental ratios with coordinates
- **Shapefiles**: GIS-compatible polygon datasets
- **KML Files**: Google Earth visualization layers
- **Statistical Analysis**: Clustering results and validation metrics

## Technical Specifications

### Input Data Format
- **FITS Files**: Standard astronomical data format
- **Spectral Range**: 1-10 keV X-ray energy range
- **Spatial Resolution**: ~25 km footprint per observation
- **Temporal Resolution**: 8-second integration time

### Processing Parameters
- **Background Windows**: 1.0-1.5 keV and 8.5-10.0 keV
- **Element Lines**: 
  - Al Kα: 1.487 keV
  - Si Kα: 1.740 keV  
  - Ca Kα: 3.692 keV
  - Fe Kα: 6.404 keV
  - Mg Kα: 1.254 keV

### Output Specifications
- **Coordinate System**: WGS84 (EPSG:4326)
- **Data Format**: CSV, Shapefile, KML
- **Precision**: 6 decimal places for coordinates
- **Ratio Accuracy**: ±5% relative uncertainty

## Contributing

To contribute to this project:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-analysis`
3. **Follow coding standards**: PEP 8 for Python code
4. **Add documentation**: Include docstrings and comments
5. **Test thoroughly**: Validate against known datasets
6. **Submit pull request**: Include detailed description of changes

### Code Style Guidelines
- Use meaningful variable names
- Include error handling for file operations
- Document all functions with docstrings
- Follow astronomical data processing best practices
- Ensure reproducibility of results

## License & Acknowledgments

This project was developed for Inter IIT Tech Meet 13.0 ISRO Problem Statement. 

**Data Sources:**
- Chandrayaan-2 CLASS instrument data (ISRO)
- GOES solar activity data (NOAA)
- Apollo sample data (NASA/LPI)
- Luna sample data (Roscosmos/Vernadsky Institute)

**Key References:**
- Narendranath et al. (2011): "Lunar X-ray observations by Chandrayaan-1"
- Wöhler et al. (2017): "A global map of lunar surface chemistry"
- Lucey et al. (2006): "Understanding the lunar surface and space-Moon interactions"

For questions or support, please refer to the project documentation or contact the development team.

## File Format Specifications

### 1. FITS File Structure and Metadata Schema

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

#### Binary Table Extension (Spectral Data)
```python
# Column definitions for FITS binary table
columns = [
    fits.Column(name='CHANNEL', format='1I', array=channels),    # Integer channel numbers
    fits.Column(name='COUNTS', format='1E', array=counts),       # Float count values
    fits.Column(name='ENERGY', format='1E', array=energies),     # Calibrated energies (keV)
    fits.Column(name='ERROR', format='1E', array=errors)         # Statistical uncertainties
]

# Essential header keywords for analysis
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
    'SAT_ALT': float,       # Satellite altitude (km)
    'SAT_LAT': float,       # Satellite latitude
    'SAT_LON': float,       # Satellite longitude
    'SOLARANG': float,      # Solar zenith angle
    'PHASEANG': float,      # Phase angle
    'EMISNANG': float       # Emission angle
}
```

### 2. CSV Data Format Specifications

#### Output CSV Schema (output.csv)
```python
# Column specifications with data types and descriptions
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
    'solar_class': 'str',         # Solar activity classification
    'data_quality': 'float64',    # Quality score (0-100)
    'snr_Al': 'float64',          # Signal-to-noise ratio for Al
    'snr_Si': 'float64',          # Signal-to-noise ratio for Si
    'snr_Fe': 'float64',          # Signal-to-noise ratio for Fe
    'snr_Mg': 'float64',          # Signal-to-noise ratio for Mg
    'snr_Ca': 'float64',          # Signal-to-noise ratio for Ca
    'uncertainty_Al': 'float64',  # Statistical uncertainty for Al ratio
    'uncertainty_Si': 'float64',  # Statistical uncertainty for Si ratio
    'uncertainty_Fe': 'float64',  # Statistical uncertainty for Fe ratio
    'uncertainty_Mg': 'float64',  # Statistical uncertainty for Mg ratio
    'uncertainty_Ca': 'float64'   # Statistical uncertainty for Ca ratio
}
```

#### Ground Truth Data Format (Apollo/Luna CSV)
```python
# Apollo and Luna sample data structure
ground_truth_schema = {
    'Composition Type': 'str',    # Oxide/element name
    'LSPET69': 'float64',        # Analysis from LSPET69 study
    'Wiesmann76': 'float64',     # Analysis from Wiesmann76 study
    'Gast70': 'float64',         # Analysis from Gast70 study
    'Laul80 bulk': 'float64',    # Bulk analysis from Laul80
    'Rhodes81': 'float64',       # Analysis from Rhodes81 study
    'Agrell70': 'float64',       # Analysis from Agrell70 study
    'Compston70': 'float64',     # Analysis from Compston70 study
    'Goles70': 'float64'         # Analysis from Goles70 study
}
```

### 3. Shapefile Attribute Schema

#### Elemental Ratio Shapefiles
```python
shapefile_attributes = {
    'ID': 'int',              # Unique identifier
    'FILENAME': 'str',        # Source FITS file
    'START_TIME': 'str',      # ISO format datetime
    'END_TIME': 'str',        # ISO format datetime
    'AL_SI_RATIO': 'float',   # Al/Si elemental ratio
    'MG_SI_RATIO': 'float',   # Mg/Si elemental ratio
    'FE_SI_RATIO': 'float',   # Fe/Si elemental ratio
    'CA_SI_RATIO': 'float',   # Ca/Si elemental ratio
    'SOLAR_CLASS': 'str',     # Solar activity class
    'DATA_QUAL': 'float',     # Data quality score
    'AREA_SQKM': 'float',     # Footprint area (km²)
    'CENTROID_X': 'float',    # Centroid longitude
    'CENTROID_Y': 'float',    # Centroid latitude
    'CLUSTER_ID': 'int'       # Cluster assignment
}
```

## Algorithm Details

### 1. Peak Deconvolution Algorithm

```python
def gaussian_peak_fit(energies, counts, peak_center, initial_params=None):
    """
    Fits Gaussian peak model to spectral data
    
    Model: f(E) = A × exp(-0.5 × ((E - μ)/σ)²) + B₀ + B₁×E
    
    Parameters:
    - A: Peak amplitude
    - μ: Peak centroid (keV)
    - σ: Peak width (keV)
    - B₀: Constant background
    - B₁: Linear background slope
    """
    from scipy.optimize import curve_fit
    import numpy as np
    
    def gaussian_with_background(x, amplitude, centroid, sigma, bg_const, bg_slope):
        gaussian = amplitude * np.exp(-0.5 * ((x - centroid) / sigma) ** 2)
        background = bg_const + bg_slope * x
        return gaussian + background
    
    # Define fitting window (±3σ around peak)
    window_width = 0.15  # keV
    mask = (energies >= peak_center - window_width) & (energies <= peak_center + window_width)
    
    # Initial parameter estimates
    if initial_params is None:
        max_counts = np.max(counts[mask])
        initial_params = [
            max_counts,           # amplitude
            peak_center,          # centroid
            0.03,                # sigma (typical for CLASS)
            np.min(counts[mask]), # background constant
            0.0                  # background slope
        ]
    
    # Parameter bounds
    bounds = (
        [0, peak_center-0.05, 0.01, 0, -1],          # Lower bounds
        [max_counts*2, peak_center+0.05, 0.1, max_counts, 1]  # Upper bounds
    )
    
    try:
        popt, pcov = curve_fit(
            gaussian_with_background,
            energies[mask],
            counts[mask],
            p0=initial_params,
            bounds=bounds,
            maxfev=5000
        )
        
        # Calculate parameter uncertainties
        param_errors = np.sqrt(np.diag(pcov))
        
        # Calculate integrated peak area
        peak_area = popt[0] * popt[2] * np.sqrt(2 * np.pi)
        peak_area_error = peak_area * np.sqrt(
            (param_errors[0]/popt[0])**2 + (param_errors[2]/popt[2])**2
        )
        
        return {
            'peak_area': peak_area,
            'peak_area_error': peak_area_error,
            'centroid': popt[1],
            'centroid_error': param_errors[1],
            'width': popt[2],
            'width_error': param_errors[2],
            'fit_quality': np.sum((gaussian_with_background(energies[mask], *popt) - counts[mask])**2)
        }
        
    except RuntimeError as e:
        print(f"Peak fitting failed: {e}")
        return None
```

### 2. Advanced Background Modeling

```python
def polynomial_background_fit(energies, counts, exclude_regions, poly_order=3):
    """
    Fits polynomial background model excluding peak regions
    
    Background model: B(E) = Σ(aᵢ × Eⁱ) for i = 0 to poly_order
    """
    # Create mask excluding peak regions
    bg_mask = np.ones(len(energies), dtype=bool)
    for start, end in exclude_regions:
        region_mask = (energies >= start) & (energies <= end)
        bg_mask = bg_mask & ~region_mask
    
    # Fit polynomial to background regions
    bg_coeffs = np.polyfit(energies[bg_mask], counts[bg_mask], poly_order)
    
    # Calculate background over full energy range
    background = np.polyval(bg_coeffs, energies)
    
    # Calculate goodness of fit
    chi_squared = np.sum((np.polyval(bg_coeffs, energies[bg_mask]) - counts[bg_mask])**2 / counts[bg_mask])
    
    return background, bg_coeffs, chi_squared
```

### 3. Solar Activity Correlation Algorithm

```python
def calculate_solar_correction_factor(solar_class, energy_kev):
    """
    Calculates energy-dependent solar activity correction factors
    
    Based on empirical relationships between solar X-ray flux and
    observed XRF enhancement factors
    """
    # Base correction factors by solar class
    base_corrections = {
        'A': 1.00,  # No correction needed
        'B': 1.02,  # 2% enhancement
        'C': 1.05,  # 5% enhancement
        'M': 1.15,  # 15% enhancement
        'X': 1.30   # 30% enhancement (if usable)
    }
    
    # Energy-dependent correction (higher energies less affected)
    energy_factor = 1.0 + 0.1 * np.exp(-energy_kev / 2.0)
    
    total_correction = base_corrections.get(solar_class, 1.0) * energy_factor
    
    return total_correction
```

## Performance Optimization

### 1. Memory Management Strategies

```python
def optimize_memory_usage():
    """
    Memory optimization techniques for large dataset processing
    """
    # Use memory-mapped files for large datasets
    import numpy as np
    
    # Process data in chunks to avoid memory overflow
    chunk_size = 1000  # Process 1000 files at a time
    
    # Use efficient data types
    dtype_mapping = {
        'coordinates': np.float32,    # Sufficient precision for coordinates
        'ratios': np.float64,         # High precision for elemental ratios
        'counts': np.uint32,          # Integer counts
        'energies': np.float32        # Energy values
    }
    
    # Implement garbage collection for large processing loops
    import gc
    gc.collect()
```

### 2. Parallel Processing Implementation

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

### 3. Database Optimization for Large Datasets

```python
def optimize_database_queries():
    """
    SQL optimization strategies for large elemental datasets
    """
    import sqlite3
    
    # Create optimized database schema
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS elemental_data (
        id INTEGER PRIMARY KEY,
        filename TEXT NOT NULL,
        start_time DATETIME,
        end_time DATETIME,
        longitude REAL,
        latitude REAL,
        al_si_ratio REAL,
        mg_si_ratio REAL,
        fe_si_ratio REAL,
        ca_si_ratio REAL,
        solar_class TEXT,
        data_quality REAL
    );
    
    -- Create spatial index for geographic queries
    CREATE INDEX IF NOT EXISTS idx_spatial ON elemental_data(longitude, latitude);
    
    -- Create temporal index for time-based queries
    CREATE INDEX IF NOT EXISTS idx_temporal ON elemental_data(start_time, end_time);
    
    -- Create composition index for elemental ratio queries
    CREATE INDEX IF NOT EXISTS idx_composition ON elemental_data(al_si_ratio, mg_si_ratio);
    '''
```

## Troubleshooting Guide

### 1. Common FITS File Issues

#### Problem: "Header keyword missing" error
```python
def handle_missing_keywords(fits_file):
    """
    Robust handling of missing or corrupted FITS keywords
    """
    try:
        with fits.open(fits_file) as hdul:
            header = hdul[1].header
            
            # Check for required keywords with defaults
            required_keys = {
                'EXPOSURE': 8.0,      # Default exposure time
                'GAIN': 4.85,         # Default gain value
                'V0_LAT': None,       # No default for coordinates
                'V0_LON': None
            }
            
            for key, default in required_keys.items():
                if key not in header:
                    if default is not None:
                        print(f"Warning: Missing {key}, using default {default}")
                        header[key] = default
                    else:
                        raise ValueError(f"Critical keyword {key} missing from {fits_file}")
                        
    except Exception as e:
        print(f"Error processing {fits_file}: {e}")
        return None
```

#### Problem: Corrupted spectral data
```python
def validate_spectral_data(channels, counts):
    """
    Validates spectral data integrity and quality
    """
    issues = []
    
    # Check for negative counts
    if np.any(counts < 0):
        issues.append("Negative count values detected")
    
    # Check for unrealistic count values
    if np.max(counts) > 1e6:
        issues.append("Suspiciously high count values")
    
    # Check for dead channels
    zero_channels = np.sum(counts == 0)
    if zero_channels > len(counts) * 0.1:  # More than 10% zeros
        issues.append(f"High number of zero channels: {zero_channels}")
    
    # Check for energy calibration
    if len(channels) != len(counts):
        issues.append("Channel and count array length mismatch")
    
    return issues
```

### 2. Geospatial Processing Errors

#### Problem: Invalid polygon coordinates
```python
def fix_invalid_polygons(polygon):
    """
    Attempts to repair invalid polygon geometries
    """
    from shapely.validation import make_valid
    
    if not polygon.is_valid:
        # Try automatic repair
        fixed_polygon = make_valid(polygon)
        
        if fixed_polygon.is_valid:
            return fixed_polygon
        else:
            # Manual repair strategies
            # 1. Remove duplicate points
            coords = list(polygon.exterior.coords)
            unique_coords = []
            for coord in coords:
                if coord not in unique_coords:
                    unique_coords.append(coord)
            
            # 2. Ensure closure
            if unique_coords[0] != unique_coords[-1]:
                unique_coords.append(unique_coords[0])
            
            return Polygon(unique_coords)
```

### 3. Solar Activity Data Issues

#### Problem: Missing GOES data
```python
def handle_missing_goes_data(date_range):
    """
    Strategies for handling missing solar activity data
    """
    # 1. Use interpolation for short gaps
    # 2. Apply statistical background for longer gaps
    # 3. Flag data quality appropriately
    
    default_solar_class = 'B'  # Conservative estimate
    confidence_penalty = 0.5   # Reduce confidence by 50%
    
    return default_solar_class, confidence_penalty
```

## Advanced Configuration

### 1. Processing Parameters Configuration

```python
# config.yaml
processing_parameters:
  spectral_analysis:
    energy_calibration:
      polynomial_order: 3
      calibration_source: "Fe55"  # 5.9 keV Mn Kα
    background_subtraction:
      method: "linear_interpolation"  # or "polynomial_fit"
      background_windows:
        - [1.0, 1.3]  # Low energy window (keV)
        - [8.5, 10.0] # High energy window (keV)
    peak_integration:
      integration_method: "gaussian_fit"  # or "simple_sum"
      peak_windows:
        Mg: [1.20, 1.30]
        Al: [1.44, 1.54]
        Si: [1.69, 1.79]
        Ca: [3.64, 3.74]
        Fe: [6.35, 6.45]
  
  quality_control:
    minimum_snr: 3.0
    maximum_chi_squared: 5.0
    minimum_exposure_time: 5.0  # seconds
    
  geospatial:
    coordinate_system: "EPSG:4326"  # WGS84
    polygon_validation: true
    minimum_polygon_area: 0.01  # square degrees
    
  clustering:
    algorithm: "kmeans"
    n_clusters: 5
    random_state: 42
    standardize_features: true
```

### 2. Output Format Configuration

```python
# output_config.yaml
output_formats:
  csv:
    decimal_places: 6
    include_uncertainties: true
    include_quality_flags: true
    
  shapefile:
    coordinate_precision: 6
    include_metadata: true
    color_coding: "quantile"  # or "equal_interval"
    
  kml:
    include_popup_info: true
    icon_scaling: "data_quality"
    transparency: 0.7
```

## Quality Assurance

### 1. Automated Quality Control Checks

```python
def comprehensive_quality_assessment(data):
    """
    Implements comprehensive quality control checks
    """
    qc_results = {
        'spectral_quality': {},
        'spatial_quality': {},
        'temporal_quality': {},
        'overall_score': 0.0
    }
    
    # Spectral quality metrics
    qc_results['spectral_quality'] = {
        'snr_al': calculate_snr(data['al_peak'], data['al_background']),
        'snr_si': calculate_snr(data['si_peak'], data['si_background']),
        'peak_resolution': data['energy_resolution'],
        'calibration_accuracy': data['calibration_error']
    }
    
    # Spatial quality metrics
    qc_results['spatial_quality'] = {
        'coordinate_precision': data['coordinate_uncertainty'],
        'polygon_validity': data['polygon_valid'],
        'coverage_completeness': data['spatial_coverage']
    }
    
    # Temporal quality metrics
    qc_results['temporal_quality'] = {
        'solar_activity_impact': data['solar_correction_factor'],
        'measurement_stability': data['temporal_drift'],
        'exposure_adequacy': data['exposure_time'] >= 8.0
    }
    
    # Calculate overall quality score (0-100)
    weights = {'spectral': 0.5, 'spatial': 0.3, 'temporal': 0.2}
    qc_results['overall_score'] = sum(
        weights[category] * np.mean(list(metrics.values()))
        for category, metrics in qc_results.items()
        if category != 'overall_score'
    )
    
    return qc_results
```

## Known Limitations

### 1. Instrumental Limitations
- **Energy Resolution**: 180 eV FWHM limits separation of closely spaced peaks
- **Detection Efficiency**: Decreases significantly below 1.5 keV (affects Mg detection)
- **Spatial Resolution**: ~25 km footprint prevents fine-scale geological mapping
- **Temporal Resolution**: 8-second integration may miss rapid compositional variations

### 2. Analysis Limitations
- **Light Element Detection**: Limited sensitivity to elements lighter than Mg (Z < 12)
- **Oxide vs. Element Ambiguity**: Cannot distinguish between different oxidation states
- **Matrix Effects**: Composition-dependent absorption effects not fully corrected
- **Surface Roughness**: Topographic effects on signal intensity not accounted for

### 3. Validation Constraints
- **Ground Truth Coverage**: Apollo/Luna samples represent <1% of lunar surface
- **Sampling Bias**: Ground truth data biased toward specific geological units
- **Temporal Mismatch**: Decades between sample collection and orbital measurements
- **Scale Mismatch**: Point samples vs. 25 km footprint measurements

## Future Enhancements

### 1. Advanced Spectral Analysis
- **Machine Learning Peak Detection**: Neural network-based peak identification
- **Multi-element Deconvolution**: Simultaneous fitting of overlapping peaks
- **Matrix Effect Corrections**: Composition-dependent absorption modeling
- **Spectral Unmixing**: Separation of surface and subsurface contributions

### 2. Enhanced Geospatial Integration
- **Topographic Corrections**: Integration with lunar elevation models
- **Thermal Corrections**: Temperature-dependent spectral response modeling
- **Multi-temporal Analysis**: Change detection over mission duration
- **Cross-calibration**: Integration with other lunar compositional datasets

### 3. Advanced Validation Methods
- **Statistical Validation**: Bootstrap uncertainty estimation
- **Cross-validation**: Holdout testing with ground truth data
- **Sensitivity Analysis**: Parameter uncertainty propagation
- **Comparative Analysis**: Validation against other XRF missions
