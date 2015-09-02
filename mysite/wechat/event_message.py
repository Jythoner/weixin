# -*- coding:utf-8 -*-
from .message_xml import Message_Xml


class EventMessage(object):

    def __init__(self):
        pass

    def dispath(self, fromusername, tousername, event):
        if event == 'subscribe':
            replay = self.subscribe()
        else:
            replay = self.unsubscribe()

        return Message_Xml.event_message_xml(Message_Xml(), fromusername, tousername, event, replay)

    def subscribe(self):
        return u'''主人你好，欢迎关注小胡的小号的订阅号，这个微信是出于业余爱好所建立,输入help查看功能。'''

    def unsubscribe(self):
        return u'我现在功能还很简单，知道满足不了您的需求，但是我会慢慢改进，欢迎您以后再来...'



