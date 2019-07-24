# -*- coding: utf-8 -*-
import scrapy,json


class JrttSpider(scrapy.Spider):
    name = 'jrtt'
    # allowed_domains = ['www.jinricom']
    # start_urls = ['https://is-hl.snssdk.com/api/news/feed/v88/?list_count=0&category=news_entertainment']
    # start_urls = ['https://is-hl.snssdk.com/api/news/feed/v88/?list_count=0&category=video']
    start_urls = ['https://is-hl.snssdk.com/api/news/feed/v88/?list_count=0&category=news_tech']


    def parse(self, response):
        # print(response.text)
        guyi = json.loads(response.text)
        # print(type(guyi))
        # print(guyi)
        for i in guyi['data']:
            biaoti = json.loads(i['content'])['abstract']
            lianjie = json.loads(i['content'])['article_url']
            print(biaoti)
            print(lianjie)

"""
https://ic-hl.snssdk.com/api/news/feed/v47/?category=video&refer=1&refresh_reason=5&count=20&last_refresh_sub_entrance_interval=1563501974&loc_mode=5&tt_from=enter_auto&lac=4527&cid=28883&cp=59d9381f2b596q1&plugin_enable=4&client_extra_params=%7B%7D&iid=78957814920&device_id=68761115669&ac=wifi&channel=lite2_tengxun&aid=35&app_name=news_article_lite&version_code=703&version_name=7.0.3&device_platform=android&ab_version=668904%2C668906%2C652980%2C668903%2C679107%2C944310%2C668905%2C933995%2C643999%2C442157%2C661932%2C785656%2C668907%2C808414%2C772540%2C1016023%2C846821%2C861707%2C861726%2C996309%2C914859%2C908123%2C928942&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=z1&abflag=3&ssmix=a&device_type=OPPO+R11&device_brand=OPPO+&language=zh&os_api=22&os_version=5.1.1&uuid=866174012200610&openudid=2c83dd4935287539&manifest_version_code=703&resolution=720*1280&dpi=240&update_version_code=70313&_rticket=1563501974132&sa_enable=0&fp=G2TZFMwtJlq_FlPMc2U1F2FePrZW&tma_jssdk_version=1.21.2.1&rom_version=coloros__r11-user+5.1.1+nmf26x+500190611+release-keys&plugin_state=7563839
"""
