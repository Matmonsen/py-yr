# -*- coding: utf-8 -*-

from weather_report.py_yr import utilities


class WindDirection(object):
    def __init__(self, direction):
        self.degree = float(direction['deg'])
        self.name = direction['name']
        try:
            self.time = utilities.parse_iso8601(direction['time'])
        except KeyError:
            self.time = None

    def __str__(self):
        return '\t\tDegree: {0} \n\t\tName: {1} \n\t\tTime: {2}'.format(self.degree, self.name, self.time)