# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestBeijingItem
      
#import sys
#import time
from datetime import timedelta, datetime
import json
from scrapy import item

#福建
class InvestBeijingSpider(scrapy.Spider):
    count = 1
    packet = {}
    name = 'investBeijingSpider'
    allowed_domains = ['tzxm.beijing.gov.cn']
    start_urls = ['http://tzxm.beijing.gov.cn/information/projectData']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestBeijingPipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    
    def start_requests(self):
        self.initPacket()
        yield scrapy.FormRequest(self.start_urls[0], formdata = self.packet, headers=self.headers, callback=self.parse)
              
    def parse(self, response):
        endFlag='0'
        body = json.loads(response.text)
        print(response.text)
        for each in body['page']['list']:
            item = GovinvestBeijingItem()
            investDict = {}
            applyDate = each['APPROVALDATE']
            recordDate = datetime.strptime(applyDate, "%Y-%m-%d")
            print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            if currDate == recordDate:
                print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                print('yesterday > recordDate')
                endFlag='1'
                #continue 
            pid = each['ID']
            projectZY = each['PROJECTCODE_ZY']
            projectName = each['PROJECTNAME']
            projectCode = each['PROJECTCODE']
            consunit = each['CONSUNIT']
            pyType = each['PJTYPE']
            orgName = each['ORGNAME']
            createTime = each['CREATE_TIME']
            
            investDict['立项时间'] = applyDate  #立项时间
            investDict['项目名称'] = projectName  #项目名称
            investDict['项目单位'] = consunit  #项目单位
            investDict['id'] = pid  #id
            investDict['国家编码'] = projectZY  #国家编码
            investDict['项目代码'] = projectCode  #项目代码
            investDict['立项类型'] = pyType  #立项类型
            investDict['立项单位'] = orgName  #立项单位
            investDict['公示时间'] = createTime  #公示时间
            item['dic']=investDict
            yield item
            
        self.count +=1     
        if self.count<32 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            self.packet['pageNo'] = str(self.count)
            yield scrapy.FormRequest(self.start_urls[0], formdata = self.packet, headers=self.headers, callback=self.parse)
                 
        
    def initPacket(self):
        self.packet['recordsperpage'] = '10'
        self.packet['pageNo'] = '1'
        self.packet['projectCode'] = ''
        self.packet['selElement'] = '0'
        self.packet['isPPP'] = '0'
    
    
