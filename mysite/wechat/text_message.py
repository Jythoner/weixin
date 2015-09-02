# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
from .message_xml import Message_Xml
from .performance_function.youdao import YouDao
from .performance_function.weather import Weather
from .performance_function.contact import ContactMessage
from .performance_function.constellation import SuperStar


class TextMessge(object):
    def __init__(self, fromusername, tousername):
        self.fromusername = fromusername
        self.tousername = tousername

    def dispath(self, content):

        if content == u'翻译':
            replay = u'hi~~ /可爱，按以下组合输入您想翻译的词组，我会为您自动翻译.\n\n(格式: 翻译+单词)\n例如: 翻译interface'
        elif content == u'天气':
            replay = u'hi~~ /可爱，给您提供实时天气，方便您的出行.\n\n(格式: 天气+城市)\n\n例如: 天气邯郸'
        elif content == u'星座':
            replay = u'hi~~ /可爱，为你提供星座运势查询.\n\n(格式: 星座+星座名)\n\n例如：星座双鱼座'
        else:
            replay = self.chinese_segment(content)
            if len(replay) != 2:
                result_dict = SuperStar.get_help(SuperStar())
                return Message_Xml.feature_message_xml(Message_Xml(), self.fromusername, self.tousername, **result_dict)

            else:
                keyword = replay[0]['word']
                parameter = replay[1]['word']
                replay = self.power(keyword, parameter)
                return replay
        return Message_Xml.text_message_xml(Message_Xml(), self.fromusername, self.tousername, replay)

    def chinese_segment(self, content):
        content = content.replace(' ', '')
        _SEGMENT_BASE_URL = 'http://segment.sae.sina.com.cn/urlclient.php'
        payload = urllib.urlencode([('context', content.strip().encode("utf-8")), ])
        args = urllib.urlencode([('word_tag', 1), ('encoding', 'UTF-8'), ])
        url = _SEGMENT_BASE_URL + '?' + args
        result = urllib2.urlopen(url, payload).read()
        return json.loads(result)

    def power(self, keyword, parameter):

        if keyword == u'翻译':
            result = YouDao.youdao(YouDao(), parameter)
            return Message_Xml.text_message_xml(Message_Xml(), self.fromusername, self.tousername, result)

        if keyword == u'天气':
            result_dict = Weather.get_weather(Weather(), parameter)
            return Message_Xml.imagetext_message_xml(Message_Xml(), self.fromusername, self.tousername, **result_dict)

        if keyword == u'星座':
            result_dict = SuperStar.get_info(SuperStar(), parameter)
            return Message_Xml.star_message_xml(Message_Xml(), self.fromusername, self.tousername, **result_dict)

        if keyword == u'联系':
            result_dict = ContactMessage.res_message(ContactMessage())
            return Message_Xml.contact_message_xml(Message_Xml(), self.fromusername, self.tousername, **result_dict)

        else:
            result_dict = SuperStar.get_help(SuperStar())
            return Message_Xml.feature_message_xml(Message_Xml(), self.fromusername, self.tousername, **result_dict)
