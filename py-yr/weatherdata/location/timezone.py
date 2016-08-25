# -*- coding: utf-8 -*-


class TimeZone(object):
    def __init__(self, timezone):
        self.id = timezone['id']
        self.utcoffsetMinutes = int(timezone['utcoffsetMinutes'])

    def __str__(self):
        return '\t\tId: {0} \n\t\tUtcOffsetminutes: {1}'.format(self.id, self.utcoffsetMinutes)