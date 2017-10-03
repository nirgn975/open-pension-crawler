from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class XnesSpider(OpenPensionCrawlSpiderBase):
    name = 'xnes'
    allowed_domains = ['xnes.co.il']
    start_urls = ['https://www.xnes.co.il/pension/About/Statements.aspx']
    regex = r'(.*)[0-9]{2}.(xlsx|xls)'
