# -*- coding: utf-8 -*-

from .location import Location
from .credit import Credit
from .forecast import Forecast
from .links import Links
from .Meta import Meta
from .observations import Observations
from .sun import Sun


class WeatherData(object):
    def __init__(self, data):
        self.credit = Credit(data['credit'])
        self.meta = Meta(data['meta'])
        self.sun = Sun(data['sun'])
        self.forecast = Forecast(data['forecast'])
        self.links = Links(data['links'])
        self.location = Location(data['location'])
        try:
            self.observations = Observations(data['observations'])
        except KeyError:
            self.observations = None

    def __str__(self):
        return 'Credit: \n{0} ' \
               '\nMeta: \n{1} ' \
               '\nSun: \n{2}: ' \
               '\nForecast: \n{3} ' \
               '\nLinks: \n{4} ' \
               '\nLocation: \n{5} ' \
               '\nObservations: \n{6}'.format(self.credit, self.meta, self.sun, self.forecast, self.links,
                                              self.location,
                                              self.observations)
