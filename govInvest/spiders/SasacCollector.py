# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import SasacItem
      
#import time
from datetime import timedelta, datetime

count=0
#网信
class SasacSpider(scrapy.Spider):
    name = 'SasacSpider'
    allowed_domains = ['http://www.sasac.gov.cn/']
    start_urls = ['http://www.sasac.gov.cn/n2588035/n2641579/n2641645/index.html']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.SasacPipeline': 300},
    }
    
    #只取第一页，这个网站所有列表都只有一页
    def parse(self, response):
        item = SasacItem()
        docDict = {}
        nameList = []
        print(response.xpath("/html/body/div[4]/div[2]/table/tr/td/div/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a/text()").extract())
        for each in response.xpath("/html/body/div[4]/div[2]/table/tr/td/div/div/div[2]/table/tbody/tr/td/table/tbody/tr"):
            name1 = each.xpath("./td[2]/a/text()").extract()
            name2 = each.xpath("./td[5]/a/text()").extract()
            print(name1)
            print(name2)
            if name1:
                nameList.append(name1)
            if name2:
                nameList.append(name2)
        docDict['nameList'] = nameList
        item['dic']=docDict
        yield item
         
             
