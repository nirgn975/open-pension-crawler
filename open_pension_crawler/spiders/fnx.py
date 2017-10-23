from open_pension_crawler.OpenPensionCrawlSpiderBase import OpenPensionCrawlSpiderBase


class FnxSpider(OpenPensionCrawlSpiderBase):
    name = 'fnx'
    allowed_domains = ['www.fnx.co.il']
    start_urls = ['https://www.fnx.co.il/pension-savings/pension/phoenix-pension-providence-ltd/'
                  'quarterly-assets-list.aspx']
    regex = r'(.*)(01|02|03|04)[0-9]{2}.(xlsx|xls)'
