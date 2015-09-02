# -*- coding:utf-8 -*-
import urllib2
import json

class TextMessage(object):

    def __init__(self):
        self.API_KEY = 1907689986  # 有道API设置
        self.KEY_FROM = 'virtualenv'

    def youdao(self, word):
        if isinstance(word, unicode):
            word = word.encode('utf-8')
        qword = urllib2.quote(word)
        base_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=json&version=1.1&q=' % (
            self.KEY_FROM, self.API_KEY)
        url = base_url + qword
        resp = urllib2.urlopen(url)
        fanyi = json.loads(resp.read())
        if fanyi['errorCode'] == 0:
            if 'basic' in fanyi.keys():
                trans = u'【查询单词】: %s \n【翻译】: %s\n【解释】: %s\n【网络释义】：\n%s' % (
                    fanyi['query'], ''.join(fanyi['translation']), ''.join(fanyi['basic']['explains']),
                    '\n'.join(fanyi['web'][0]['value']))
            else:
                trans = u'%s:\n【基本翻译】:%s\n' % (fanyi['query'], ''.join(fanyi['translation']))

            return trans
        elif fanyi['errorCode'] == 20:
            return u'对不起，要翻译的文本过长.'
        elif fanyi['errorCode'] == 30:
            return u'对不起，无法进行有效的翻译.'
        elif fanyi['errorCode'] == 40:
            return u'对不起，不支持的语言类型.'
        else:
            return u'对不起，您输入的单词%s无法翻译，请检查拼写.' % word

    def machine(self, ask):
        if isinstance(ask, unicode):
            ask = ask.encode('utf-8')
        enask = urllib2.quote(ask)
        cookies = {
            'Cookie': 'AWSELB=B9551BF112497261E578B202D2B846B8A14A9E1649CB0437E6911BDD2F8B94DFC543CC723803EBDD4C47F84244016C7397B26926368A8594CAC5AB79099CD419DF99533536; uid=98750759; simsimi_uid=566843; simsimi_uid=566843; ft=1.0; ft=1.0; selected_nc=ch; selected_nc=ch; SimSimiSid=s%3A1WrVLaa-_6tO96NuQYLXkshvXm1yLlKZ.PbEE5%2FAmMUJrkpwMLgdBkrqC6q%2BUS07WskdFX2HBpts'
        }
        base_url = 'http://www.simsimi.com/func/app/request_p?fl=http%3A%2F%2Fwww.simsimi.com%2Ftalk.htm&request_text='
        url = base_url + enask
        req = urllib2.Request(url, headers=cookies)
        response = urllib2.urlopen(req).read()
        repaly = json.loads(response)

        try:
            result = repaly['response']
        except KeyError:
            result = u'主人，你们城里人真会玩.'

        return result

