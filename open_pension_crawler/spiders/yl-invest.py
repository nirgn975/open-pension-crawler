from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class YlInvestSpider(OpenPensionCrawlSpiderBase):
    name = 'yl-invest'
    allowed_domains = ['yl-invest.co.il']
    start_urls = ['http://www.yl-invest.co.il']
    file_prefix = 'yl_'
    regex = r'[0-9]{9}_(b|g|p|m)[0-9]{4}_(01|02|03|04)[0-9]{2}.(xlsx|xls)'
