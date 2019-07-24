# -*- coding: utf-8 -*-
# @Time : 2019/7/21 14:04
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : jobbole.py
# @Software: PyCharm
from scrapy_redis.spiders import RedisSpider


class JobboleSpider(RedisSpider):
    name = 'jobbole'
    # allowed_domains = ['blog.jobbole.com']
    collection = 'news'
    redis_key = 'jobbole:start_urls'

    # start_urls = ['http://tech.163.com/special/gd2016/']

    def parse(self, response):
        print(response.url)
