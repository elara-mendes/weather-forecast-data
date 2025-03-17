import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
text_input = st.text_input(label="Place:")

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

st.subheader(f"{select_box} for the next {forecast_day} days in {text_input}")

def get_data(i):
    dates = ["2025-15-03", "2025-16-03", "2025-17-03"]
    temperatures = [10, 20, 30]
    temperatures = [i * forecast_day for i in temperatures]
    return dates, temperatures

dates_values, temperatures_values = get_data(forecast_day)

figure = px.line(x=dates_values, y=temperatures_values, labels=dict(x="Date", y="Temperature (C)"))
st.plotly_chart(figure)