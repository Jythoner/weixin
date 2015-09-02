# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from views import WechatInterface


urlpatterns = patterns('',
    url(r'^$', csrf_exempt(WechatInterface.as_view())),

)