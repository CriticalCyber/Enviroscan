# EnviroScan - Tracking Biodiversity Change Using Remote Sensing & Data Analytics

## Project Overview

EnviroScan is a comprehensive geospatial system designed to monitor biodiversity changes in Jim Corbett National Park using satellite imagery, machine learning, and data analytics. The system provides insights into vegetation health, land cover changes, and species distribution patterns over time.

### Case Study: Jim Corbett National Park

- **Location**: Uttarakhand, India
- **Coordinates**: 78.56°E - 79.15°E, 29.29°N - 29.63°N
- **Study Period**: 2000, 2010, 2020, 2025

## Project Structure

```
EnviroScan/
│
├── backend/
│   ├── main.py                 # Main entry point
│   ├── ndvi.py                 # NDVI calculation module
│   ├── land_classification.py   # Land cover classification
│   ├── change_detection.py     # Environmental change detection
│   ├── species_mapping.py      # Species data integration
│   ├── data_preprocessing.py   # Data preprocessing utilities
│   ├── utils.py                # Utility functions
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── index.html              # Main HTML interface
│   ├── style.css               # Styling
│   └── app.js                  # Frontend JavaScript
│
├── data/
│   ├── satellite/              # Raw satellite imagery
│   ├── species/                # Biodiversity data
│   └── processed/              # Processed data products
│
├── output/
│   ├── ndvi_maps/              # NDVI raster maps and visualizations
│   ├── classification_maps/    # Land cover classification maps
│   └── change_maps/            # Change detection maps
│
├── models/
│   └── random_forest_model.pkl # Trained ML model
│
├── gee/
│   ├── gee_ndvi.js             # GEE NDVI calculation script
│   └── gee_data_fetch.js       # GEE data acquisition script
│
├── dashboard/
│   └── streamlit_app.py        # Interactive Streamlit dashboard
│
├── logs/                       # System logs
│
└── README.md                   # This file
```

## Technology Stack

### Backend
- **Python 3.9+**
- **Streamlit** - Interactive dashboard
- **Flask** - API layer (optional)
- **Google Earth Engine API** - Satellite data processing
- **Rasterio** - Geospatial raster data processing
- **GeoPandas** - Geospatial vector data processing
- **Scikit-learn** - Machine learning algorithms
- **NumPy/Pandas** - Data manipulation
- **Matplotlib/Plotly** - Data visualization

### GIS & Remote Sensing
- **Google Earth Engine** - Cloud-based geospatial processing
- **Rasterio** - Local raster processing
- **GeoPandas** - Vector data handling

### Machine Learning
- **Scikit-learn**
- **Random Forest** - Land cover classification
- **K-Means** - Clustering analysis

### Visualization
- **Matplotlib** - Static visualizations
- **Plotly** - Interactive charts
- **Folium** - Interactive maps

### Frontend (Optional)
- **HTML5/CSS3/JavaScript** - Web interface

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd EnviroScan
   ```

2. Install Python dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. Set up Google Earth Engine authentication:
   ```bash
   earthengine authenticate
   ```

## How to Run the System

### Backend Processing
```bash
python backend/main.py
```

This command will:
1. Authenticate with Google Earth Engine
2. Download and preprocess satellite data
3. Calculate NDVI for all time periods
4. Perform land cover classification
5. Detect environmental changes
6. Integrate biodiversity species data
7. Generate all output products

### Interactive Dashboard
```bash
streamlit run dashboard/streamlit_app.py
```

The dashboard provides:
- NDVI Map Viewer
- Land Cover Classification Maps
- Change Detection Heatmaps
- Species Distribution Maps
- Year selector dropdown
- Layer toggle system

## Key Modules

### 1. Data Acquisition Module
- Fetches satellite imagery via Google Earth Engine
- Clips imagery to Jim Corbett region
- Saves GeoTIFF files locally

### 2. Image Preprocessing Module
- Cloud masking
- Atmospheric correction
- Band normalization
- Geo-referencing

### 3. NDVI Calculation Module
- Implements NDVI formula: `(NIR - Red) / (NIR + Red)`
- Generates NDVI Raster Maps
- Creates NDVI PNG Visualizations

### 4. Land Cover Classification Module
- Uses Random Forest to classify land cover types:
  - Forest
  - Water
  - Urban
  - Agriculture
- Extracts pixel features
- Trains and saves ML model
- Produces classified maps

### 5. Change Detection Module
- Compares NDVI values between time periods:
  - 2000 vs 2010
  - 2010 vs 2020
  - 2020 vs 2025
- Generates vegetation loss maps
- Creates vegetation gain maps
- Produces change heatmaps

### 6. Species Mapping Module
- Loads GBIF species occurrence data
- Integrates eBird observations
- Plots species locations on maps
- Overlays on environmental data
- Identifies biodiversity hotspots

### 7. Visualization & Dashboard Module
- Interactive Streamlit dashboard
- NDVI Map Viewer
- Land Cover Classification display
- Change Detection Heatmap
- Species Distribution Map
- Time series analysis tools

## Output Products

The system generates the following outputs:

1. **NDVI Maps** (GeoTIFF + PNG)
2. **Land Cover Classification Maps** (GeoTIFF + PNG)
3. **Change Detection Maps** (GeoTIFF + PNG)
   - Vegetation loss maps
   - Vegetation gain maps
   - Change heatmaps
4. **Species Distribution Overlays** (PNG)
5. **Trained ML Model** (.pkl file)
6. **System Logs** (text files)

## Data Sources

### Satellite Data
- **Sentinel-2** (2022-2025) via Google Earth Engine
- **Landsat 8** (2013-2021) via Google Earth Engine
- **Landsat 7** (2000-2012) via Google Earth Engine

### Biodiversity Data
- **GBIF Species Occurrence Data** (CSV format)
- **eBird Observations** (CSV format)

## Advanced Features (Optional Enhancements)

1. **Deforestation Alert System**
2. **Real-time Forest Fire Detection**
3. **PDF Report Generation**
4. **API Endpoints for Live Data**
5. **Dockerized Deployment**

## Development Guidelines

### Code Organization
- Modular design with separate modules for each functionality
- Clear separation between data processing and visualization
- Consistent logging throughout the system
- Error handling for all critical operations

### Best Practices
- Use virtual environments for dependency management
- Follow PEP 8 coding standards
- Document all functions and classes
- Write unit tests for critical components
- Version control all code changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Earth Engine for satellite data processing capabilities
- USGS for Landsat data
- ESA for Sentinel data
- GBIF and eBird for biodiversity data
- The open-source geospatial community