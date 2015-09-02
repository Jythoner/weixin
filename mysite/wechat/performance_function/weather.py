# -*- coding:utf-8 -*-
import json
import urllib2


class Weather(object):
    def __init__(self):
        self.BAIDU_API = 'UUQeN2DqGrzsHaHeNTUDBtNY'

    def get_weather(self, city):
        if isinstance(city, unicode):
            city = city.encode('utf-8')
        city = urllib2.quote(city)
        Base_url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=' % city
        url = Base_url + self.BAIDU_API
        response = urllib2.urlopen(url).read()

        return self.response_weather(json.loads(response))

    def response_weather(self, json_data):
        result = json_data['results'][0]

        main_title = u'%s近期天气情况 .' % result['currentCity']
        main_image = 'http://img02.tooopen.com/images/20141231/sy_78327074576.jpg'
        today_title = u'%s, %s, %s , %s' % (result['weather_data'][0]['date'],
                                                result['weather_data'][0]['weather'], result['weather_data'][0]['wind'],
                                                result['weather_data'][0]['temperature'])
        today_image = result['weather_data'][0]['dayPictureUrl']
        tomorrow_title = u'%s, %s, %s , %s' % (result['weather_data'][1]['date'],
                                                   result['weather_data'][1]['weather'],
                                                   result['weather_data'][1]['wind'],
                                                   result['weather_data'][1]['temperature'])
        tomorrow_image = result['weather_data'][1]['dayPictureUrl']
        after_tomorrow_title = u'%s, %s, %s , %s' % (result['weather_data'][2]['date'],
                                                         result['weather_data'][2]['weather'],
                                                         result['weather_data'][2]['wind'],
                                                         result['weather_data'][2]['temperature'])
        after_tomorrow_image = result['weather_data'][2]['dayPictureUrl']

        dic = {'main_title': main_title, 'main_image': main_image,
               'today_title': today_title, 'today_image': today_image,
               'tomorrow_title': tomorrow_title, 'tomorrow_image': tomorrow_image,
               'after_tomorrow_title': after_tomorrow_title, 'after_tomorrow_image': after_tomorrow_image
        }

        return dic
