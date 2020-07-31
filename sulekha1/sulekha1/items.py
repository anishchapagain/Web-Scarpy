# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Sulekha1Item(scrapy.Item):
    roomtitle = scrapy.Field()
    Available_From = scrapy.Field()
    post_by = scrapy.Field()
    location = scrapy.Field()
    rental = scrapy.Field()
    bedrooms = scrapy.Field()
    size = scrapy.Field()
    description = scrapy.Field()
    # name = scrapy.Field()
    
    # define the fields for your item here like:
    # name = scrapy.Field()
#     offer=scrapy.Field()
#     room_location=scrapy.Field()
#     post_hr=scrapy.Field()
#     post_by=scrapy.Field()
#  #   # Available_From=scrapy.Field()
#     # Ad_Type=scrapy.Field()
#     Rental=scrapy.Field()
#     # Bedrooms =scrapy.Field()
#     # bedrooms=scrapy.Field()
#     # bathrooms=scrapy.Field()
#     # sizes_sqft=scrapy.Field()
#     Details=scrapy.Field()
#     prize_per_month=scrapy.Field()
#     University_nearby=scrapy.Field()

