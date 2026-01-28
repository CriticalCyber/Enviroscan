"""
Main entry point for the EnviroScan biodiversity monitoring system.
"""
import os
import sys
import logging
from datetime import datetime

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import modules
from data_preprocessing import preprocess_satellite_data
from ndvi import calculate_ndvi
from land_classification import classify_land_cover
from change_detection import detect_changes
from species_mapping import map_species_data
from utils import setup_logging, authenticate_gee

def main():
    """Main function to run the EnviroScan system."""
    # Setup logging
    setup_logging()
    logging.info("Starting EnviroScan biodiversity monitoring system")
    
    try:
        # Authenticate with Google Earth Engine
        logging.info("Authenticating with Google Earth Engine")
        authenticate_gee()
        
        # Download and preprocess satellite data
        logging.info("Downloading and preprocessing satellite data")
        preprocess_satellite_data()
        
        # Calculate NDVI
        logging.info("Calculating NDVI")
        calculate_ndvi()
        
        # Perform land cover classification
        logging.info("Performing land cover classification")
        classify_land_cover()
        
        # Detect changes over time
        logging.info("Detecting environmental changes")
        detect_changes()
        
        # Integrate biodiversity data
        logging.info("Mapping species data")
        map_species_data()
        
        logging.info("EnviroScan system completed successfully")
        
    except Exception as e:
        logging.error(f"Error in EnviroScan system: {str(e)}")
        raise

if __name__ == "__main__":
    main()