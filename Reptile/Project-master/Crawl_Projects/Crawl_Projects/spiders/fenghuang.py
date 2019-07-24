# -*- coding: utf-8 -*-
import scrapy,time


class FenghuangSpider(scrapy.Spider):
    name = 'fenghuang'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.ifeng.com/']

    def parse(self, response):
        #获取源码
        # print(response.text)
        #标题启动
        guyi = response.xpath('//*[@id="newsList"]')
        # print(guyi)
        for i in guyi:
            title = '\n'.join(i.xpath('./ul/li//text()').extract())
            lianjie = '\n'.join(i.xpath('./ul/li/a/@href').extract())
            # print(title)
            # print(lianjie)
