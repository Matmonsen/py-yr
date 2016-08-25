# -*- coding: utf-8 -*-

from .temperature import Temperature
from .windspeed import WindSpeed
from .winddirection import WindDirection
from .symbol import Symbol


class WeatherStation(object):
    def __init__(self, weatherstation):
        try:
            self.stno = int(weatherstation['stno'])
        except KeyError:
            self.stno = None
        try:
            self.sttype = weatherstation['sttype']
        except KeyError:
            self.sttype = None
        try:
            self.name = weatherstation['name']
        except KeyError:
            self.name = None
        try:
            self.distance = int(weatherstation['distance'])
        except KeyError:
            self.distance = None
        try:
            self.lat = float(weatherstation['lat'])
        except KeyError:
            self.lat = None
        try:
            self.lon = float(weatherstation['lon'])
        except KeyError:
            self.lon = None
        try:
            self.source = weatherstation['source']
        except KeyError:
            self.source = None
        try:
            self.temperature = Temperature(weatherstation['temperature'])
        except KeyError:
            self.temperature = None
        try:
            self.windspeed = WindSpeed(weatherstation['windSpeed'])
        except KeyError:
            self.windspeed = None
        try:
            self.winddirection = WindDirection(weatherstation['windDirection'])
        except KeyError:
            self.winddirection = None
        try:
            self.symbol = Symbol(weatherstation['symbol'])
        except KeyError:
            self.symbol = None

    def __str__(self):
        if self.symbol is None:
            symbol = "\t\t"
        else:
            symbol = ''

        if self.windspeed is None:
            speed = "\t\t"
        else:
            speed = ''

        if self.winddirection is None:
            direction = "\t\t"
        else:
            direction = ''

        if self.temperature is None:
            temp = "\t\t"
        else:
            temp = ''

        return '\tStno: {0} ' \
               '\n\tStType: {1} ' \
               '\n\tName: {2} ' \
               '\n\tDistance: {3} ' \
               '\n\tLat: {4} ' \
               '\n\tLon: {5} ' \
               '\n\tSource: {6} ' \
               '\n\tTemperature: \n{7}{8} ' \
               '\n\tWindSpeed: \n{9}{10} ' \
               '\n\tWindDirection: \n{11}{12}' \
               '\n\tSymbol: \n{13}{14}'.format(self.stno, self.sttype, self.name, self.distance, self.lat, self.lon,
                                               self.source, temp, self.temperature, speed, self.windspeed, direction,
                                               self.winddirection, symbol, self.symbol)
