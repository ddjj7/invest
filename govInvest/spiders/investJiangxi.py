# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestJiangxiItem
import time
from datetime import timedelta, datetime
import json
import govInvest.cookieTools as cookieTool

#江西
class InvestJiangxiSpider(scrapy.Spider):
    sig = ''
    timestamp = ''
    tkey = ''
    count = 1
    name = 'investJiangxiSpider'
    #allowed_domains = ['tzxm.jxzwfww.gov.cn']
    start_urls = ['http://tzxm.jxzwfww.gov.cn/icity/ipro/open/publicity']
    api_url = 'http://tzxm.jxzwfww.gov.cn/icity/api-v2/jxtzxm.app.icity.ipro.IproCmd/getDisplayListByPage?s={sig}&t={timestamp}&o={tkey}'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestJiangxiPipeline': 300},
    }
    
    def start_requests(self):
        self.initVerifyParam()
        param = {'page': str(self.count), 'rows': "10", 'type': "0", 'projectName': "", 'projectCode': "-"}
        posturl = self.api_url.format(sig=self.sig,timestamp=self.timestamp,tkey=self.tkey)
        print(posturl)
        yield scrapy.FormRequest(posturl, formdata = param, callback=self.parse)

    def parse(self, response):
        print(response.text)
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        body = json.loads(response.text)
        for each in body['data']:
            each = each['columns']
            item = GovinvestJiangxiItem()
            investDict = {}
            finishDate = each['FINISH_TIME']
            recordDate = datetime.strptime(finishDate, "%Y-%m-%d")
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
            
            state = each['STATE']
            orgName = each['ORG_NAME']
            applySubject = each['APPLY_SUBJECT']
            itemId = each['ITEM_ID']
            projectCode = each['PROJECT_CODE']
            projectName = each['PROJECT_NAME']
            itemName = each['ITEM_NAME']
            submitTime = each['SUBMIT_TIME']/1000
            timearr = time.localtime(submitTime)
            subTime = time.strftime("%Y-%m-%d", timearr)
            timeLimt = each['TIME_LIMIT']/1000
            timearr = time.localtime(timeLimt)
            timeLmt = time.strftime("%Y-%m-%d", timearr)
            receiveNumber = each['RECEIVE_NUMBER']
            
            investDict[u'审批时间'] = finishDate   #审批时间
            investDict[u'状态'] = state   #状态
            investDict[u'ORG_NAME'] = orgName  #项目(法人)单位
            investDict[u'申请事项'] = applySubject   #申请事项
            investDict[u'ITEM_ID'] = itemId   #ITEM_ID
            investDict[u'项目代码'] = projectCode  #项目代码
            investDict[u'项目名称'] = projectName  #项目名称
            investDict[u'事项审批'] = itemName   #事项审批
            investDict[u'申请时间'] = subTime   #申请时间
            investDict[u'审批期限'] = timeLmt   #审批期限
            investDict[u'RECEIVE_NUMBER'] = receiveNumber  #RECEIVE_NUMBER
            item['dic']=investDict
            print(investDict)
            yield item
            
        self.count +=1     
        if self.count<50 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            posturl = self.api_url.format(sig=self.sig,timestamp=self.timestamp,tkey=self.tkey)
            #self.initVerifyParam()
            param = {'page': str(self.count), 'rows': "10", 'type': "0", 'projectName': "", 'projectCode': "-"}
#             print(posturl)
#             print(param)
            time.sleep(5) 
            yield scrapy.FormRequest(posturl, formdata = param, callback=self.parse)#,dont_filter=True
            
            
    def initVerifyParam(self):
        verifyParam = cookieTool.getJiangxiCookieParam(self.start_urls[0])
        self.sig = verifyParam[0]
        self.timestamp = verifyParam[1]
        self.tkey = verifyParam[2]       