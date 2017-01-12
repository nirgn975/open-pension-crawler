import scrapy
import urllib.request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class JilinLapidotSpider(CrawlSpider):
    name = 'jilin_lapidot'
    allowed_domains = ['yl-invest.co.il']
    start_urls = ['http://www.yl-invest.co.il']
    rules = (
        # Extract 'href' and 'ng-href' links and parse them with the spider's method parse_item
        Rule(LinkExtractor(attrs=['href', 'ng-href']), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        files_extension = ['doc', 'docx', 'xls', 'xlsx']

        # Get all the href from the page
        urls = response.xpath('//a/@href')

        # Loop throgh them and extract only the files urls
        for url in urls:
            url = url.extract()
            url_path = url.split('.')
            if len(url_path) == 2 and url_path[1] in files_extension:
                # Create the url to download the file
                download_url = response.urljoin(url)

                # Create the name of the file
                file_path = url_path[0].split('/')
                file_name = '{}.{}'.format(file_path[len(file_path) - 1], url_path[1])
                path_to_save_file = '{}/{}/{}'.format('./files', 'yl', file_name)

                # # Download the file
                urllib.request.urlretrieve(download_url, path_to_save_file)

                # Save the data
                yield {
                    'file_name': file_name,
                    'page_url': download_url,
                }
