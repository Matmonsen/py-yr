# -*- coding: utf-8 -*-


class WindSpeed(object):
    def __init__(self, wind):
        self.mps = float(wind['mps'])
        self.name = wind['name']
    
    def __str__(self):
        return '\t\t\t\tMps: {0} \n\t\t\t\tName: {1}'.format(self.mps, self.name)