# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GovinvestAnhuiItem(scrapy.Item):
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

class GovinvestJiangsuItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestShandongItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestHubeiItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestGuangdongItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestJiangxiItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestZhejiangItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestFujianItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestHunanItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestHenanItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestHebeiItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestBeijingItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestGuangxiItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class GovinvestShaanxiItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class MpsItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class CacItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class CbircItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class MiitItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class SasacItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class ShcpeItem(scrapy.Item):
    dic = scrapy.Field()
    pass

class BeikeItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    position = scrapy.Field()
    info = scrapy.Field()
    tag = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()
    pass