"""
Change detection module for EnviroScan system.
Detects environmental changes over time by comparing NDVI values.
"""
import os
import logging
import numpy as np
from utils import get_analysis_years

def detect_changes():
    """
    Detect environmental changes by comparing NDVI values over time.
    
    Compares NDVI for:
    1. 2000 vs 2010
    2. 2010 vs 2020
    3. 2020 vs 2025
    
    Outputs:
    1. Vegetation loss map
    2. Vegetation gain map
    3. Change heatmap
    """
    logging.info("Starting change detection")
    
    # Define comparison periods
    comparisons = [
        (2000, 2010),
        (2010, 2020),
        (2020, 2025)
    ]
    
    try:
        # Create output directory
        change_maps_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
            'output', 'change_maps'
        )
        os.makedirs(change_maps_dir, exist_ok=True)
        
        for period in comparisons:
            year1, year2 = period
            logging.info(f"Detecting changes between {year1} and {year2}")
            
            # In practice, this would:
            # 1. Load NDVI maps for both years
            # 2. Calculate difference (year2 - year1)
            # 3. Identify significant changes
            # 4. Generate vegetation loss/gain maps
            # 5. Create change heatmaps
            # 6. Save outputs as GeoTIFF and PNG
            
            # Simulate change detection
            simulate_change_detection(year1, year2, change_maps_dir)
            
        logging.info("Change detection completed")
        
    except Exception as e:
        logging.error(f"Error in change detection: {str(e)}")
        raise

def simulate_change_detection(year1, year2, output_dir):
    """
    Simulate change detection between two years.
    
    Args:
        year1 (int): First year
        year2 (int): Second year
        output_dir (str): Directory to save outputs
    """
    # Create simulated change arrays
    # Difference in NDVI values (year2 - year1)
    diff_array = np.random.uniform(-1, 1, (100, 100))
    
    # Vegetation loss map (negative changes)
    loss_array = np.where(diff_array < 0, np.abs(diff_array), 0)
    
    # Vegetation gain map (positive changes)
    gain_array = np.where(diff_array > 0, diff_array, 0)
    
    # Save vegetation loss map (simulated)
    loss_path = os.path.join(output_dir, f"loss_{year1}_{year2}.tif")
    with open(loss_path, 'w') as f:
        f.write(f"Simulated vegetation loss map for {year1}-{year2}")
    
    # Save vegetation gain map (simulated)
    gain_path = os.path.join(output_dir, f"gain_{year1}_{year2}.tif")
    with open(gain_path, 'w') as f:
        f.write(f"Simulated vegetation gain map for {year1}-{year2}")
    
    # Save change heatmap (simulated)
    heatmap_path = os.path.join(output_dir, f"change_heatmap_{year1}_{year2}.tif")
    with open(heatmap_path, 'w') as f:
        f.write(f"Simulated change heatmap for {year1}-{year2}")
    
    # Save PNG visualizations (simulated)
    loss_png = os.path.join(output_dir, f"loss_{year1}_{year2}.png")
    with open(loss_png, 'w') as f:
        f.write(f"Simulated vegetation loss PNG for {year1}-{year2}")
    
    gain_png = os.path.join(output_dir, f"gain_{year1}_{year2}.png")
    with open(gain_png, 'w') as f:
        f.write(f"Simulated vegetation gain PNG for {year1}-{year2}")
    
    heatmap_png = os.path.join(output_dir, f"change_heatmap_{year1}_{year2}.png")
    with open(heatmap_png, 'w') as f:
        f.write(f"Simulated change heatmap PNG for {year1}-{year2}")
    
    logging.info(f"Saved change detection outputs for {year1}-{year2} to {output_dir}")

if __name__ == "__main__":
    detect_changes()