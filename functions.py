import requests
import os

API = os.getenv("WEATHER_KEY")


# CITY = "Nilópolis, BR"

# print(weather_temp)
# # print(weather_day)
# # print(get_weather)
# # print(get_weather.json())

def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}&units=metric"
    response = requests.get(url)
    content = response.json()

    date_temp_pair = []

    for row in content["list"]:
        date = row["dt_txt"]
        temperature = row["main"]["temp"]
        sky = row["weather"][0]["main"]
        date_temp_pair.append((date, str(temperature), sky))

    days_count = days * 8
    date_temp_pair = date_temp_pair[:days_count]

    return date_temp_pair


if __name__ == "__main__":
    print(get_data(place="London", days=1))
