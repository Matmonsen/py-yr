# -*- coding: utf-8 -*-

from weather_report.py_yr import utilities


class Temperature(object):
    def __init__(self, temperature):
        self.unit = temperature['unit']
        self.value = float(temperature['value'])
        self.time = utilities.parse_iso8601(temperature['time'])

    def __str__(self):
        return '\t\tUnit: {0} \n\t\tValue: {1} \n\t\tTime: {2}'.format(self.unit, self.value, self.time)