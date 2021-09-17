# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import BeikeItem
import time

   
endFlag = '0'
headers = None

class BeikeSpider(scrapy.Spider):
    name = 'beikeSpider'
    count = 1
    allowed_domains = ['sh.ke.com']
    start_urls = ['https://sh.ke.com/ershoufang/yangpu/p4/']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.BeikeXlsxPipeline': 300},
    }
    
    
    
    def parse(self, response):
        global endFlag
        endFlag = '0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #//*[@id='beike']/div[1]/div[4]/div[1]/div[4]/ul
        print(response.xpath("//*[@id='beike']/div[1]/div[4]/div[1]/div[4]/ul"))
        for each in response.xpath("//li[@class='clear']"):
            title = each.xpath("./div[1]/div[1]/a/@title").extract()[0].strip().replace(' ','')
            print(title)
            link = each.xpath("./div[1]/div[1]/a/@href").extract()[0].strip().replace(' ','')
            print(link)
            position = each.xpath("./div[1]/div[2]/div[1]/div/a/text()").extract()[0].strip().replace(' ','')
            print(position)
            #//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li[1]/div[1]/div[2]/div[2]/text()
            info = each.xpath("./div[1]/div[2]/div[2]").xpath('string(.)').extract()[0].strip().replace(' ','')
            print(info)
            tag = each.xpath("./div[1]/div[2]/div[4]").xpath('string(.)').extract()[0].strip().replace(' ','')
            print(tag)
            totalPrice = each.xpath("./div[1]/div[2]/div[5]/div[1]/span/text()").extract()[0].strip().replace(' ','')
            print(totalPrice)
            unitPrice = each.xpath("./div[1]/div[2]/div[5]/div[2]/span/text()").extract()[0].strip().replace(' ','')
            print(unitPrice)
            print(30*"*")
            item = BeikeItem()
            item['title']=title
            item['link']=link
            item['position']=position
            item['info']=info
            item['tag']=tag
            item['totalPrice']=totalPrice
            item['unitPrice']=unitPrice
            yield item
            #yield scrapy.Request(link, callback=self.get_detail,headers=headers,cb_kwargs=add_params)
         
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        if self.count<12 and endFlag=='0':
            nextUrl = 'https://sh.ke.com/ershoufang/yangpu/pg{count}p4'.format(count=self.count)
            time.sleep(5)
            yield scrapy.Request(nextUrl, callback=self.parse)
            
             
    # def get_detail(self,response,date,title,link):
    #     item = BeikeItem()
    #     docDict = {}
    #
    #     text = ''
    #     #//*[@id="ztdx"]
    #     for each in response.xpath("//*[@id='ztdx']"):
    #         text = each.xpath("./p").xpath('string(.)').extract()
    #         #print(title)
    #         print(text)
    #     docDict['date'] = date
    #     docDict['title'] = title
    #     docDict['link'] = link
    #     docDict['text'] = text
    #     item['dic']=docDict
    #     time.sleep(5)
    #     return item
    #

    
    
     
