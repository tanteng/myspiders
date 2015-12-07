# coding=utf-8
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from scrapy import log
from bs4 import BeautifulSoup
from dayegov.items import DayegovItem
import sys


class HotSpider(CrawlSpider):
    name = "hotfocus"
    allowed_domains = ["hbdaye.gov.cn"]
    start_urls = [
        "http://www.hbdaye.gov.cn/xwzx/bmdt/index.shtml",
    ]

    for page in range(1, 50):
        start_urls.append('http://www.hbdaye.gov.cn/xwzx/bmdt/index_' + str(page) + '.shtml')

    def parse(self, response):
        selector = Selector(response)

        articles = selector.xpath('//div[@class="list_content"]/div[@class="list_cloumn"]')

        for article in articles:
            item = DayegovItem()
            item['title'] = article.xpath('ul/li[1]/h2/a/text()').extract()
            item['link'] = article.xpath('ul/li[1]/h2/a/@href').extract()
            item['description'] = article.xpath('ul/li[2]/p/text()').extract()
            item['pubtime'] = article.xpath('ul/li[1]/span/text()').extract()
            link = item['link'][0].encode('utf-8')
            link = link.replace('./', '')
            link = "http://www.hbdaye.gov.cn/xwzx/bmdt/" + link

            yield Request(link, meta={'item': item, 'link':link}, callback=self.parse_item)

    def parse_item(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body, 'lxml')

        try:
            item['content'] = soup.find(id='fontzoom').prettify()
            return item

        except Exception, e:
            print e,response.meta['link']
            pass
