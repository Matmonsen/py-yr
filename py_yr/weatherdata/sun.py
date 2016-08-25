# -*- coding: utf-8 -*-

from weather_report.py_yr import utilities


class Sun(object):
    def __init__(self, sun):
        self.rise = utilities.parse_iso8601(sun['rise'])
        self.set = utilities.parse_iso8601(sun['set'])

    def __str__(self):
        return '\tRise: {0} \n\tSet: {1}'.format(self.rise, self.set)