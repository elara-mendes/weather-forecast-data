Aqui está a versão em inglês do seu README:  

---

# weather-forecast-data ☔  

A data web app that displays a 5-day weather forecast visualization for any city.  

Streamlit was used for the interface, and requests were used to access API information.  

To use it, you can get your API key from [OpenWeatherMap](https://openweathermap.org/api). Look for the card labeled: _5 Day / 3 Hour Forecast_. Then, add it to the `functions.py` file:  

```python
API = "YOUR_API_KEY"
```  

Finally, run the app using:  
```bash
streamlit run main.py
```