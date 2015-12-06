# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import os
import json
import codecs

class DayegovPipeline(object):
    # Python定义类的私有变量约定双下划线表示
    __hotfocus = "http://www.hbdaye.gov.cn/xwzx/bmdt/"
    __reg = re.compile('\s+')

    def __init__(self):
        if not os.path.exists('./data'):
            os.mkdir('./data')
        self.file = codecs.open('./data/hotfocus.json','wb',encoding='utf-8')

    def process_item(self, item, spider):
        if item['link']:
            item['link'] = self.__hotfocus + item['link'][0].encode('utf-8').replace('./','')

        if item['description']:
            item['description'] = item['description'][0].encode('utf-8')
            item['description'] = re.sub(self.__reg,'',item['description'])

        if item['title']:
            item['title'] = item['title'][0]

        if item['pubtime']:
            item['pubtime'] = item['pubtime'][0]

        line = json.dumps(dict(item))+"\n"
        self.file.write(line)

    def spider_closed(self):
        self.file.close()
