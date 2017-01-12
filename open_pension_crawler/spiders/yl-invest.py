import scrapy
import re
import urllib.request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class YlInvestSpider(CrawlSpider):
    name = 'yl-invest'
    allowed_domains = ['yl-invest.co.il']
    start_urls = ['http://www.yl-invest.co.il']
    rules = (
        # Extract 'href' and 'ng-href' links and parse them with the spider's method parse_item
        Rule(LinkExtractor(attrs=['href', 'ng-href']), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        # Get all the href from the page
        urls = response.xpath('//a/@href')

        # Loop throgh them and extract only the files urls
        for url in urls:
            url = url.extract()
            regex = r'[0-9]{9}_(b|g|p|m)[0-9]{4}_(01|02|03|04)[0-9]{2}.(xlsx|xls)'

            if re.search(regex, url):
                url_path = url.split('.')

                # Create the url to download the file
                download_url = response.urljoin(url)

                # Create the name of the file
                file_path = url_path[0].split('/')
                file_name = '{}.{}'.format(file_path[len(file_path) - 1], url_path[1])
                path_to_save_file = '{}/{}/{}'.format('./files', str(self.name), file_name)

                # Download the file
                urllib.request.urlretrieve(download_url, path_to_save_file)

                # Save the data
                yield {
                    'file_name': file_name,
                    'page_url': download_url,
                }
