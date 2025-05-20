import pandas as pd
from api.weather_api import get_weather_data

def process_weather_data(station_id):
    """
    Process weather data from the API into monthly average temperatures.
    
    Args:
        station_id (str): ID of the weather station
    
    Returns:
        pd.Series: Monthly average temperatures or None if processing fails
    """
    if not station_id:
        st.error("Please select a station")
        return None

    df = get_weather_data(station_id)
    
    # Data preprocessing
    df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m', errors='coerce')
    df['month'] = df['DATE'].dt.month
    df["TMAX"] = pd.to_numeric(df["TMAX"], errors='coerce')
    df["TMIN"] = pd.to_numeric(df["TMIN"], errors='coerce')
    df["TAVG"] = (df["TMAX"] + df["TMIN"]) / 2

    # Calculate monthly averages
    monthly_avg = df.groupby('month')["TAVG"].mean().round(1)
    
    return monthly_avg