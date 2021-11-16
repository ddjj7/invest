# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestFujianItem
      
#import sys
#import time
from datetime import timedelta, datetime

import govInvest.commonTools as commonTool

#福建
class InvestFujianSpider(scrapy.Spider):
    count = 1
    name = 'investFujianSpider'
    allowed_domains = ['fj.tzxm.gov.cn']
    start_urls = ['https://fj.tzxm.gov.cn/eap/credit.showProjectInfo']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestFujianPipeline': 300},
    }
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
    
    def start_requests(self):
        global headers
        yield scrapy.FormRequest(self.start_urls[0], formdata = {'page':str(self.count)},headers=self.headers, callback=self.parse)
              
    def parse(self, response):
        global count
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #print(response.text)
        for each in response.xpath("//*[@id='tb']/tbody/tr"):
            trid = commonTool.returnNotNull(each.xpath("./@id"))
            if trid != None:
                continue
            name = each.xpath("./td[1]/text()").extract()[0].strip()
            print(name)
            date = each.xpath("./td[4]/text()").extract()[0].strip()
            print(date)
            recordDate = datetime.strptime(date, "%Y-%m-%d")
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
            projectcode = each.xpath("./td[2]/text()").extract()[0].strip()
            detailUrl = 'https://fj.tzxm.gov.cn/eap/credit.publicShow?projectcode='+projectcode+'&biaoji=0'
            add_params = {}
            add_params['applyDate'] = date
            yield scrapy.Request(detailUrl, callback=self.get_detail,headers=self.headers,cb_kwargs=add_params)
         
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        if self.count<3 and endFlag=='0':
            yield scrapy.FormRequest(self.start_urls[0], formdata = {'page':str(self.count)},headers=self.headers, callback=self.parse)
             
    def get_detail(self,response,applyDate):
        item = GovinvestFujianItem()
        investDict = {}
        projectCode = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[1]/td[1]/text()").extract()[0].strip()
        projectCodeValue = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[1]/td[2]/text()").extract()[0].strip()
        projectName = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[1]/td[3]/text()").extract()[0].strip()
        projectNameValue = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[1]/td[4]/text()").extract()[0].strip()
        
        projectType = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[2]/td[1]/text()").extract()[0].strip()
        projectTypeValue = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[2]/td[2]/text()").extract()[0].strip()
        projectLegelPerson = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[2]/td[3]/text()").extract()[0].strip()
        projectLegelPersonValue = response.xpath("//*[@id='aout_div']/fieldset/div/table/tbody/tr[1]/td[1]/text()").extract()[0].strip()
        
        applyCode = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[3]/td[1]/text()").extract()[0].strip()
        applyCodeValue = response.xpath("//*[@id='step_2']/fieldset/table/tbody/tr[3]/td[2]/text()").extract()[0].strip()
         
         
        #//*[@id='itemInfos']/fieldset/table/tbody/tr/th[1]
        approveDepartment = response.xpath("//*[@id='itemInfos']/fieldset/table/tbody/tr/th[1]/text()").extract()[0].strip()
        approveMatter = response.xpath("//*[@id='itemInfos']/fieldset/table/tbody/tr/th[2]/text()").extract()[0].strip()
        approveNo = response.xpath("//*[@id='itemInfos']/fieldset/table/tbody/tr/th[3]/text()").extract()[0].strip()
        approveResult = response.xpath("//*[@id='itemInfos']/fieldset/table/tbody/tr/th[4]/text()").extract()[0].strip()
        approveTime = response.xpath("//*[@id='itemInfos']/fieldset/table/tbody/tr/th[5]/text()").extract()[0].strip()
        
        #//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[1]
        approveDepartmentValue = commonTool.returnNotNull(response.xpath("//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[1]/text()").extract())
        approveMatterValue = commonTool.returnNotNull(response.xpath("//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[2]/text()").extract())
        approveNoValue = commonTool.returnNotNull(response.xpath("//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[3]/text()").extract())
        approveResultValue = commonTool.returnNotNull(response.xpath("//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[4]/text()").extract())
        approveTimeValue =  commonTool.returnNotNull(response.xpath("//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[5]/text()").extract())
        
        
        investDict['申请时间'] = applyDate  #申请时间
        investDict[projectName] = self.localStrip(projectNameValue)  #项目名称
        investDict[projectLegelPerson] = self.localStrip(projectLegelPersonValue)  #项目法人单位
        investDict[approveTime] = self.localStrip(approveTimeValue)  #审批时间
        investDict[applyCode] = self.localStrip(applyCodeValue)  #报建编号
        investDict[approveDepartment] = self.localStrip(approveDepartmentValue)  #审批部门
        investDict[projectCode] = self.localStrip(projectCodeValue)  #项目代码
        investDict[projectType] = self.localStrip(projectTypeValue)  #项目类型
        investDict[approveMatter] = self.localStrip(approveMatterValue)  #审批事项
        investDict[approveResult] = self.localStrip(approveResultValue)  #审批结果
        investDict[approveNo] = self.localStrip(approveNoValue)  #审批文号
        item['dic']=investDict
        return item
    
    def localStrip(self,localStr):
        if localStr == None:
            return ''
        else:
            return localStr.strip()
    
    
