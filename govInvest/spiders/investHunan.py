# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestHunanItem
from scrapy.http import JsonRequest
#import time
from datetime import timedelta, datetime
import json


#湖南
class InvestHunanSpider(scrapy.Spider):
    count = 1
    packet = {}
    name = 'investHunanSpider'
    allowed_domains = ['hntzxm.gov.cn']
    start_urls = ['http://www.hntzxm.gov.cn/public/public/information/homeList']
    downloadLink = 'http://www.hntzxm.gov.cn/public/public/common/download?id={fileGuid}'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestHunanPipeline': 300},
    }
    
    def start_requests(self):
        self.initPacket()
        yield JsonRequest(self.start_urls[0], data=self.packet, callback=self.parse)

    def parse(self, response):
        endFlag='0'
        body = json.loads(response.text)
        for each in body['data']['records']:
            item = GovinvestHunanItem()
            investDict = {}
            approvalDate = each['approvalDate']
            recordDate = datetime.strptime(approvalDate, "%Y-%m-%d")
            print(recordDate)
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
                
            pid  = each['id']
            projectName = each['prjName']   #项目名称
            projectCode = each['projectCode']  #项目代码
            approvalNum = each['approvalNum']  #批复文号
            fileGuid = each['fileGuid']  #文件id
            approvalDepartName = each['approvalDepartName']  #审批单位
            
            investDict[u'批复时间'] = approvalDate   #批复时间
            investDict[u'项目名称'] = projectName   #项目名称
            investDict[u'项目代码'] = projectCode   #项目代码
            investDict[u'批复文号'] = approvalNum   #批复文号
            investDict[u'审批单位'] = approvalDepartName   #审批单位
            investDict[u'id'] = pid  #项目id
            investDict[u'附件地址'] = self.downloadLink.format(fileGuid=fileGuid)  #附件地址
            
            item['dic']=investDict
            yield item
            
        self.count +=1     
        if self.count<3 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            self.packet['page'] = self.count
            yield JsonRequest(self.start_urls[0], data=self.packet, callback=self.parse)
            

    def initPacket(self):
        conditions = {'state': "1", 'publish': "1", 'finish': "1", 'keyword': ""}
        self.packet['conditions'] = conditions
        self.packet['pageIndex'] = 1
        self.packet['pageSize'] = 10
        self.packet['currentPage1'] = 1
        self.packet['currentPage2'] = 5
        self.packet['currentPage3'] = 5
        self.packet['currentPage4'] = 4
        