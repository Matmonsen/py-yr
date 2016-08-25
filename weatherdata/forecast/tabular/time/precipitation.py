# -*- coding: utf-8 -*-


class Precipitation(object):
    def __init__(self, precipitation):
        self.value = float(precipitation['value'])
        try:
            self.minValue = float(precipitation['minvalue'])
        except KeyError:
            self.minValue = None
        try:
            self.maxValue = float(precipitation['maxvalue'])
        except KeyError:
            self.maxValue = None

    def __str__(self):
        return '\t\t\t\tValue: {0} \n\t\t\t\tMinValue: {1} \n\t\t\t\tMaxValue: {2}'.format(self.value, self.minValue, self.maxValue)