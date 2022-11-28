# Weather App

## About The Project

Weather App is a console program that provides temperature forecast for a given place.
The app provides four forecast points: most immediate (+/- 1h), at 12:00 the following day and so on.


## Requirements

1)  Python 3.11 or later, install dependencies:
```
poetry install
```

2) Set up os environment variables to identify requestor to API services. For example:
```
USER_AGENT=ExampleApp/0.0.0
SOURCE=email@example.com
```
3) Read and agree to the API Usage Policies:

   a) https://operations.osmfoundation.org/policies/nominatim/

   b) https://api.met.no/doc/TermsOfService





## Usage

1) Launch the weatherapp.py using Python
2) Enter the name of the location.

```
PS C:\dev\weather_app> py .\weatherapp.py

Weather App
Request forecast for: 
> Cairo
Fetching latitude and longitude...
Cairo: latitude: 30.04, longitude: 31.24
Fetching weather forecast...
Date: 2022-11-19 Temperature: 22.5°C
Date: 2022-11-20 Temperature: 27.7°C
Date: 2022-11-21 Temperature: 27.0°C
Date: 2022-11-22 Temperature: 25.1°C
```

## Things to consider

1) Python 3.11  is required to parse datetime returned by met.no API. See the below for relevant discussion:
https://github.com/python/cpython/issues/80010

2) Calculating local time from geo coordinates isn't straight forward, see: https://docs.api.met.no/doc/locationforecast/FAQ
As a result all forecast data is normalized to provide a forecast as at 12:00 UTC.
3) This program was tested on Windows 10 only.


## Roadmap

- [ ] Introduce tests
- [ ] Local data caching to avoid downloading the same data and reuse the data if not changed. [See](https://docs.api.met.no/doc/TermsOfService)


## Acknowledgments

This program uses two public API services:

**The Norwegian Meteorological Institute**

[https://docs.api.met.no/doc/](https://nominatim.org)

**Nominatim.org**

[https://nominatim.org](https://nominatim.org)
