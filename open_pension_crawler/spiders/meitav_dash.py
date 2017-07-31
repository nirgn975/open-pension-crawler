from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class MeitavDashSpider(OpenPensionCrawlSpiderBase):
    name = 'meitav_dash'
    allowed_domains = ['https://www.meitavdash.co.il']
    start_urls = ['https://www.meitavdash.co.il/companies-and-business-units/keren-pensia/reports/']
    regex = r'[0-9]*_[0-9]*_[0-9]*_[0-9]*_(Q1|Q2|Q3|Q4)[0-9]*.(xlsx|xls)'
