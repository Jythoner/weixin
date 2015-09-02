# -*- coding:utf-8 -*-


class ContactMessage(object):

    def __init__(self):
        self.qq_message = u'【腾讯QQ】\nQQ号码: 125094084'
        self.qq_image = 'http://7fvg10.com1.z0.glb.clouddn.com/qq.jpg'
        self.weixin_message = u'【腾讯微信】\n微信ID: huyiyang2010'
        self.weixin_image = 'http://7fvg10.com1.z0.glb.clouddn.com/wechat.png'
        self.sina_message = u'【新浪微博】\nSinaID: 丶河图洛书'
        self.sina_image = 'http://7fvg10.com1.z0.glb.clouddn.com/sina.jpg'

    def res_message(self):
        main_title = u'联系方式 .'
        main_image = 'http://7fvg10.com1.z0.glb.clouddn.com/contact.jpg'

        dic = {'main_title': main_title, 'main_image': main_image,
               'qq_message': self.qq_message, 'qq_image': self.qq_image,
               'weixin_message': self.weixin_message, 'weixin_image': self.weixin_image,
               'sina_message': self.sina_message, 'sina_image': self.sina_image}

        return dic

