# -*- coding: utf-8 -*-


class WindDirection(object):
    def __init__(self, wind):
        self.deg = float(wind['deg'])
        self.code = wind['code']
        self.name = wind['name']

    def __str__(self):
        return '\t\t\t\tDegree: {0} \n\t\t\t\tCode: {1} \n\t\t\t\tName: {2}'.format(self.deg, self.code, self.name)