# -*- coding:utf-8 -*-
from .event_message import EventMessage
from .text_message import TextMessge

class HandleMessage(object):

    def __init__(self):
        pass

    def dispath_message(self, request_xml):
        msgtype = request_xml.find('MsgType').text
        fromusername = request_xml.find('FromUserName').text
        tousername = request_xml.find('ToUserName').text
        if msgtype == 'text':
            content = request_xml.find('Content').text
            replay = TextMessge(fromusername, tousername).dispath(content)
            return replay

        elif msgtype == 'event':
            event = request_xml.find('Event').text
            return EventMessage.dispath(EventMessage(), fromusername, tousername, event)

