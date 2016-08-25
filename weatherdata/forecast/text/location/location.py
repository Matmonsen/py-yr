# -*- coding: utf-8 -*-

from .time import Time


class Location(object):
    def __init__(self, location):
        self.time = self.get_times(location['time'])

    def __str__(self):

        time_str = []

        for t in self.time:
            time_str.append(t.__str__() + '\n\n')

        return '\t\t\tTime: \n{0}'.format(''.join(time_str))

    def get_times(self, times):
        time = []

        for t in times:
            time.append(Time(t))

        return time
