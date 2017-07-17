from scrapy.http import HtmlResponse
from selenium import webdriver


class OpenPensionSeleniumCrawler(object):

    def process_request(self, request, spider):
        # driver = webdriver.Ch(executable_path="/Users/roysegall/geckodriver")
        driver = webdriver.PhantomJS(executable_path='/Users/roysegall/phantomjs')
        driver.get(request.url)
        return HtmlResponse(request.url, encoding='utf-8', body=driver.page_source.encode('utf-8'))
