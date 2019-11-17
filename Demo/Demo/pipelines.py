# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DemoPipeline(object):
    def process_item(self, item, spider):
        return item
 #初始化的操作，这里我们做本地化直接写成文件，所以初始化文件对象
    def __init__(self):
        print('实例化DemoPipeline')
        self.f = open('itcast_pipeline.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item))
        self.f.write(content)
        print(content)
        return item
    #结束后做的操作，在这里我们要关闭文件
    def close_spider(self,spider):
        print('结束')
        self.f.close()