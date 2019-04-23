# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class News(scrapy.Item):
    oid = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    website = scrapy.Field()
    publish_at = scrapy.Field()
    comment_count = scrapy.Field()
    personid = scrapy.Field()

