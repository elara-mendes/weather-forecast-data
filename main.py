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

if place_input:
    try:
        all_data = get_data(place_input, forecast_day)
        if select_box == "Temperature":
            dates_values = [date[0] for date in all_data]
            temperatures_values = [temp[1] for temp in all_data]
            figure = px.line(x=dates_values, y=temperatures_values, labels=dict(x="Date", y="Temperature (C)"))
            st.plotly_chart(figure)

        if select_box == "Sky":
            images = {
               "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png",
                "Clear": "images/clear.png",
            }
            sky_condition = [temp[2] for temp in all_data]
            images_paths = [images[condition] for condition in sky_condition]
            # print(sky_condition)
            cols = st.columns(3)
            for i, (image_path, caption) in enumerate(zip(images_paths, ([date[0] for date in all_data]))):
                    image = image_path
                    cols[i % 3].image(image, caption=caption, width=115)
    except KeyError:
        st.error("Please write a valid option")