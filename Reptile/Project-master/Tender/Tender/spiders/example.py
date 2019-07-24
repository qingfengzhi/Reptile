import requests
from lxml import etree

# r = requests.get('https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=581209')
# print(r)
# 'https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeType=2&noticeBean.companyType=professional'
# 'https://b2b.10086.cn/b2b/main/showNotice.html?noticeBean.noticeType=3&noticeBean.companyType=hq      &noticeBean.eppNoticeType=11,13'
# 'https://b2b.10086.cn/b2b/main/showNotice.html?noticeBean.noticeType=3&noticeBean.companyType=professional&noticeBean.eppNoticeType=11,13'
# 'https://b2b.10086.cn/b2b/main/listVendorNoticeResult.html?noticeBean.noticeType=3'
# 总公司——hq 省公司——province  专业公司——professional
request_headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
response1 = requests.get('https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2',
                         headers=request_headers1)
response_headers1 = response1.headers
c = response_headers1.get('set-cookie')
key = etree.HTML(response1.content.decode()).xpath('//input[@name="_qt"]/@value')[0]
import re

r = ''.join(re.compile(r'saplb_\*=\([\w]+\)[\d]+; ').findall(c) + re.compile(r'JSESSIONID=[\w-]+;').findall(c)).strip(
    ';')
print(r)
data = {
    '_qt': key,
    'page.currentPage': '1',
    'page.perPageSize': '20',
    'noticeBean.sourceCH': '',
    'noticeBean.source': '',
    'noticeBean.title': '',
    'noticeBean.startDate': '',
    'noticeBean.endDate': '',
}
request_headers2 = {
    'Referer': 'https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2',
    'Cookie': r,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
# print(request_headers2)
url = 'https://b2b.10086.cn/b2b/main/listVendorNoticeResult.html?noticeBean.noticeType=7'
r = requests.post(url=url, data=data, headers=request_headers2).content.decode()
print(r)
t = etree.HTML(r).xpath('//a/@title')
print(t)
# 采购公告——2
