# -*- coding: utf-8 -*-
import scrapy

import re
from Demo.items import DemoItem


class ItcastSpider(scrapy.Spider):
    name = 'demo'
     # 允许域,可以是多个
    allowed_domains = ['http://www.itcast.cn']

    # scrapy 开始发起请求的地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    #http://resource.boxuegu.com/booklist/

    def parse(self, response):
        html = response.text
        reg = r'<img data-original="(.*?)">.*?<div class="li_txt">.*?<h3>(.*?)</h3>.*?<h4>(.*?)</h4>.*?<p>(.*?)</p>'
        infos = re.findall(reg, html, re.S)

        for img, name, grade, talk in infos:
            item = DemoItem()
            item['name'] = name
            item['grade'] = grade
            item['info'] = talk
            item['img'] = self.allowed_domains[0] + img
            # 这里是用的yield 而不是return
            yield item

    def parse1(self, response):
        html = response.text
        reg = r'<img data-original="(.*?)">.*?<div class="li_txt">.*?<h3>(.*?)</h3>.*?<h4>(.*?)</h4>.*?<p>(.*?)</p>'
        infos = re.findall(reg, html, re.S)

        for img, name, grade, talk in infos:
            item = DemoItem()
            item['name'] = name
            item['grade'] = grade
            item['info'] = talk
            item['img'] = self.allowed_domains[0] + img
            # 这里是用的yield 而不是return
            yield item