import scrapy,json


class JrttSpider(scrapy.Spider):
    name = 'tyc'
    # allowed_domains = ['www.jinricom']
    start_urls = ['https://www.tianyancha.com/?jsid=SEM-BAIDU-PZ1907-SY-000100']


    def parse(self, response):
        print(response.text)
