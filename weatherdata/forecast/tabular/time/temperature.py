# -*- coding: utf-8 -*-


class Temperature(object):
    def __init__(self, temperature):
        self.unit = temperature['unit']
        self.value = int(temperature['value'])

    def __str__(self):
        return '\t\t\t\tUnit: {0} \n\t\t\t\tValue: {1}'.format(self.unit, self.value)