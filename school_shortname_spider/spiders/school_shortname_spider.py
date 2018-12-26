"""
@Author: liyinwei
@E-mail: coridc@foxmail.com
@Time: 2018-12-25 16:10
@Description: 学校简称
"""
import re
from urllib.parse import unquote
import pandas as pd
from scrapy import Spider
from school_shortname_spider.items import SchoolShortnameSpiderItem


class AreaSpider(Spider):
    def __init__(self):
        self.reg = re.compile(u'[^\u4E00-\u9FA5A-Za-z、]')

    name = "school_shortname_spider"

    allowed_domains = ['baidu.com']
    import os
    print(os.getcwd())
    print(os.path.abspath(os.path.dirname(__file__)))

    schools = pd.read_excel('./school_shortname_spider/data/2017年高校名单.xls')

    start_urls = schools['学校名称'].apply(
        lambda x: 'http://www.baidu.com/s?wd=%s简称' % x
    ).values
    # start_urls = ['http://www.baidu.com/s?wd=中央财经大学简称', 'http://www.baidu.com/s?wd=浙江大学简称']

    def parse(self, response):
        """
        处理省份页面
        :param response:
        :return:
        """
        url = unquote(response.request.url)
        item = SchoolShortnameSpiderItem()
        item['full_name'] = url[url.find('=') + 1:-2]
        item['short_name'] = self.reg.sub('', ''.join(
            response.xpath('//div[@class="op_exactqa_s_answer"]/text()').extract()))
        yield item
