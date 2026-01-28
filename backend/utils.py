"""
Utility functions for the EnviroScan system.
"""
import os
import logging
from datetime import datetime

def setup_logging():
    """Setup logging configuration."""
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"enviroscan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def authenticate_gee():
    """
    Authenticate with Google Earth Engine.
    This function would handle the authentication process with GEE.
    """
    # Placeholder for GEE authentication
    # In practice, this would involve:
    # 1. Checking for existing credentials
    # 2. Authenticating with service account or user account
    # 3. Initializing the Earth Engine library
    try:
        import ee
        # ee.Authenticate()  # Uncomment for actual authentication
        ee.Initialize()
        logging.info("Successfully authenticated with Google Earth Engine")
    except ImportError:
        logging.warning("Earth Engine API not available. Running in simulation mode.")
    except Exception as e:
        logging.error(f"Failed to authenticate with Google Earth Engine: {str(e)}")
        raise

def get_study_area_bounds():
    """
    Get the bounding box coordinates for Jim Corbett National Park.
    
    Returns:
        list: [min_lon, min_lat, max_lon, max_lat]
    """
    return [78.56, 29.29, 79.15, 29.63]

def get_analysis_years():
    """
    Get the years to analyze.
    
    Returns:
        list: Years to analyze
    """
    return [2000, 2010, 2020, 2025]