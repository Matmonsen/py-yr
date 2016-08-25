# -*- coding: utf-8 -*-


class Link(object):
    def __init__(self, link):
        self.url = link['url']
        self.id = link['id']

    def __str__(self):
        return '\t\tId: {0} \n\t\tUrl: {1}'.format(self.id, self.url)