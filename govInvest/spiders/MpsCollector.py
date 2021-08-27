# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from govInvest.items import GovinvestMpsItem
      
import time
from datetime import timedelta, datetime

import govInvest.cookieTools as cookieTool

   
#count = 1
endFlag = '0'
headers = None

#公安
class MpsSpider(scrapy.Spider):
    name = 'mpsSpider'
    count = 0
    allowed_domains = ['www.mps.gov.cn']
    start_urls = ['https://www.mps.gov.cn/n6557558/index.html']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestMpsPipeline': 300},
    }
    
    def start_requests(self):
        global headers
        if not headers:
            headers = cookieTool.getMpsHeaderWithCookie(self.start_urls[0])
        yield Request(self.start_urls[0],headers=headers, callback=self.parse)
    
              
    def parse(self, response):
        #global count
        global endFlag
        endFlag = '0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #//*[@id="comp_7574611"]/ul/li[1]/a
        #print(response.xpath("//*[@id='comp_7574611']/ul/li"))
        #print(response.text)
        for each in response.xpath("//*[@id='comp_7574611']/ul/li"):
            #//*[@id="comp_7574611"]/ul/li[1]/span
            date = each.xpath("./span/text()").extract()[0]
            print(date)
            title = each.xpath("./a/text()").extract()[0]
            print(title)
            rawlink = each.xpath("./a/@href").extract()[0]
            #print(rawlink)
            link = rawlink.replace('..','https://www.mps.gov.cn')
            print(link)
            #time.sleep(0.5) 
            recordDate = datetime.strptime(date, "%Y-%m-%d")
            #print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
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
            yield scrapy.Request(link, callback=self.get_detail,headers=headers,cb_kwargs=add_params)
         
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        urlPattern = 'https://www.mps.gov.cn/n6557558/index_7574611_{num}.html'
        nextUrl = urlPattern.format(num=self.count)
        print(nextUrl)
        if self.count<2 or endFlag=='0':
            #pass
            time.sleep(5)
            yield scrapy.Request(nextUrl, callback=self.parse_second,headers=headers)
            
    def parse_second(self,response):
        #/html/body/ul/li[10]
        for each in response.xpath("//html/body/ul/li"):
            date = each.xpath("./span/text()").extract()[0]
            print(date)
            title = rawlink = each.xpath("./a/text()").extract()[0]
            print(title)
            rawlink = each.xpath("./a/@href").extract()[0]
            link = rawlink.replace('..','https://www.mps.gov.cn')
            print(link)
            add_params = {}
            add_params['date'] = date
            add_params['title'] = title
            add_params['link'] = link
            yield scrapy.Request(link, callback=self.get_detail,headers=headers,cb_kwargs=add_params)
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        urlPattern = 'https://www.mps.gov.cn/n6557558/index_7574611_{num}.html'
        nextUrl = urlPattern.format(num=self.count)
        print(nextUrl)
        if self.count<10 and endFlag=='0':
            #pass
            time.sleep(5)
            yield scrapy.Request(nextUrl, callback=self.parse_second,headers=headers)
             
    def get_detail(self,response,date,title,link):
        item = GovinvestMpsItem()
        docDict = {}
         
        texts = []
        #//*[@id="ztdx"]
        #print(response.text)
        for each in response.xpath("//*[@id='ztdx']"):
            text = each.xpath("./p").xpath('string(.)').extract()
            texts.append(text)
        docDict['date'] = date
        docDict['title'] = title
        docDict['link'] = link
        print(date)
        print(title)
        print(texts)
        docDict['text'] = texts
        item['dic']=docDict
        #time.sleep(5)
        return item
    
    
    
     
