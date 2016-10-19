from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "h1"
    def start_requests(self):
        urls = [
            'https://www.yl-invest.co.il/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        filename = "h1 headers"
        with open(filename, 'wb') as f:
            f.write(response.xpath("//h1/text()")[0].extract())