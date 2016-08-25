# -*- coding: utf-8 -*-

from weather_report.py_yr import utilities
from .symbol import Symbol
from .precipitation import Precipitation
from .winddirection import WindDirection
from .windspeed import WindSpeed
from .temperature import Temperature
from .pressure import Pressure


class Time(object):
    def __init__(self, time):
        self.from_ = utilities.parse_iso8601(time['from'])
        self.to = utilities.parse_iso8601(time['to'])
        try:
            self.period = int(time['period'])
        except KeyError:
            self.period = None
        self.symbol = Symbol(time['symbol'])
        self.precipitation = Precipitation(time['precipitation'])
        self.windDirection = WindDirection(time['windDirection'])
        self.windSpeed = WindSpeed(time['windSpeed'])
        self.temperature = Temperature(time['temperature'])
        self.pressure = Pressure(time['pressure'])

    def __str__(self):
        return '\t\t\tFrom: {0} ' \
               '\n\t\t\tTo: {1} ' \
               '\n\t\t\tPeriod: {2} ' \
               '\n\t\t\tSymbol: \n{3} ' \
               '\n\t\t\tPrecipitation: \n{4} ' \
               '\n\t\t\tWindDirection: \n{5} ' \
               '\n\t\t\tWindSpeed: \n{6} ' \
               '\n\t\t\tTemperature: \n{7} ' \
               '\n\t\t\tPressure: \n{8}'.format(self.from_, self.to, self.period, self.symbol, self.precipitation,
                                        self.windDirection, self.windSpeed, self.temperature, self.precipitation)
