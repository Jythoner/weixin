# -*- coding:utf-8 -*-


class FeatureMessage(object):

    def __init__(self):
        self.translate_title = u'回复【翻译】，中英互译.'
        self.translate_image = 'http://7fvg10.com1.z0.glb.clouddn.com/translate.jpg'
        self.weather_title = u'回复【天气】，天气查询.'
        self.weather_image = 'http://7fvg10.com1.z0.glb.clouddn.com/weather.jpg'
        self.xingzuo_title = u'回复【星座】，星座运势查询.'
        self.xingzuo_image = 'http://7fvg10.com1.z0.glb.clouddn.com/xingzuo.jpg'
        self.contact_title = u'回复【联系方式】, 获取微主联系方式.'
        self.contact_image = 'http://7fvg10.com1.z0.glb.clouddn.com/contact.jpg'
        self.help_title = u'回复【help】，查看功能.'
        self.help_image = 'http://7fvg10.com1.z0.glb.clouddn.com/help.jpg'

    def get_help(self):
        main_title = u'fetch-message功能大全.'
        main_image = 'http://7fvg10.com1.z0.glb.clouddn.com/main.jpg'
        dic = {'main_title': main_title, 'main_image': main_image}

        return dic
