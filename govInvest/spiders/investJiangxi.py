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
            finishDate = each['FINISH_TIME']
            projectCode = each['PROJECT_CODE']
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
            
            detailUrl = 'http://tzxm.jxzwfww.gov.cn/icity/api-v2/jxtzxm.app.icity.ipro.IproCmd/getInvestInfoByCodeForOut?s={sig}&t={timestamp}&o={tkey}'
            detailUrl = detailUrl.format(sig=self.sig,timestamp=self.timestamp,tkey=self.tkey)
            time.sleep(5) 
            add_params = {}
            add_params['finishDate'] = finishDate
            yield scrapy.FormRequest(detailUrl, formdata = {'projectCode':projectCode}, callback=self.get_detail, cb_kwargs=add_params)
            
        self.count +=1     
        if self.count<50 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            posturl = self.api_url.format(sig=self.sig,timestamp=self.timestamp,tkey=self.tkey)
            #self.initVerifyParam()
            param = {'page': str(self.count), 'rows': "10", 'type': "0", 'projectName': "", 'projectCode': "-"}
            time.sleep(5) 
            yield scrapy.FormRequest(posturl, formdata = param, callback=self.parse)#,dont_filter=True
            
    def get_detail(self,response,finishDate):
        #print(response.text)
        body = json.loads(response.text)
        item = GovinvestJiangxiItem()
        investDict = {}
        projectCode = body['data']['projectCode']
        #print(projectCode)
        investDict[u'项目编号'] = projectCode
        projectName = body['data']['baseInfo']['projectName']
        #print(projectName)
        investDict['项目名称'] = projectName
        investDict['备案时间'] = finishDate
        #investDict['projectCode'] = projectCode
        divisionName = body['data']['baseInfo']['divisionName']
        investDict['建设项目所属区域'] = divisionName
        placeAreaDetail = body['data']['baseInfo']['placeAreaDetail']
        investDict['建设地点详情'] = placeAreaDetail
        try:
            address = body['data']['baseInfo']['address']
            investDict['详细地址'] = address
        except Exception as e:
            print(e)
        investment = body['data']['baseInfo']['investment']
        investDict['项目总投资'] = investment+'万元'
        projectContent = body['data']['baseInfo']['projectContent']
        investDict['建设规模及内容'] = projectContent
        enterpriseName = body['data']['baseInfo']['lerepInfo'][0]['enterpriseName']
        investDict['建设单位'] = enterpriseName
        startYear = body['data']['baseInfo']['startYear']
        investDict['开工时间'] = str(startYear)+'年'
        endYear = body['data']['baseInfo']['endYear']
        investDict['竣工时间'] = str(endYear)+'年'
        #projectContent = body['data']['baseInfo']['projectContent']
        projectType = body['data']['baseInfo']['projectType']
        projectTypeCn = ''
        if projectType=='A00001':
            projectTypeCn = '审批类'
        elif projectType=='A00002':
            projectTypeCn = '核准类'
        elif projectType=='A00003':
            projectTypeCn = '备案类'
        investDict['项目类型'] = projectTypeCn
        investDict['备案状态'] = '已备案'
        item['dic']=investDict
        return item
            
    def initVerifyParam(self):
        verifyParam = cookieTool.getJiangxiCookieParam(self.start_urls[0])
        self.sig = verifyParam[0]
        self.timestamp = verifyParam[1]
        self.tkey = verifyParam[2]       