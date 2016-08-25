# -*- coding: utf-8 -*-

from .location import Location


class Text(object):
    def __init__(self, text):
        self.location = Location(text['location'])

    def __str__(self):
        return '\t\tLocation: \n{0}'.format(self.location)
