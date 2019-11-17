# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = [''www.itcast.cn'']
    start_urls = ['http://'www.itcast.cn'/']

    def parse(self, response):
        pass
