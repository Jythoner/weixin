# -*- coding:utf-8 -*-

class EventMessage(object):

    def __init__(self, event):
        self.event = event

    def dispath(self):
        if self.event == 'subscribe':
            return self.subscribe()
        else:
            return self.unsubscribe()

    def subscribe(self):
        return u'''主人你好，欢迎关注小胡的小号的订阅号，这个微信是出于业余爱好所建立， 目前具有 机器人自动回复功能，由于是机器人回复，可能有些言语不文明，请谅解 ╮(╯▽╰)╭ 。'''

    def unsubscribe(self):
        return u'我现在功能还很简单，知道满足不了您的需求，但是我会慢慢改进，欢迎您以后再来...'

