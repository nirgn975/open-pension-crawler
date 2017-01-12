# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpenPensionCrawlerItem(scrapy.Item):
    # The fields for out item
    file_name = scrapy.Field()
    page_url = scrapy.Field()
