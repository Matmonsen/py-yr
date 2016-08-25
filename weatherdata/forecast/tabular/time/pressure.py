# -*- coding: utf-8 -*-


class Pressure(object):
    def __init__(self, pressure):
        self.unit = pressure['unit']
        self.value = float(pressure['value'])

    def __str__(self):
        return '\t\t\t\tUnit: {0} \n\t\t\t\tValue: {1}'.format(self.unit, self.value)