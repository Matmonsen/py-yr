# -*- coding: utf-8 -*-

from weather_report.py_yr import utilities


class Time(object):
    def __init__(self, time):
        self.from_ = utilities.parse_iso8601(time['from'])
        self.to = utilities.parse_iso8601(time['to'])
        self.title = time['title']
        self.body = time['body']
        self.remove_html_tags()

    def __str__(self):
        return '\t\t\tFrom: {0} \n\t\t\tTo: {1} \n\t\t\tTitle: {2} \n\t\t\tBody: {3}'.format(self.from_, self.to, self.title, self.body)

    def remove_html_tags(self):
        self.body = self.body.replace('<strong>', '')
        self.body = self.body.replace('</strong>', '')