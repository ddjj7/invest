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
    start_urls = ['https://tzxm.shaanxi.gov.cn/tzxmspweb/api/admin/service/sbsp/apprtprojectinfo/phgsBacx?sort=updateDate&order=desc&pageNo={num}&pageSize=10']
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
            #print(each)
            item = GovinvestShaanxiItem()
            investDict = {}
            applyDate = each['applyTime']
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
            if len(projectName)<5:
                print(projectName)
                continue
            projectLegel = each['projectDept']   #法人单位
            contactName = each['contact']   #项目法人
            projectCode = each['dealCode']   #项目代码
            addressDetial = each['addressDetial']   #建设地点
            corType = each['corTypeText']   #申报单位经济类型
            industryName = each['industryName']   #项目所属行业
            totalMoney = each['totalMoney']   #项目总投资
            projectType = each['projectType']   #建设性质
            projectStarttime = each['projectStarttime']   #计划开工时间
            state = each['stateTxt']   #审核状态
            scaleContent = each['scaleContent']   #建设规模及内容
            
            
            investDict[u'申报时间'] = applyDate   #申报时间
            investDict[u'项目名称'] = projectName   #项目名称
            investDict[u'法人单位'] = projectLegel  #法人单位
            investDict[u'项目法人'] = contactName   #项目法人
            investDict[u'项目代码'] = projectCode   #项目代码
            investDict[u'建设地点'] = addressDetial   #建设地点
            investDict[u'申报单位经济类型'] = corType   #申报单位经济类型
            investDict[u'项目所属行业'] = industryName   #项目所属行业
            if totalMoney:
                investDict[u'项目总投资'] = str(totalMoney)+u'万'  #项目总投资
            investDict[u'建设性质'] = projectType   #建设性质
            investDict[u'计划开工时间'] = projectStarttime   #计划开工时间
            investDict[u'审核状态'] = state   #审核状态
            investDict[u'建设规模及内容'] = scaleContent   #建设规模及内容
            item['dic']=investDict
            yield item
            
        self.count +=1     
        if self.count<5 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            nextUrl = self.start_urls[0].format(num=self.count)
            yield scrapy.Request(nextUrl,headers=self.headers, callback=self.parse)
             
        
        