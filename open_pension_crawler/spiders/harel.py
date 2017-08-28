from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class HarelSpider(OpenPensionCrawlSpiderBase):
    name = 'harel'
    allowed_domains = ['www.harel-group.co.il']
    start_urls = ['https://www.harel-group.co.il/long-term-savings/pension/funds/pension/Pages/list-of-assets.aspx']
    regex = r'(.*)%D7%A8%D7%A9%D7%99%D7%9E%D7%95%D7%AA%20%D7%A0%D7%9B%D7%A1%D7%99%D7%9D(.*).(xlsx|xls)'
