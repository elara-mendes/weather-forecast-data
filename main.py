import streamlit as st
import plotly.express as px
from functions import get_data

st.title("Weather Forecast for the Next Days")
place_input = st.text_input(label="Place:")

forecast_day = st.select_slider(
    label="Forecast Days:",
    options=[1, 2, 3, 4, 5],
    help="Select the number of days to forecast"
)

select_box = st.selectbox(
    label="Select Data to View",
    options=[
        "Temperature",
        "Sky"
    ]
)

st.subheader(f"{select_box} for the next {forecast_day} days in {place_input}")

dates_values, temperatures_values = get_data(place_input, forecast_day, select_box)

if dates_values and temperatures_values:
    figure = px.line(x=dates_values, y=temperatures_values, labels=dict(x="Date", y="Temperature (C)"))
    st.plotly_chart(figure)