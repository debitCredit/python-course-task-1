import requests
from datetime import datetime, timezone


def fetch_forecast(lat: str, lon: str, user_agent: str, source: str) -> str:
    """
    Requests forcast information for a specified location from met.no API service.

    https://api.met.no/weatherapi/locationforecast/2.0/documentation

    :param lat: string representation of latitude with 2 decimal points.
    :param lon: string representation of longitude with 2 decimal points.
    :param user_agent: unique value to identify the requestor to the API.
    :param source: unique value to identify the requestor to the API.
    :return: API return in json format. See met.no documentation for details.
    """

    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    headers = {
        "User-Agent": user_agent,
        "From": source
    }
    r = requests.get(url, headers=headers)

    # Error handling if response wasn't 200.
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    return r.json()


def parse_forecast(r: dict) -> dict:
    """
    Parses the json API response into a dictionary of date: temperature forecast.

    :param r: response from the MET.NO API call in json format.
    :return: dictionary of date in datetime format and corresponding air temperature forecast in celsius for this date.
    """
    """Parse the request to create a kv store of time:temperature."""
    result = {}
    for d in r["properties"]["timeseries"]:
        result[datetime.fromisoformat(d["time"])] = (d["data"]["instant"]["details"]["air_temperature"])
    return result


def filter_forecast(d: dict) -> dict:
    """
    Filters the dictionary of date: temperature forecast to return the 4 days of forecast.

    :param d: dictionary of date(datetime): temperature
    :return: Returns 4 forecasts: most recent +24h, +48h, +72h. Due to changes in forecast granularity  the subseqent
    forecasts are from 12:00 UTC.
    """

    dates = {}
    most_recent = next(iter(d))
    dates[most_recent.date()] = d[most_recent]
    for i in range(1, 4):
        a = datetime(most_recent.year, most_recent.month, most_recent.day + i, hour=12, tzinfo=timezone.utc)
        dates[a.date()] = d[a]
    return dates
