# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SulekhaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    Event_Name = scrapy.Field()
    # Event_day = scrapy.Field()
    # Event_month=scrapy.Field()
    Date = scrapy.Field()
    Title = scrapy.Field()
    
