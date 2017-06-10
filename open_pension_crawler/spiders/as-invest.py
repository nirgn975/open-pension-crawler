from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class AsInvestSpider(OpenPensionCrawlSpiderBase):
    name = 'as-invest'
    allowed_domains = ['as-invest.co.il']
    start_urls = ['https://www.as-invest.co.il']
    regex = r'[0-9]{9}_(b|g|p|m)[0-9]{4}_(01|02|03|04)[0-9]{2}.(xlsx|xls)'
