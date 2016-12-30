# -*- coding: utf-8 -*-

"""
    This module contains the application settings

    Attributes:
        BASE_URL (str): Base url for the forecast service
        FORECAST_TYPE_STANDARD (str): Forecast type for standard forecast
        FORECAST_TYPE_HOURLY (str): Forecast type for hourly forecast
        LANGUAGE (dict): Dict containing language variables.
            English, Norwegian-nynorsk and Norwegian-Bokmål is supported.
"""

BASE_URL = 'http://www.yr.no/'

FORECAST_TYPE_STANDARD = "standard"
FORECAST_TYPE_HOURLY = "hourly"


LANGUAGE = {
    'en': {
        'url': BASE_URL + 'place/',
        'forecast_type': {
            FORECAST_TYPE_STANDARD: 'forecast.xml',
            FORECAST_TYPE_HOURLY: 'forecast_hour_by_hour.xml'
        }
    },
    'nb': {
        'url': BASE_URL + 'sted/',
        'forecast_type': {
            FORECAST_TYPE_STANDARD: 'varsel.xml',
            FORECAST_TYPE_HOURLY: 'varsel_time_for_time.xml'
        }
    },
    'nn': {
        'url': BASE_URL + 'stad/',
        'forecast_type': {
            FORECAST_TYPE_STANDARD: 'varsel.xml',
            FORECAST_TYPE_HOURLY: 'varsel_time_for_time.xml'
        }
    }
}
