# -*- coding: utf-8 -*-
# @Time : 2019/7/23 8:20
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : zygg.py
# @Software: PyCharm
import scrapy
from itertools import count
import requests
import pinyin
from ..items import TenderItem


class ZyggSpider(scrapy.Spider):
    name = 'zygg'
    # allowed_domains = ['example.com']
    start_urls = ['http://www.ccgp.gov.cn/cggg/zygg/']
    kw_list = ['采购项目名称', '品目', '采购单位', '总中标金额', '项目联系人', '项目联系电话', '采购单位地址', '采购单位联系方式', '代理机构名称', '代理机构地址', '代理机构联系方式']
    dict1 = {}

    def parse(self, response):
        for p in count(1, 1):
            url = response.url + 'index_{}.htm'.format(p)
            r = requests.get(url).content.decode('utf8')
            if '对不起，您所访问的页面不存在' in r:
                url = response.url + 'index.htm'
                yield scrapy.Request(url, callback=self.parse_to_detail)
                break
            else:
                yield scrapy.Request(url, callback=self.parse_to_detail)

    def parse_to_detail(self, response):
        hrefs = response.xpath('//ul[@class="c_list_bid"]/li/a/@href').getall()
        if hrefs != []:
            for href in [self.start_urls[0] + h.strip('.') for h in hrefs]:
                yield scrapy.Request(href, callback=self.parse_detail)

    def parse_detail(self, response):
        # print(response.url)
        self.dict1.update(
            title_h2=response.xpath('//h2/text()').get('暂无'),
            pubTime=response.xpath('//span[@id="pubTime"]/text()').get('暂无'),
            sourceName=response.xpath('//span[@id="sourceName"]/text()').get('中国政府采购网'),
        )
        for kw in self.kw_list:
            k = pinyin.get(kw, format='numerical')
            v = response.xpath('//td[contains(text(),"{}")]/following-sibling::td//text()'.format(kw)).get('暂无')
            self.dict1.update({k: v})
        itemTenderItem = TenderItem()
        itemTenderItem['total'] = self.dict1
        print(itemTenderItem)
        # yield itemTenderItem
