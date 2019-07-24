# -*- coding: utf-8 -*-
import scrapy


class CaigouSpider(scrapy.Spider):
    name = 'caigou'
    # allowed_domains = ['www.caigou.com']
    start_urls = ['http://www.ccgp.gov.cn/cggg/zygg/']

    def parse(self, response):
        print(response.text)


