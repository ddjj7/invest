# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import Govinvest3Item

import time
from datetime import timedelta, datetime
import requests 
import json

count = 1

#山东
class Invest3Spider(scrapy.Spider):
    name = 'invest3'
    #allowed_domains = ['221.214.94.51:8081']
    start_urls = ['http://221.214.94.51:8081/icity/ipro/projectlist']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.Govinvest3Pipeline': 300},
    }

    def parse(self, response):
        global count
        endFlag='0'
        posturl = 'http://221.214.94.51:8081/icity/api-v2/app.icity.ipro.IproCmd/getProjectList'
        t = time.time()
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':'2'}, callback=self.parse)
        headers = {'Content-Type': 'application/json'}
        packet = {}
        packet['page'] = count
        packet['limit']=10
        packet['projectcode']=''
        packet['projectname']=''
        packet['contractor']=''
        packet['projecttype']=''
        data = json.dumps(packet)
        posturl = posturl+'?s=eb54861620379457861&t=7045_e72466_'+str(int(round(t * 1000)))
        r = requests.post(posturl, data=data, headers=headers)
        body = json.loads(r.text)
        for each in body['data']:
            item = Govinvest3Item()
            dict = {}
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
                endFlag='1'
                print('yesterday > recordDate')
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
            
            dict[u'项目代码'] = projectCode   #项目代码
            dict[u'项目名称'] = projectName   #项目名称
            dict[u'项目(法人)单位'] = enterpriseName  #项目(法人)单位
            dict[u'项目法人'] = contactName   #项目法人
            dict[u'项目阶段'] = u'已赋码'   #项目阶段  99=已赋码
            dict[u'seqId'] = seqId
            dict[u'项目类型'] = projectType  #项目类型
            dict[u'申报时间'] = applyDate   #申报时间
            item[u'dic']=dict
            yield item
            
        count +=1     
        if count<100 or endFlag=='0':
            print ('go next page ------------------------------'+str(count))
            time.sleep(5) 
            startUrl = 'http://221.214.94.51:8081/icity/ipro/projectlist'  #没用
            yield scrapy.FormRequest(startUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
            
