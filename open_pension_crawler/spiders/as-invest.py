from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class AsInvestSpider(OpenPensionCrawlSpiderBase):
    name = 'as-invest'
    allowed_domains = ['as-invest.co.il']
    start_urls = ['https://www.as-invest.co.il']
    regex = r'[0-9]{9}_(b|g|p|m)[0-9]{4}_(01|02|03|04)[0-9]{2}.(xlsx|xls)'

    rules = (
        # Extract 'href' and 'ng-href' links and parse them with the spider's method parse_item.
        Rule(LinkExtractor(
            attrs=['href', 'ng-href'],
            deny_domains=['online.as-invest.co.il', 'http://agents.as-invest.co.il']),
            callback="parse_item",
            follow=True
        ),
    )
