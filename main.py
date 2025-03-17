import streamlit as st

st.title("Weather Forecast for the Next Days")
text_input = st.text_input(label="Place:")

forecast_day = st.select_slider(
    label="Forecast Days:",
    options=[
        1,
        2,
        3,
        4,
        5
    ],
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