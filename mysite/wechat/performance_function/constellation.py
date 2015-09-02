# -*- coding:utf-8 -*-


Status = {
    u'白羊座': 'Aries', u'金牛座': 'Taurus', u'双子座': 'Gemini', u'巨蟹座': 'Cancer',
    u'狮子座': 'Leo', u'处女座': 'Virgo', u'天秤座': 'Libra', u'天蝎座': 'Scorpio',
    u'射手座': 'Sagittarius', u'摩羯座': 'Capricorn', u'水瓶座': 'Aquarius', u'双鱼座': 'Pisces'
}

Star = {
    u'白羊座': 'http://7fvg10.com1.z0.glb.clouddn.com/1.jpg',
    u'金牛座': 'http://7fvg10.com1.z0.glb.clouddn.com/2.jpg',
    u'双子座': 'http://7fvg10.com1.z0.glb.clouddn.com/3.jpg',
    u'巨蟹座': 'http://7fvg10.com1.z0.glb.clouddn.com/4.jpg',

    u'狮子座': 'http://7fvg10.com1.z0.glb.clouddn.com/5.jpg',
    u'处女座': 'http://7fvg10.com1.z0.glb.clouddn.com/6.jpg',
    u'天秤座': 'http://7fvg10.com1.z0.glb.clouddn.com/7.jpg',
    u'天蝎座': 'http://7fvg10.com1.z0.glb.clouddn.com/8.jpg',

    u'射手座': 'http://7fvg10.com1.z0.glb.clouddn.com/9.jpg',
    u'摩羯座': 'http://7fvg10.com1.z0.glb.clouddn.com/10.jpg',
    u'水瓶座': 'http://7fvg10.com1.z0.glb.clouddn.com/11.jpg',
    u'双鱼座': 'http://7fvg10.com1.z0.glb.clouddn.com/12.jpg'
}

num = {
    u'白羊座': '1', u'金牛座': '2', u'双子座': '3', u'巨蟹座': '4',
    u'狮子座': '5', u'处女座': '6', u'天秤座': '7', u'天蝎座': '8',
    u'射手座': '9', u'摩羯座': '10', u'水瓶座': '11', u'双鱼座': '12'
}


class SuperStar(object):
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

    def get_info(self, name):

        url = 'http://wap.weixiaoxin.com/AstroShow/gday/?aid=%s' % num[name]
        title = u'%s(%s)_今日运势' %(name, Status[name])
        dic = {'title': title, 'image_url': Star[name], 'url': url}

        return dic

    def get_help(self):
        main_title = u'fetch-message功能大全.'
        main_image = 'http://7fvg10.com1.z0.glb.clouddn.com/slient.jpg'
        dic = {'main_title': main_title, 'main_image': main_image,
               'translate_title': self.translate_title, 'translate_image': self.translate_image,
               'weather_title': self.weather_title, 'weather_image': self.weather_image,
               'xingzuo_title': self.xingzuo_title, 'xingzuo_image': self.xingzuo_image,
               'contact_title': self.contact_title, 'contact_image': self.contact_image,
               'help_title': self.help_title, 'help_image': self.help_image}

        return dic


if __name__ == '__main__':
    obj = SuperStar.get_info(SuperStar(), u'双鱼座')






