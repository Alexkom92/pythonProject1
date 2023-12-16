import requests
from typing import Dict, Union, List

api_key = "d22e25e32821d5f57097627163a163e6"


class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city) -> Dict[str, Union[str, int, float]]:
        try:
            params = {"q": city, "appid": self.api_key, "units": "metric"}
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            data = response.json()
            weather = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }

            return weather

        except requests.exceptions.RequestException as e:
            return {}

    def show_weather(self, city) -> None:
        weather = self.get_weather(city)

        if weather:
            print(f"Температура в {city}: {weather['temperature']}°C, "
                  f"влажность: {weather['humidity']}%, "
                  f"скорость ветра: {weather['wind_speed']} м/с")
        else:
            print(f"Не удалось получить данные о погоде в {city}")


class WeatherForecast(WeatherAPI):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_forecast(self, city: str) -> List[Dict[str, Union[str, int, float]]]:
        forecast = []

        try:
            params = {"q": city, "appid": self.api_key, "units": "metric"}
            response = requests.get(self.forecast_url, params=params)
            response.raise_for_status()

            data = response.json()

            for weather_data in data['list'][:5]:
                forecast.append({
                    "temperature": weather_data["main"]["temp"],
                    "humidity": weather_data["main"]["humidity"],
                    "wind_speed": weather_data["wind"]["speed"],
                    "date": weather_data["dt_txt"],
                })

            return forecast

        except requests.exceptions.RequestException as e:
            return []


if __name__ == "__main__":
    api = WeatherAPI(api_key)
    api.show_weather("Kharkiv")

    forecast = WeatherForecast(api_key)
    for day in forecast.get_forecast("Kharkiv"):
        print(day)
