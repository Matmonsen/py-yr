#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from urllib import request
from urllib.error import HTTPError

import xmltodict

from py_yr.config.settings import LANGUAGE
from py_yr.weatherdata.weatherdata import WeatherData


class Yr(object):
    """
        An Yr object for retrieving different types of weather data for a specific location
    """

    def __init__(self,
                 location,
                 forecast_type='standard',
                 language='en',
                 source_data=None,):

        self.source_data = source_data
        self.forecast_type = forecast_type
        self.language = language
        self.location = location
        self.xml_file = LANGUAGE[language]['forecast_type'][self.forecast_type]
        self.url = LANGUAGE[language]['url'] + self.location + self.xml_file

    def get_as_object(self):
        """
        Renders the weather data as objects.
        Returns: Object representation of the weather data.

        """
        data = None
        raw_data = self.get_as_json()

        if raw_data is not None:
            data = WeatherData(raw_data)
        return data

    def get_as_xml(self) -> str:
        """
        Renders the weather data as xml.
        Returns(str): Original data

        """
        return self.source_data

    def get_as_ordered_dict(self) -> dict:
        """
        Renders the weather data as an ordered dict.
        Returns(dict): Dict representation of weather data

        """
        raw_data = self.get_as_xml()
        if raw_data is not None:
            try:
                return xmltodict.parse(raw_data)
            except ValueError:
                return None

    def get_as_json(self) -> str:
        """
            Renders the weather data as json.
        Returns(str): json represented string of weather data, or none if no data exists.

        """
        raw_data = self.get_as_ordered_dict()
        if raw_data is not None:
            try:
                return json.loads(json.dumps(raw_data).replace('@', ''))['weatherdata']
            except (TypeError, ValueError) as err:
                return None

    def is_valid_url(self):
        """
        Check weather the location given is valid or not.
        Returns: None of the location is not valid. Weather data for the location otherwise.

        """
        try:
            response = request.urlopen(self.url)
            if response.status is 200:
                return response
            else:
                return None
        except HTTPError:
            return None

    def download(self) -> None:
        """
            Downloads weather data from url

        """
        response = self.is_valid_url()
        if response is not None:
            data = response.read()
            self.source_data = data.decode('utf-8')
        else:
            self.source_data = None
