# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestShandongItem
from scrapy.http import JsonRequest
from datetime import timedelta, datetime
import govInvest.cookieTools as cookieTool
import json

#山东
class InvestShandongSpider(scrapy.Spider):
    sig = ''
    timestamp = ''
    count = 1
    packet = {}
    name = 'investShandongSpider'
    #allowed_domains = ['221.214.94.51:8081']
    posturl = 'http://221.214.94.51:8081/icity/api-v2/app.icity.ipro.IproCmd/getProjectList?s={sig}&t={timestamp}'
    #sdzwfw.com.cn
    start_urls = ['http://221.214.94.51:8081/icity/ipro/projectlist']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestShandongPipeline': 300},
    }

    def start_requests(self):
        self.initVerifyParam()
        self.initParam()
        posturl = self.posturl.format(sig=self.sig,timestamp=self.timestamp)
        yield JsonRequest(posturl, data=self.packet, callback=self.parse)

    def parse(self, response):
        print(response.text)
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        body = json.loads(response.text)
        for each in body['data']:
            item = GovinvestShandongItem()
            investDict = {}
            applyDate = each['APPLY_DATE']
            recordDate = datetime.strptime(applyDate, "%Y-%m-%d")
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                print('currDate == recordDate')
                continue 
            if yesterday > recordDate:
                print('yesterday > recordDate')
                endFlag='1'
                continue 
            
            projectCode = each['PROJECT_CODE']
            projectName = each['PROJECT_NAME']
            enterpriseName = each['ENTERPRISE_NAME']
            if len(enterpriseName)<5:
                continue
            
            contactName = each['CONTACT_NAME']
            status = each['STATUS']
            if status !='99':
                continue
            
            seqId = each['SEQ_ID']
            projectType = each['PROJECT_TYPE']
            if projectType == 'A00001':
                projectType = u'审批类项目'
            elif projectType == 'A00002':
                projectType = u'核准类项目'
            elif projectType == 'A00003':
                projectType= u'备案类项目'
            
            investDict[u'申报时间'] = applyDate   #申报时间
            investDict[u'项目名称'] = projectName   #项目名称
            investDict[u'项目(法人)单位'] = enterpriseName  #项目(法人)单位
            investDict[u'项目法人'] = contactName   #项目法人
            investDict[u'项目代码'] = projectCode   #项目代码
            investDict[u'项目阶段'] = u'已赋码'   #项目阶段  99=已赋码
            investDict[u'seqId'] = seqId
            investDict[u'项目类型'] = projectType  #项目类型
            
            item['dic']=investDict
            yield item
            
        self.count +=1     
        if self.count<50 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            self.packet['page'] = self.count
            self.initVerifyParam()
            posturl = self.posturl.format(sig=self.sig,timestamp=self.timestamp)
            print(posturl)
            yield JsonRequest(posturl, data=self.packet, callback=self.parse)
            
             
    def initVerifyParam(self):
        verifyParam = cookieTool.getShandongCookieParam(self.start_urls[0])
        self.sig = verifyParam[0]
        self.timestamp = verifyParam[1]
        
    def initParam(self):
        self.packet['page'] = 1
        self.packet['limit'] = 10
        self.packet['projectcode'] = ''
        self.packet['projectname'] = ''
        self.packet['contractor'] = ''
        self.packet['projecttype'] = ''
