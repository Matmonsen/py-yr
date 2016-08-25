# -*- coding: utf-8 -*-


class Credit(object):
    def __init__(self, credit):
        self.url = credit['link']['url']
        self.text = credit['link']['text']

    def __str__(self):
        return '\tUrl: {0} \n\tText: {1}'.format(self.url, self.text)