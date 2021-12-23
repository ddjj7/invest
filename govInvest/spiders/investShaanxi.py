# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestShaanxiItem
from datetime import timedelta, datetime
import json

#陕西
class InvestShaanxiSpider(scrapy.Spider):
    count = 1
    name = 'investShaanxiSpider'
    packet = {}
    allowed_domains = ['tzxm.shaanxi.gov.cn']
    start_urls = ['https://tzxm.shaanxi.gov.cn/tzxmspweb/api/admin/service/sbsp/apprtprojectinfo/selectApprtProjectInfoByDealState?pageSize=10&pageNo={num}']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestShaanxiPipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    
    def start_requests(self):
        startUrl = self.start_urls[0].format(num=self.count)
        yield scrapy.Request(startUrl,headers=self.headers, callback=self.parse)

    def parse(self, response):
        print(response.text)
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        body = json.loads(response.text)
        for each in body['data']['objList']:
            each = each['items'][0]
            #print(each)
            item = GovinvestShaanxiItem()
            investDict = {}
            applyDate = each['approvalDate']
            print(applyDate)
            tempDate = datetime.strptime(applyDate, "%Y-%m-%d %H:%M:%S")
            recordDate = datetime.strptime(tempDate.strftime("%Y-%m-%d"), "%Y-%m-%d")
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
            
            projectName = each['applyProjectName']   #项目名称
            itemName = each['itemName']   #事项名称
            #projectUuid = each['projectUuid']   #id
            dealDeptName = each['dealDeptName']   #审批部门
            projectCode = each['dealCode']   #项目代码
            obtainresult = each['obtainresult']   #批复结果
            
            investDict[u'申报时间'] = applyDate   #申报时间
            investDict[u'项目名称'] = projectName   #项目名称
            investDict[u'事项名称'] = itemName  #事项名称
            investDict[u'项目代码'] = projectCode   #项目代码
            investDict[u'审批部门'] = dealDeptName   #审批部门
            if obtainresult == '1':
                investDict[u'批复结果'] = u'批复'   #批复结果
            
            item['dic']=investDict
            yield item
            
        self.count +=1     
        if self.count<4 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            nextUrl = self.start_urls[0].format(num=self.count)
            yield scrapy.Request(nextUrl,headers=self.headers, callback=self.parse)
             
        
        