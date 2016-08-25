# -*- coding: utf-8 -*-


class Symbol(object):
    def __init__(self, symbol):
        self.number = int(symbol['number'])
        self.numberEx = int(symbol['numberEx'])
        self.name = symbol['name']
        self.var = symbol['var']
        
    def __str__(self):
        return '\t\t\t\tNumber: {0} \n\t\t\t\tNumberEx: {1} \n\t\t\t\tName: {2} \n\t\t\t\tVar: {3}'.format(self.number, self.numberEx, self.name, self.var)