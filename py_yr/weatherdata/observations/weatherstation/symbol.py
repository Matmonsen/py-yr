# -*- coding: utf-8 -*-
from py_yr import utilities


class Symbol(object):
    def __init__(self, symbol):
        self.number = int(symbol['number'])
        self.name = symbol['name']
        self.time = utilities.parse_iso8601(symbol['time'])

    def __str__(self):
        return '\t\tNumber: {0} \n\t\tName: {1} \n\t\tTime: {2}'.format(self.number, self.name, self.time)