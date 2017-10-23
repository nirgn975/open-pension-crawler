from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class AmitimSpider(OpenPensionCrawlSpiderBase):
    name = 'amitim'
    allowed_domains = ['http://www.amitim.com/wps/portal/']
    start_urls = ['http://www.amitim.com/wps/portal/']
    regex = r'[0-9]*_[b|g|p|m][0-9]{0,4}_(01|02|03|04)[0-9]{2}.(xlsx|xls)'
