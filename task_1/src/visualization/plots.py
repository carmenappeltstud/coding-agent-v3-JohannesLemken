import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import calendar

def display_weather_plot(data, plot_type='Bar Graph'):
    """
    Display weather data visualization using matplotlib.
    
    Args:
        data (pd.Series or pd.DataFrame): Weather data to plot
        plot_type (str): Type of plot ('Bar Graph' or 'Horizontal Bar Graph')
    """
    if data is None:
        return
    
    plt.figure(figsize=(12, 6))
    
    # Extract data
    if isinstance(data, pd.Series):
        temperatures = data.values
        months_raw = data.index.values
    else:
        temperatures = data["TAVG"].values
        months_raw = data["month"].values
    
    # Convert month numbers to month names
    months = [calendar.month_name[int(m.split('-')[0])] if '-' in str(m) 
             else calendar.month_name[int(m)] for m in months_raw]
    
    # Create plot based on type
    if plot_type == 'Bar Graph':
        plt.bar(range(len(months)), temperatures)
        plt.xlabel('Month')
        plt.ylabel('Temperature (°C)')
        plt.xticks(range(len(months)), months, rotation=45, ha='right')
    else:  # Horizontal Bar Graph
        plt.barh(range(len(months)), temperatures)
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Month')
        plt.yticks(range(len(months)), months)

    
    plt.title('Monthly Average Temperatures by Station')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    
    plt.title('Monthly Average Temperatures')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(plt)
    plt.close()