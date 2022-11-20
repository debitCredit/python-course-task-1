from geopy.geocoders import Nominatim


def geolocate(query: str, user_agent) -> tuple[str, str]:
    """
    Makes a request to Nominatim API to search for lat/lon coordinates for a supplied place.

    For more information see documentation:
    https://nominatim.org/release-docs/latest/api/Search/

    :param query: textual description of location e.g. "Paris"
    :param user_agent: unique value to identify the requestor to the API.
    :return: tuple of latitude and longitude.
    """

    g = Nominatim(user_agent=user_agent)
    location = g.geocode(query)
    if location is None:
        print("Incorrect location, exiting.")
        exit(1)
    return location.latitude, location.longitude
