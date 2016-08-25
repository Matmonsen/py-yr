# -*- coding: utf-8 -*-

"""
    This module contains the application settings

    Attributes:
        BASE_URL (str): Base url for the forecast service
        LANGUAGE (dict): Dict containing language variables.
            English, Norwegian-nynorsk and Norwegian-Bokmål is supported.
"""

BASE_URL = 'http://www.yr.no/'


LANGUAGE = {
    'en': {
        'url': BASE_URL + 'place/',
        'forecast_type': {
            'standard': '/forecast.xml',
            'hourly': '/forecast_hour_by_hour.xml'
        }
    },
    'nb': {
        'url': BASE_URL + 'sted/',
        'forecast_type': {
            'standard': '/varsel.xml',
            'hourly': '/varsel_time_for_time.xml'
        }
    },
    'nn': {
        'url': BASE_URL + 'stad/',
        'forecast_type': {
            'standard': '/varsel.xml',
            'hourly': '/varsel_time_for_time.xml'
        }
    }
}
