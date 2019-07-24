# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from utils.server_mongodb import format_insert_many
import logging


class CrawlProjectsPipeline(object):
    # 打开时调用此方法,只一次，类似于 init 。
    def open_spider(self, spider):
        # 实例化 logging，__name__——文件名
        self.logger = logging.getLogger(__name__)
        self.db = pymongo.MongoClient()['Crawl_Projects']

    def process_item(self, item, spider):
        # print(item._values)
        self.db[spider.collection].insert_many(format_insert_many(item._values))
        # 打印 log 及其位置
        self.logger.warning('*****')
        return item

    # 和 open_spider 对应，关闭时调用此方法。一般用于关闭数据库
    def close_spider(self, spider):
        pass
