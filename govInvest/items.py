# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Govinvest1Item(scrapy.Item):
    # define the fields for your item here like:
#     department = scrapy.Field()
#     result = scrapy.Field()
#     matter = scrapy.Field()
#     title = scrapy.Field()
#     date = scrapy.Field()
#     rawlink = scrapy.Field()
#     link = scrapy.Field()
    dic = scrapy.Field()
    pass

class Govinvest2Item(scrapy.Item):
    dic = scrapy.Field()
    pass

class Govinvest3Item(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestMpsItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestCacItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestCbircItem(scrapy.Item):
    dic = scrapy.Field()
    pass


