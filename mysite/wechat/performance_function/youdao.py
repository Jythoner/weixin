# -*- coding:utf-8 -*-
import urllib2
import json

class YouDao(object):

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
                trans = u'%s: \n%s\n\n━━━━━━━━━━━\n\n音标: %s \n\n网络释义:\n\n%s : %s\n\n%s : %s' % (
                    fanyi['query'], ''.join(fanyi['basic']['explains']), fanyi['basic']['phonetic'],
                    ' | '.join(fanyi['web'][1]['value']), fanyi['web'][1]['key'], ' | '.join(fanyi['web'][2]['value']), fanyi['web'][2]['key'])
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
