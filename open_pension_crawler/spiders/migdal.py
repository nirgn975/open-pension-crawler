from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class MigdalSpider(OpenPensionCrawlSpiderBase):
    name = 'migdal'
    allowed_domains = ['www.migdal.co.il']
    start_urls = ['https://www.migdal.co.il/He/MigdalTeam/investments/Assets/Pages/Assets16_Q3.aspx']
    regex = r'(.*)[0-9]{2}.(xlsx|xls)'
