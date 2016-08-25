# -*- coding: utf-8 -*-

from weather_report.py_yr import utilities


class Meta(object):
    def __init__(self, meta):
        self.lastupdate = utilities.parse_iso8601(meta['lastupdate'])
        self.nextupdate = utilities.parse_iso8601(meta['nextupdate'])

    def __str__(self):
        return '\tLastUpdate: {0} \n\tNextUpdate: {1}'.format(self.lastupdate, self.nextupdate)