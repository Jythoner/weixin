# -*- coding: utf-8 -*-
import hashlib
from lxml import etree
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.views.generic import View
from .handle_message import HandleMessage


class WechatInterface(View):

    def __init__(self):
        super(WechatInterface, self).__init__()
        self.token = 'weixin'    #微信公众平台token验证设置

    def get(self, request, *args, **kwargs):
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', '')
        alist = [self.token, timestamp, nonce]
        alist.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, alist)
        if signature == sha1.hexdigest():
            return HttpResponse(echostr)
        else:
            return HttpResponse(None)

    def post(self, request, *args, **kwargs):
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = HandleMessage.dispath_message(HandleMessage(), request_xml)
        return HttpResponse(response_xml)
