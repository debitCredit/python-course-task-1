import os
from weatherforecast import fetch_forecast, parse_forecast, filter_forecast
from geolocation import geolocate
from dotenv import load_dotenv

class WeatherApp:
    def __init__(self):
        # Secrets
        load_dotenv()
        self.USER_AGENT = os.getenv("USER_AGENT")
        self.SOURCE = os.getenv("SOURCE")

        self.start_screen(self)

    @staticmethod
    def process_forecast(forecast: dict):
        for k in forecast:
            print(f'Date: {k.strftime("%Y-%m-%d")} Temperature: {forecast[k]}°C')

    @staticmethod
    def start_screen(self):
        # Print console information and request location input from the user then display forecast information.
        print("")
        print("Weather App")
        print("Request forecast for: ")
        place = input("> ")
        print("Fetching latitude and longitude...")
        lat, lon = geolocate(place, self.USER_AGENT)
        print(f"{place}: latitude: {lat:.2f}, longitude: {lon:.2f}")
        print("Fetching weather forecast...")
        r = fetch_forecast(f"{lat:.2f}", f"{lon:.2f}", self.USER_AGENT, self.SOURCE)
        parsed_r = parse_forecast(r)
        filtered_dates = filter_forecast(parsed_r)
        self.process_forecast(filtered_dates)


if __name__ == '__main__':
    WeatherApp()
