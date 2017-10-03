from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class PsagotSpider(OpenPensionCrawlSpiderBase):
    name = 'psagot'
    allowed_domains = ['psagot.co.il']
    start_urls = ['https://www.psagot.co.il/heb/PensionSavings/GeneralInformation/Pages/gemelcompanyreports.aspx']
    regex = r'(.*)gSUM_(.*)(01|02|03|04)(.*).(xlsx|xls)'
