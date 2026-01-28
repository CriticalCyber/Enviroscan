"""
Streamlit dashboard for EnviroScan system.
Displays NDVI maps, land cover classification, change detection heatmaps, and species distribution.
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Set page configuration
st.set_page_config(
    page_title="EnviroScan - Biodiversity Monitoring",
    page_icon="🌍",
    layout="wide"
)

def main():
    """Main function for the Streamlit dashboard."""
    # App title and description
    st.title("🌍 EnviroScan - Biodiversity Change Monitoring")
    st.markdown("""
    This dashboard displays biodiversity changes in Jim Corbett National Park 
    using satellite imagery, machine learning, and data analytics.
    """)
    
    # Sidebar for controls
    st.sidebar.header("Controls")
    
    # Year selector
    years = [2000, 2010, 2020, 2025]
    selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
    
    # Layer selection
    st.sidebar.subheader("Map Layers")
    show_ndvi = st.sidebar.checkbox("Show NDVI Map", True)
    show_land_cover = st.sidebar.checkbox("Show Land Cover Classification", True)
    show_species = st.sidebar.checkbox("Show Species Distribution", True)
    
    # Comparison period for change detection
    st.sidebar.subheader("Change Detection")
    comparison_periods = [
        "2000 vs 2010",
        "2010 vs 2020",
        "2020 vs 2025"
    ]
    selected_period = st.sidebar.selectbox("Comparison Period", comparison_periods)
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Overview", 
        "🌿 Vegetation Analysis", 
        "🗺️ Land Cover", 
        "🐾 Species Distribution"
    ])
    
    with tab1:
        display_overview(selected_year)
    
    with tab2:
        display_vegetation_analysis(selected_year)
    
    with tab3:
        display_land_cover(selected_year)
    
    with tab4:
        display_species_distribution()

def display_overview(year):
    """Display overview information."""
    st.header("Overview")
    
    # Study area information
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Study Area: Jim Corbett National Park")
        st.markdown("""
        - **Location**: Uttarakhand, India
        - **Coordinates**: 78.56°E - 79.15°E, 29.29°N - 29.63°N
        - **Area**: ~520 km²
        """)
    
    with col2:
        st.subheader("Analysis Summary")
        st.markdown(f"""
        - **Year**: {year}
        - **Data Source**: Sentinel-2 Satellite Imagery
        - **Vegetation Index**: NDVI
        - **Classification**: Forest/Water/Urban/Agriculture
        """)
    
    # Map visualization
    st.subheader("Study Area Map")
    
    # Create a simple Folium map centered on Jim Corbett
    corbett_coords = [29.45, 78.85]  # Approximate center
    m = folium.Map(location=corbett_coords, zoom_start=10)
    
    # Add a marker for Jim Corbett
    folium.Marker(
        corbett_coords,
        popup="Jim Corbett National Park",
        tooltip="Jim Corbett National Park"
    ).add_to(m)
    
    # Add a rectangle for the study area bounds
    bounds = [[29.29, 78.56], [29.63, 79.15]]
    folium.Rectangle(
        bounds=bounds,
        color="blue",
        weight=2,
        fill=False,
        tooltip="Study Area Bounds"
    ).add_to(m)
    
    st_folium(m, width=700, height=500)

def display_vegetation_analysis(year):
    """Display vegetation analysis including NDVI maps."""
    st.header("Vegetation Analysis")
    
    # NDVI information
    st.subheader(f"NDVI Map - {year}")
    st.markdown("""
    The Normalized Difference Vegetation Index (NDVI) is used to analyze vegetation health.
    NDVI values range from -1 to 1:
    - Values close to 1 indicate healthy vegetation
    - Values close to 0 indicate bare soil or sparse vegetation
    - Negative values indicate water bodies
    """)
    
    # Simulate NDVI visualization
    # In practice, this would load and display actual NDVI GeoTIFF files
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create simulated NDVI data
    ndvi_data = np.random.uniform(-1, 1, (50, 50))
    im = ax.imshow(ndvi_data, cmap='RdYlGn', vmin=-1, vmax=1)
    ax.set_title(f'Simulated NDVI Map - {year}')
    plt.colorbar(im, ax=ax, label='NDVI Value')
    
    st.pyplot(fig)
    
    # Statistics
    st.subheader("NDVI Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Mean NDVI", f"{np.mean(ndvi_data):.3f}")
    col2.metric("Min NDVI", f"{np.min(ndvi_data):.3f}")
    col3.metric("Max NDVI", f"{np.max(ndvi_data):.3f}")
    col4.metric("Std Dev", f"{np.std(ndvi_data):.3f}")

def display_land_cover(year):
    """Display land cover classification."""
    st.header("Land Cover Classification")
    
    st.subheader(f"Land Cover Map - {year}")
    st.markdown("""
    Land cover classification using Random Forest algorithm:
    - **Forest** (Green)
    - **Water** (Blue)
    - **Urban** (Gray)
    - **Agriculture** (Yellow)
    """)
    
    # Simulate land cover visualization
    # In practice, this would load and display actual classification GeoTIFF files
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create simulated land cover data
    land_cover_data = np.random.choice([0, 1, 2, 3], size=(50, 50))
    colors = ['green', 'blue', 'gray', 'yellow']
    im = ax.imshow(land_cover_data, cmap=mcolors.ListedColormap(colors))
    ax.set_title(f'Simulated Land Cover Classification - {year}')
    
    # Create custom legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', label='Forest'),
        Patch(facecolor='blue', label='Water'),
        Patch(facecolor='gray', label='Urban'),
        Patch(facecolor='yellow', label='Agriculture')
    ]
    ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')
    
    st.pyplot(fig)
    
    # Land cover statistics
    st.subheader("Land Cover Statistics")
    unique, counts = np.unique(land_cover_data, return_counts=True)
    labels = ['Forest', 'Water', 'Urban', 'Agriculture']
    
    # Create a DataFrame for the statistics
    stats_df = pd.DataFrame({
        'Land Cover Type': [labels[i] for i in unique],
        'Area (pixels)': counts,
        'Percentage': [count/land_cover_data.size*100 for count in counts]
    })
    
    st.table(stats_df)

def display_species_distribution():
    """Display species distribution data."""
    st.header("Species Distribution")
    
    st.subheader("Biodiversity Data Sources")
    st.markdown("""
    - **GBIF** (Global Biodiversity Information Facility)
    - **eBird** (Bird observations)
    """)
    
    # Load simulated species data
    # In practice, this would load actual CSV files
    gbif_data = {
        'species': ['Tiger', 'Leopard', 'Elephant', 'Deer', 'Bird'],
        'latitude': [29.4, 29.35, 29.5, 29.45, 29.38],
        'longitude': [78.8, 78.9, 79.0, 78.85, 78.95],
        'date': ['2020-01-15', '2020-02-20', '2020-03-10', '2020-04-05', '2020-05-12']
    }
    
    gbif_df = pd.DataFrame(gbif_data)
    
    # Display species table
    st.subheader("Species Observations")
    st.dataframe(gbif_df)
    
    # Create species map
    st.subheader("Species Distribution Map")
    
    # Create a Folium map
    corbett_coords = [29.45, 78.85]
    m = folium.Map(location=corbett_coords, zoom_start=10)
    
    # Add markers for each species observation
    for idx, row in gbif_df.iterrows():
        folium.Marker(
            [row['latitude'], row['longitude']],
            popup=f"{row['species']}<br>Date: {row['date']}",
            tooltip=row['species']
        ).add_to(m)
    
    st_folium(m, width=700, height=500)
    
    # Biodiversity hotspot analysis
    st.subheader("Biodiversity Hotspots")
    st.markdown("""
    Areas with high species concentration have been identified as biodiversity hotspots.
    Conservation efforts should focus on these areas.
    """)

if __name__ == "__main__":
    main()