from pathlib import Path
import re
import urllib.request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class OpenPensionCrawlSpiderBase(CrawlSpider):

    allowed_domains = []

    start_urls = []

    file_prefix = ''

    regex = ''

    rules = (
        # Extract 'href' and 'ng-href' links and parse them with the spider's method parse_item.
        Rule(LinkExtractor(attrs=['href', 'ng-href']), callback="parse_item", follow=True),
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
                download_url = response.urljoin(url)

                # Create the name of the file.
                file_path = url_path[0].split('/')
                file_name = self.file_prefix + '{}.{}'.format(file_path[len(file_path) - 1], url_path[1])
                folder = '{}/{}'.format('./files', str(self.name))
                path_to_save_file = '{}/{}'.format(folder, file_name)
                Path(folder).mkdir(parents=True, exist_ok=True)

                # Download the file.
                try:
                    urllib.request.urlretrieve(download_url, path_to_save_file)
                except TimeoutError as error:
                    print(error)

                # Save the data.
                yield {
                    'file_name': file_name,
                    'page_url': download_url,
                }
