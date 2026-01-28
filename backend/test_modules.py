"""
Test script to verify that core modules work without GEE authentication.
"""
import os
import sys
import logging

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import modules
from data_preprocessing import preprocess_satellite_data
from ndvi import calculate_ndvi
from land_classification import classify_land_cover
from change_detection import detect_changes
from species_mapping import map_species_data
from utils import setup_logging

def test_modules():
    """Test all modules without GEE authentication."""
    # Setup logging
    setup_logging()
    logging.info("Testing EnviroScan modules without GEE authentication")
    
    try:
        # Test data preprocessing (without actual GEE connection)
        logging.info("Testing data preprocessing module")
        preprocess_satellite_data()
        
        # Test NDVI calculation
        logging.info("Testing NDVI calculation module")
        calculate_ndvi()
        
        # Test land cover classification
        logging.info("Testing land cover classification module")
        classify_land_cover()
        
        # Test change detection
        logging.info("Testing change detection module")
        detect_changes()
        
        # Test species mapping
        logging.info("Testing species mapping module")
        map_species_data()
        
        logging.info("All modules tested successfully!")
        
    except Exception as e:
        logging.error(f"Error testing modules: {str(e)}")
        raise

if __name__ == "__main__":
    test_modules()