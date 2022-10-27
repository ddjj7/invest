# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestGuangdongItem
#import time
from scrapy.http import Request
from datetime import timedelta, datetime
import json

#广东
class InvestGuangdongSpider(scrapy.Spider):
    count = 1
    packet = {}
    name = 'investGuangdongSpider'
    #allowed_domains = ['tzxm.jxzwfww.gov.cn']
    start_urls = ['https://gd.tzxm.gov.cn/tzxmspweb/api/publicityInformation/selectByPageBA']
    detail_url = 'https://gd.tzxm.gov.cn/tzxmspweb/api/publicityInformation/selectBaProjectInfo'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestJiangxiPipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    def start_requests(self):
        self.initParam()
        print(self.payload)
        yield Request(self.start_urls[0], method="POST", body=json.dumps(self.payload), headers=self.headers, callback=self.parse)

    def parse(self, response):
        print(response.text)
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        body = json.loads(response.text)
        for each in body['data']['list']:
            finishDate = each['finishDate']
            baId = each['baId']
            recordDate = datetime.strptime(finishDate, "%Y-%m-%d")
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
            
            #time.sleep(5) 
            param = {'baId':baId}
            yield Request(self.detail_url, method="POST", body=json.dumps(param), headers=self.headers, callback=self.get_detail)
            
        self.count +=1     
        if self.count<100 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            self.initParam()
            yield Request(self.start_urls[0], method="POST", body=json.dumps(self.payload), headers=self.headers, callback=self.parse)
            
    def get_detail(self,response):
        print(response.text)
        body = json.loads(response.text)
        item = GovinvestGuangdongItem()
        investDict = {}
        proofOrSerialCode = body['data']['proofOrSerialCode'] #备案项目编号
        projectName = body['data']['projectName'] #项目名称
        place = body['data']['place'] #项目所在地
        totalInvest = body['data']['totalInvest'] #项目总投资
        scope = body['data']['scope'] #项目规模及内容
        applyOrgan = body['data']['applyOrgan'] #建设单位
        fullName = body['data']['fullName'] #备案机关
        submitDate = body['data']['submitDate'] #备案申报日期
        finishDate = body['data']['finishDate'] #复核通过日期
        beginDate = body['data']['beginDate'] #项目起年限
        overDate = body['data']['overDate'] #项目止年限
        stateFlagName = body['data']['stateFlagName'] #项目当前状态
        
        investDict[u'项目名称'] = projectName
        investDict[u'建设单位'] = applyOrgan
        investDict[u'备案项目编号'] = proofOrSerialCode
        investDict[u'建设项目所属区域'] = place
        investDict[u'备案机关'] = fullName
        investDict[u'项目总投资'] = str(totalInvest)+u'万元'
        investDict[u'建设规模及内容'] = scope
        investDict[u'备案申报日期'] = submitDate
        investDict[u'复核通过日期'] = finishDate
        investDict[u'项目起年限'] = beginDate
        investDict[u'项目止年限'] = overDate
        investDict[u'项目当前状态'] = stateFlagName
        item['dic']=investDict
        return item
            
    def initParam(self):
        self.payload = {
        "city": '',
        "flag": 1,
        "nameOrCode": '',
        "pageNumber": self.count,
        "pageSize": 15
    }
        
