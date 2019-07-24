# -*- coding: utf-8 -*-
# @Time : 2019/7/23 15:05
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : dfgg.py
# @Software: PyCharm
from .zygg import ZyggSpider


class DfggSpider(ZyggSpider):
    name = 'dfgg'
    start_urls = ['http://www.ccgp.gov.cn/cggg/dfgg/']
