from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class ClalbitSpider(OpenPensionCrawlSpiderBase):
    name = 'clalbit'
    allowed_domains = ['clalbit.co.il']
    start_urls = ['https://www.clalbit.co.il']
    regex = r'[0-9]{9}_(b|g|p|m)[0-9]{4}_(01|02|03|04)[0-9]{2}.(xlsx|xls)'
