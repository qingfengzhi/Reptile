# -*- coding: utf-8 -*-
# @Time : 2019/7/18 17:05
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : github.py
# @Software: PyCharm
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    # allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'https://github.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    def parse(self, response):
        url = 'https://github.com/session'
        """
        start_request 发送请求 response 携带者 Set-Cookie. 再次 post 请求以 {Cookies: Set-Cookie} 传过去.
        """
        # 响应头获取 Set-Cookie
        Set_Cookie = response.headers.getlist('Set-Cookie')
        # Set-Cookie 是 bytes 类型转 string
        Set_Cookie = [str(i, encoding="utf-8") for i in Set_Cookie]
        # 编写请求头
        request_headers = self.headers.update(dict(Cookie='; '.join(Set_Cookie)))
        # 获取 authenticity_token
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").extract_first()
        # formdata 以 dict 形式
        post_data = dict(
            login="twden",
            password="github737598",
            commit=commit,
            utf8=utf8,
            authenticity_token=authenticity_token,
            webauthn_support=webauthn_support
        )
        yield scrapy.FormRequest(
            url=url,
            callback=self.after_login,
            headers=request_headers,
            formdata=post_data,
        )

    def after_login(self, response):
        home_page = response.xpath(".//*[@id='dashboard']/div[2]/div[1]/nav/a[1]/text()").extract()
        # 获取登录成功后页面中的文本“Browse activity”
        with open('a.html', 'w')as f:
            f.write(response.body.decode())

        if 'Browse activity' in home_page:
            self.logger.info('登录成功！')
            # 如果含有“Browse activity”，则打印登录成功
        else:
            self.logger.error('登录失败！')
