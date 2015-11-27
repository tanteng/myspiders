from scrapy.spiders import Spider,CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from dayegov.items import DayegovItem


class HotSpider(CrawlSpider):
    name = "hotfocus"
    allowed_domains = ["hbdaye.gov.cn"]
    start_urls = [
        "http://www.hbdaye.gov.cn/xwzx/bmdt/index.shtml",
    ]
    # http://www.hbdaye.gov.cn/xwzx/bmdt/index_1.shtml
    rules = [
        Rule(LinkExtractor(allow=('index_\d+.shtml')),
             callback="parse"),
    ]

    for page in range(1,50):
        start_urls.append('http://www.hbdaye.gov.cn/xwzx/bmdt/index_' + str(page) + '.shtml')



    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//div[@class="list_content"]/div[@class="list_cloumn"]')

        for article in articles:
            item = DayegovItem()
            item['title'] = article.xpath('ul/li[1]/h2/a/text()').extract()
            item['link'] = article.xpath('ul/li[1]/h2/a/@href').extract()
            item['description'] = article.xpath('ul/li[2]/p/text()').extract()

            yield item