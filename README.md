# weather-forecast-data ☔

Um data web app que mostra a visualização do clima para os próximos 5 dias de qualquer cidade.

Onde foi utilizado Streamlit para a interface e requests para acessar as informações da API.

Para utilizar você pode conseguir sua chave da API em [OpenWeatherMap](https://openweathermap.org/api). Busque pelo card escrito: _5 Day / 3 Hour Forecast_. E coloque no arquivo `functions.py`:

```python
API = "SUA CHAVE API"
```

Por fim rodar utilizando streamlit run `main.py`