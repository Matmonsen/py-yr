#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import xml

import requests

import xmltodict

from py_yr.config.settings import LANGUAGE, FORECAST_TYPE_STANDARD
from py_yr.weatherdata.weatherdata import WeatherData


class Yr(object):
    """
        An Yr object for retrieving different types of weather data for a specific location
    """

    def __init__(self,
                 location,
                 language='en',
                 forecast_type=FORECAST_TYPE_STANDARD,
                 source_data=None,):

        self.source_data = source_data
        self.forecast_type = forecast_type
        self.language = language
        self.location = location

        if not self.location.endswith('/'):
            self.location += "/"

        try:
            self.url = "{0}{1}{2}".format(
                LANGUAGE[language]['url'],
                self.location,
                LANGUAGE[language]['forecast_type'][self.forecast_type])
        except KeyError:
            self.url = "http://yr.no/sted/rubbish"

    def get_as_object(self) -> WeatherData:
        """
        Renders the weather data as objects.
        Returns: Object representation of the weather data.

        """
        data = None
        raw_data = self.get_as__dict()

        if raw_data is not None:
            data = WeatherData(raw_data)
        return data

    def get_as_xml(self) -> str:
        """
        Renders the weather data as xml.
        Returns(str): Original data

        """
        return self.source_data

    def get_as__dict(self) -> dict:
        """
        Renders the weather data as a dict.
        Returns(dict): Dict representation of weather data

        """
        raw_data = self.get_as_xml()
        if raw_data is not None:
            try:
                try:
                    ordred_dict = xmltodict.parse(raw_data)
                    return json.loads(json.dumps(ordred_dict).replace('@', ''))['weatherdata']
                except (TypeError, ValueError) as err:
                    return None
            except ValueError:
                return None
        return None

    def download(self) -> None:
        """
            Downloads weather data from url
        """
        response = requests.get(self.url)
        if response.status_code is 200:
            try:
                # Some special cases like Norge/Oslo/Oslo is not a valid location,
                # but returns a normal html page, not a xml error like with a invalid location
                xmltodict.parse(response.text)
                self.source_data = response.text
            except xml.parsers.expat.ExpatError:
                self.source_data = None
        else:
            self.source_data = None
