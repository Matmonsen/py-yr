# -*- coding: utf-8 -*-

from .link import Link


class Links(object):
    def __init__(self, links):
        self.xmlSource = Link(links['link'][0])
        self.xmlSourceHourByHour = Link(links['link'][1])
        self.overview = Link(links['link'][2])
        self.hourbyhour = Link(links['link'][3])
        self.longTermForecast = Link(links['link'][4])
        try:
            self.radar = Link(links['link'][5])
        except IndexError:
            self.radar = None

    def __str__(self):
        return '\txmlSource: \n{0} ' \
               '\n\txmlSourceHourByHour: \n{1} ' \
               '\n\tOverview: \n{2} ' \
               '\n\tHourByHour: \n{3} ' \
               '\n\tLongTermForecast: \n{4} ' \
               '\n\tRadar: \n{5}'.format(self.xmlSource, self.xmlSourceHourByHour, self.overview, self.hourbyhour,
                                     self.longTermForecast, self.radar)