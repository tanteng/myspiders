from scrapy.spiders import Spider
from scrapy.selector import Selector

from dayegov.items import DayegovItem


class HotSpider(Spider):
    name = "hotfocus"
    allowed_domains = ["hbdaye.gov.cn"]
    start_urls = [
        "http://www.hbdaye.gov.cn/xwzx/bmdt/index.shtml",
    ]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//div[@class="list_content"]/div[@class="list_cloumn"]')
        items = []

        for article in articles:
            item = DayegovItem()
            item['title'] = article.xpath('ul/li[1]/h2/a/text()').extract()
            item['link'] = article.xpath('ul/li[1]/h2/a/@href').extract()
            item['description'] = article.xpath('ul/li[2]/p/text()').extract()

            items.append(item)

        return items