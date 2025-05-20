import requests
from datetime import datetime, timedelta
from config.settings import API_TOKEN, STATIONS, BASE_URL
import streamlit as st
import pandas as pd

def get_stations():
    """
    Get the predefined list of weather stations.
    Returns:
        dict: Dictionary of station names and their IDs
    """
    return STATIONS

def get_weather_data(station_id, start_date=None, end_date=None):
    """
    Fetch weather data for a specific station from the NOAA API.
    
    Args:
        station_id (str): The ID of the weather station
        start_date (str, optional): Start date in YYYY-MM-DD format
        end_date (str, optional): End date in YYYY-MM-DD format
    
    Returns:
        pd.DataFrame: Weather data for the specified station and time period
    """
    if not start_date:
        start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    if not end_date:
        end_date = datetime.now().strftime("%Y-%m-%d")

    try:
        params = {
            "dataset": "daily-summaries",
            "stations": station_id,
            "startDate": start_date,
            "endDate": end_date,
            "dataTypes": "TMAX,TMIN",
            "units": "metric",
            "format": "json",
            "includeAttributes": "false",
            "token": API_TOKEN
        }
        response = requests.get(BASE_URL, params=params)
        return pd.DataFrame(response.json())
    
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {str(e)}")
        return []