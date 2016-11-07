from scrapy.selector import Selector
import scrapy


class PensionSpider(scrapy.Spider):
    name = "h1"

    def start_requests(self):
        urls = [
            'https://www.yl-invest.co.il/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        header = Selector(response).xpath('//h1/text()')
