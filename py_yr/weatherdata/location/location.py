# -*- coding: utf-8 -*-

from .timezone import TimeZone
from .loc import Loc


class Location(object):
    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.country = data['country']
        self.timezone = TimeZone(data['timezone'])
        self.location = Loc(data['location'])

    def __str__(self):
        return '\tName: {0} ' \
               '\n\tType: {1} ' \
               '\n\tCountry: {2} ' \
               '\n\tTimezone: \n{3} ' \
               '\nLocation: {4}'.format(self.name, self.type, self.country, self.timezone, self.location)
