# -*- coding: utf-8 -*-

from .time import Time


class Tabular(object):
    def __init__(self, tabular):
        self.time = self.get_times(tabular['time'])

    def __str__(self):

        tabular_str = []

        for t in self.time:
            tabular_str.append(t.__str__() + '\n\n\t')

        return '\t\tTime: \n{0}'.format(''.join(tabular_str))

    def get_times(self, times):
        time = []

        for t in times:
            time.append(Time(t))

        return time
