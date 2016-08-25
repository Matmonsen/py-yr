# -*- coding: utf-8 -*-

from .weatherstation import WeatherStation


class Observations(object):
    def __init__(self, observations):
        self.stations = self.get_stations(observations)

    def __str__(self):
        stations_string = []
        for station in self.stations:
            stations_string.append(station.__str__()+'\n\n')
        return ''.join(stations_string)

    @staticmethod
    def get_stations(obser):
        stations = []
        for station in obser['weatherstation']:
            stations.append(WeatherStation(station))
        return stations
