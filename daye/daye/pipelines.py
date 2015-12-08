# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
import codecs

class DayegovPipeline(object):
    hotfocus = "http://www.hbdaye.gov.cn/xwzx/bmdt/"
    count = 0
    page = 1

    def __init__(self):
        if not os.path.exists('./data'):
            os.mkdir('./data')
        self.file = codecs.open('./data/hotfocus.json','wb',encoding='utf-8')


    def process_item(self, item, spider):
        if item['link']:
            item['link'] = self.hotfocus + item['link'][0].encode('utf-8').replace('./','')

        if item['description']:
            item['description'] = item['description'][0]

        if item['title']:
            item['title'] = item['title'][0]

        if item['pubtime']:
            item['pubtime'] = item['pubtime'][0]

        self.count += 1

        # 每20条记录分页存储
        if self.count == 20:
            self.count = 0
            self.page += 1

            if self.page > 1:
                self.file = codecs.open('./data/hotfocus'+str(self.page)+'.json','wb',encoding='utf-8')

        line = json.dumps(dict(item))+"\n"
        self.file.write(line)

    def spider_closed(self):
        self.file.close()
