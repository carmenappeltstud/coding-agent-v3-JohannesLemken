from api.weather_api import get_stations
from utils.data_processing import process_weather_data
from visualization.plots import display_weather_plot
import streamlit as st

def main():
    """
    Main application function that sets up the UI and handles user interactions.
    """
    st.title("US Weather Forecaster")
    st.write("## *Weather data provided by NOAA* 🌤️")
    st.write("##")
    st.write("### Select a weather station and your preferences:")

    graph = st.selectbox("Select Graph Type:", ('Bar Graph', 'Horizontal Bar Graph'))
    
    stations = get_stations()
    if not stations:
        st.error("Unable to fetch weather stations. Please check your API token.")
        return
    
    station_names = list(stations.keys())
    selected_station = st.selectbox("Select Weather Station:", station_names)
    selected_station_id = stations[selected_station]

    if st.button('Get Weather'):
        try:
            monthly_avg_temps = process_weather_data(selected_station_id)
            if monthly_avg_temps is not None:
                display_weather_plot(monthly_avg_temps, graph)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("If this error persists, please try selecting a different weather station.")

if __name__ == '__main__':
    main()
