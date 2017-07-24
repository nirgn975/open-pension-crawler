import re
import time

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class OpenPensionCrawlSpiderBase(CrawlSpider):

    allowed_domains = []

    start_urls = []

    file_prefix = ''

    regex = ''

    rules = (
        # Extract 'href' and 'ng-href' links and parse them with the spider's method parse_item.
        Rule(LinkExtractor(attrs=['href', 'ng-href']), callback="parse_item", follow=True, ),
    )

    def parse_item(self, response):
        # Get all the href from the page.
        urls = response.xpath('//a/@href')

        # Loop through them and extract only the files urls.
        for url in urls:
            url = url.extract()

            if re.search(self.regex, url):
                url_path = url.split('.')

                # Create the url to download the file.

                # Fields:
                # url
                # fund_body
                # scrapped_date
                # quarter_and_year

                object = {
                    'url': response.urljoin(url),
                    'fund_body': self.name,
                    'scrapped_date': int(time.time()),
                }

                print(object)

                # Add the link into the DB.

