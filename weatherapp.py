import os
from sys import stderr
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
        """Print out the forecast to the console in user friendly format.

        Args:
            forecast (dict): datetime: temperature
        """
        for k in forecast:
            print(f'Date: {k.strftime("%Y-%m-%d")} Temperature: {forecast[k]}°C', file=stderr)


    def request_input(self) -> str:
        """Request user input, if input is None or empty request the input again.

        Returns:
            str: Console input from user.
        """
        prompt = "> "
        response = input(prompt)
        if response is None or "".__eq__(response):
            self.request_input()
        else:
            return response
            

    @staticmethod
    def start_screen(self):
        # Print console information and request location input from the user then display forecast information.
        print("", file=stderr)
        print("Weather App", file=stderr)
        print("Request forecast for: ", file=stderr)
        place = self.request_input()
        print("Fetching latitude and longitude...", file=stderr)
        lat, lon = geolocate(place, self.USER_AGENT)
        print(f"{place}: latitude: {lat:.2f}, longitude: {lon:.2f}", file=stderr)
        print("Fetching weather forecast...", file=stderr)
        r = fetch_forecast(f"{lat:.2f}", f"{lon:.2f}", self.USER_AGENT, self.SOURCE)
        parsed_r = parse_forecast(r)
        filtered_dates = filter_forecast(parsed_r)
        self.process_forecast(filtered_dates)


if __name__ == '__main__':
    WeatherApp()
