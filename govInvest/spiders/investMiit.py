# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from govInvest.items import GovinvestMpsItem
      
import time
import requests
import re
import json
from datetime import timedelta, datetime
from bs4 import BeautifulSoup

import govInvest.cookieTools as cookieTool

   
endFlag = '0'
headers = None

#工信
class ItnvestMpsSpider(scrapy.Spider):
    name = 'investMiit'
    zcjdCount = 1
    wjgsCount = 1
    allowed_domains = ['www.miit.gov.cn']
    listUrl = 'https://www.miit.gov.cn/api-gateway/jpaas-publish-server/front/page/build/unit'
    start_urls = ['https://www.miit.gov.cn/zwgk/wjgs/index.html',
                  'https://www.miit.gov.cn/zwgk/zcjd/index.html']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestMpsPipeline': 300},
    }
    
    def start_requests(self):
        global headers
        if not headers:
            headers = cookieTool.getMpsHeaderWithCookie(self.start_urls[0])
        for url in self.start_urls:
            yield Request(url,headers=headers, callback=self.parse)
        #yield Request(self.start_urls[0],headers=headers, callback=self.parse)
    
              
    def parse(self, response):
        global endFlag
        endFlag = '0'
        print(response.url)
        if 'wjgs' in response.url:
            count = self.wjgsCount 
            self.wjgsCount+=1
        if 'zcjd' in response.url:
            count = self.zcjdCount 
            self.zcjdCount+=1
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        authorizedReadUnitId = re.findall(r'authorizedReadUnitId = "(.*)";', response.text)[0]
        path = '//*[@id="{authId}"]/@querydata'.format(authId=authorizedReadUnitId)
        strParams = response.xpath(path)[0].extract()
        dictParams = eval(strParams)
        paramJson = '{"pageNo":'+str(count)+',"pageSize":"24"}'
        dictParams['paramJson'] = paramJson
        print(dictParams)
        
        r = requests.get(self.listUrl, headers=headers, params=dictParams)
        body = json.loads(r.text)
        strHtml = body['data']['html']
        pageSoup = BeautifulSoup(strHtml,'html.parser')
        lis = pageSoup.find_all('li', class_='cf')
        for item in lis:
            date = item.find('span').text
            rawlink = item.find('a').get('href')
            title = item.find('a').text
            print(date)
            print(title)
            link = 'https://www.miit.gov.cn'+rawlink
            #print(link)
            recordDate = datetime.strptime(date, "%Y-%m-%d")
            #print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                pass
                #print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                pass
                #print('yesterday > recordDate')
                #endFlag='1'
                #continue 
            add_params = {}
            add_params['date'] = date
            add_params['title'] = title
            add_params['link'] = link
            #yield scrapy.Request(link, callback=self.get_detail,headers=headers,cb_kwargs=add_params)
          
        if count<4 and endFlag=='0':
            print ('go next page ------------------------------'+str(count))
            time.sleep(5)
            yield scrapy.Request(response.url+'?a='+str(count), callback=self.parse,headers=headers)
            
             
    def get_detail(self,response,date,title,link):
        item = GovinvestMpsItem()
        docDict = {}
        #print(response.text)
        text = ''
        for each in response.xpath("//*[@id='con_con']"):
            text = each.xpath("./p").xpath('string(.)').extract()
            #print(text)
        docDict['date'] = date
        #print(date)
        docDict['title'] = title
        #print(title)
        docDict['link'] = link
        docDict['text'] = text
        item['dic']=docDict
        time.sleep(5)
        return item
    
    
    
     
