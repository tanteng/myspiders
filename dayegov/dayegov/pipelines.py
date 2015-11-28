# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class DayegovPipeline(object):

    hotfocus = "http://www.hbdaye.gov.cn/xwzx/bmdt/"
    reg = re.compile('\s+')

    def process_item(self, item, spider):
        if item['link']:
            item['link'] = self.hotfocus + item['link'][0].encode('utf-8').replace('./','')

        if item['description']:
            item['description'] = item['description'][0].encode('utf-8')
            item['description'] = re.sub(self.reg,'',item['description'])

        return item