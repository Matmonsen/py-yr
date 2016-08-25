# -*- coding: utf-8 -*-
from py_yr import utilities


class WindSpeed(object):
    def __init__(self, speed):
        self.mps = float(speed['mps'])
        self.name = speed['name']
        try:
            self.time = utilities.parse_iso8601(speed['time'])
        except KeyError:
            self.time = None

    def __str__(self):
        return '\t\tMps: {0} \n\t\tName: {1} \n\t\tTime: {2}'.format(self.mps, self.name, self.time)