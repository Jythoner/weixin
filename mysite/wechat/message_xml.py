# -*- coding:utf-8 -*-
import time


class Message_Xml(object):
    def __init__(self):
        pass

    def text_message_xml(self, tousername, fromusername, content):
        """构造文本回复的xml
        """
        xml = """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                </xml>""" % (tousername, fromusername, str(int(time.time())), content)
        return xml

    def event_message_xml(self, tousername, fromusername, event, content):
        """构造事件回复的xml
        """
        xml = """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Event><![CDATA[%s]]></Event>
                <Content><![CDATA[%s]]></Content>
                </xml>""" % (tousername, fromusername, str(int(time.time())), event, content)
        return xml

    def imagetext_message_xml(self, *args, **kwargs):
        xml = """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>4</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item><item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item><item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item><item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item>
                </Articles>
                </xml>""" % (args[0], args[1], str(int(time.time())), kwargs['main_title'], '', kwargs['main_image'],
                             '', kwargs['today_title'], '', kwargs['today_image'], '',
                             kwargs['tomorrow_title'], '', kwargs['tomorrow_image'], '',
                             kwargs['after_tomorrow_title'], '', kwargs['after_tomorrow_image'], '')
        return xml

    def contact_message_xml(self, *args, **kwargs):
        xml = """
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>4</ArticleCount>
            <Articles>
            <item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item>
            </Articles>
            </xml>""" % (args[0], args[1], str(int(time.time())), kwargs['main_title'], '', kwargs['main_image'], '',
                         kwargs['qq_message'], '', kwargs['qq_image'], 'http://shang.qq.com/open_webaio.html?sigt=ac1e12d2236af8753b487fd18312ffae3846d00d1e331e623005508f95d6bb3762d538f7efc933d6d394f3dca6b599a6&sigu=969fd8e8325c7e592adaa6b0155e8bfa8ab0712fbe69dc9fe8f662177319d8f1458776badeeaeb5e&tuin=125094084',
                         kwargs['weixin_message'], '', kwargs['weixin_image'], 'http://weixin.qq.com/r/RkP17eXEvLjDraGO9xZU',
                         kwargs['sina_message'], '', kwargs['sina_image'], 'http://weibo.com/Jythoner')

        return xml

    def star_message_xml(self, *args, **kwargs):
        xml = """
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>1</ArticleCount>
            <Articles>
            <item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item>
            </Articles>
            </xml>""" % (args[0], args[1], str(int(time.time())), kwargs['title'], '', kwargs['image_url'],
        kwargs['url'])

        return xml

    def feature_message_xml(self, *args, **kwargs):
        xml = """
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>6</ArticleCount>
            <Articles>
            <item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item><item>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <PicUrl><![CDATA[%s]]></PicUrl>
            <Url><![CDATA[%s]]></Url>
            </item>
            </Articles>
            </xml>""" % (args[0], args[1], str(int(time.time())), kwargs['main_title'], '', kwargs['main_image'], '',
                         kwargs['translate_title'], '', kwargs['translate_image'], '',
                         kwargs['weather_title'], '', kwargs['weather_image'], '',
                         kwargs['xingzuo_title'], '', kwargs['xingzuo_image'], '',
                         kwargs['contact_title'], '', kwargs['contact_image'], '',
                         kwargs['help_title'], '', kwargs['help_image'], ''
                         )

        return xml

