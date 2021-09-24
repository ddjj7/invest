# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import CacItem
      
#import time
from datetime import timedelta, datetime

count=0
#网信
class CacSpider(scrapy.Spider):
    name = 'cacSpider'
    allowed_domains = ['www.cac.gov.cn']
    start_urls = ['http://www.cac.gov.cn/zcfg/fl/A090901index_1.htm',
                  'http://www.cac.gov.cn/zcfg/xzfg/A090902index_1.htm',
                  'http://www.cac.gov.cn/zcfg/bmgz/A090903index_1.htm',
                  'http://www.cac.gov.cn/zcfg/sfjs/A090904index_1.htm',
                  'http://www.cac.gov.cn/zcfg/gfxwj/A090905index_1.htm',
                  'http://www.cac.gov.cn/zcfg/zcwj/A090906index_1.htm']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.CacPipeline': 300},
    }
    
    #只取第一页，这个网站所有列表都只有一页
    def parse(self, response):
        global count
        #endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #print(response.xpath("//*[@id='pageName2']"))
        
        for each in response.xpath("//*[@id='hideData']/li"):
            articleType = response.xpath("//*[@id='pageName2']/text()").extract()[0].strip()
            print(articleType)
            date = each.xpath("./span/text()").extract()[0]
            print(date)
            title = each.xpath("./h3/a/text()").extract()[0]
            print(title)
            link = each.xpath("./h3/a/@href").extract()[0]
            print(link)
            recordDate = datetime.strptime(date, "%Y-%m-%d")
            print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            print(yesterday)
            if currDate == recordDate:
                print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                print('yesterday > recordDate')
                #endFlag='1'
                #continue 
            add_params = {}
            add_params['date'] = date
            add_params['title'] = title
            add_params['link'] = link
            add_params['articleType'] = articleType
            #time.sleep(5)
            yield scrapy.Request(link, callback=self.get_detail,cb_kwargs=add_params)
         
#         count +=1     
#         if count<200 and endFlag=='0':
#             pass
#         print ('go next page ------------------------------'+str(count))
             
    def get_detail(self,response,date,title,link,articleType):
        item = CacItem()
        docDict = {}
        text = ''
        for each in response.xpath("//*[@id='BodyLabel']"):
            text = each.xpath("./p").xpath('string(.)').extract()
            #print(text)
        docDict['date'] = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S")
        docDict['title'] = title
        docDict['link'] = link
        docDict['typeOne'] = '政策法规'
        docDict['typeTwo'] = articleType
        docDict['content'] = text
        item['dic']=docDict
        #time.sleep(5) 
        return item
        
        
    
    
    
     
