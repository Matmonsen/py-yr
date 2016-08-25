# -*- coding: utf-8 -*-

from .text import Text
from .tabular import Tabular


class Forecast(object):
    def __init__(self, forecast):
        self.tabular = Tabular(forecast['tabular'])
        try:
            self.text = Text(forecast['text'])
        except KeyError:
            self.text = None

    def __str__(self):
        return '\tTabular: \n{0}' \
               '\n\tText: \n{1}'.format(self.tabular, self.text)
