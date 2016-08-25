# -*- coding: utf-8 -*-


class Loc(object):
    def __init__(self, data):
        self.altitude = int(data['altitude'])
        self.latitude = float(data['latitude'])
        self.longitude = float(data['longitude'])
        self.geobase = data['geobase']
        self.geobaseid = int(data['geobaseid'])

    def __str__(self):
        return '\tAltitude: {0} ' \
               '\n\tLatitude: {1} ' \
               '\n\tLongitude: {2} ' \
               '\n\tGeobase: {3} ' \
               '\n\tGeobaseid: {4}'.format(self.altitude, self.latitude, self.longitude, self.geobase, self.geobaseid)