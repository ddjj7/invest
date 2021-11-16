# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestHubeiItem

#import time
from datetime import timedelta, datetime
import json


#湖北
class InvestHubeiSpider(scrapy.Spider):
    count = 1
    name = 'investHubeiSpider'
    allowed_domains = ['tzxm.hubei.gov.cn']
    start_urls = ['http://tzxm.hubei.gov.cn/portalopenapprovalResult.do?method=recordquery']
    detail_url = 'http://tzxm.hubei.gov.cn/portalopenapprovalResult.do?method=recordContentQuery'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestHubeiPipeline': 300},
    }
    
    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls[0], formdata = {'pageNo':str(self.count)}, callback=self.parse)

    def parse(self, response):
        endFlag='0'
        body = json.loads(response.text)
        for each in body[0]['list']:
            state = each['state']
            if not state == r'已审核通过':
                continue
            apply_time = each['apply_time']
            projectuuid = each['projectuuid']
            print(projectuuid)
            recordDate = datetime.strptime(apply_time, "%Y-%m-%d")
            print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                print('currDate == recordDate')
                continue 
            if yesterday > recordDate:
                endFlag='1'
                print('yesterday > recordDate')
                continue 
            yield scrapy.FormRequest(self.detail_url, formdata = {'projectuuid':projectuuid}, callback=self.get_detail)
            
        self.count +=1     
        if self.count<100 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            #time.sleep(5) 
            yield scrapy.FormRequest(self.start_urls[0], formdata = {'pageNo':str(self.count)}, callback=self.parse)
            

    def get_detail(self,response):
        item = GovinvestHubeiItem()
        investDict = {}
        
        body = json.loads(response.text)[0]
        deal_code = body['deal_code']
        #result = body['result']
        apply_time = body['apply_time']
        scale_content = body['scale_content']
        cor_type = body['cor_type']
        address_detial = body['address_detial']
        state = body['state']
        internet_mode = body['internet_mode']
        #is_foreign = body['is_foreign']
        project_dept = body['project_dept']
        contact = body['contact']
        project_type = body['project_type']
        #item_person = body['item_person']
        #catalog_code = body['catalog_code']
        project_starttime = body['project_starttime']
        #introduction_use = body['introduction_use']
        apply_project_name = body['apply_project_name']
        construction_mode = body['construction_mode']
        projectuuid = body['projectuuid']
        total_money = body['total_money']
        industry_name = body['industry_name']
        
        investDict[u'申请日期'] = apply_time
        investDict[u'项目名称'] = apply_project_name
        investDict[u'单位名称'] = project_dept
        investDict[u'项目法人/项目业主'] = contact  #项目法人/项目业主
        investDict[u'项目代码'] = deal_code
        investDict[u'建设地点'] = address_detial
        investDict[u'申报单位经济类型'] = cor_type
        investDict[u'项目所属行业'] = industry_name
        investDict[u'项目总投资（万元）'] = total_money
        investDict[u'建设性质'] = project_type
        investDict[u'计划开工时间'] = project_starttime
        investDict[u'审核状态'] = state
        investDict[u'主要建设规模及内容'] = scale_content
        
        
        
#         investDict[u'上网模式'] = internet_mode
#         investDict[u'建设模式'] = construction_mode
#         investDict[u'projectuuid'] = projectuuid
        
        
        item['dic']=investDict
        return item
