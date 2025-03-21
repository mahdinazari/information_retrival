# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PopularityAnalysisItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    views = scrapy.Field()
    comments = scrapy.Field()
    source = scrapy.Field()
    