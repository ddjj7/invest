# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from govInvest.items import GovinvestAnhuiItem
      
#import sys
#import time
from datetime import timedelta, datetime

import govInvest.commonTools as commonTool
import govInvest.cookieTools as cookieTool

# reload(sys)
# sys.setdefaultencoding("utf-8")
   
count = 0
headers = None

#安徽 
class InvestAnhuiSpider(scrapy.Spider):
    name = 'investAnhuiSpider'
    allowed_domains = ['tzxm.ahzwfw.gov.cn']
    start_urls = ['http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestAnhuiPipeline': 300},
    }
    
    def start_requests(self):
        global headers
        if not headers:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
            #cookie有效期半小时
            #headers = cookieTool.getAHHeaderWithCookie(self.start_urls[0])
        yield Request(self.start_urls[0],headers=headers, callback=self.parse)
              
    def parse(self, response):
        global count
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #print(response.text)
        for each in response.xpath("//*[@id='publicInformationForm']/tr"):
            date = each.xpath("./td[5]/text()").extract()[0]
            result = each.xpath("./td[4]/text()").extract()[0]
            rawlink = each.xpath("./td[1]/a[1]/@onclick").extract()[0]
            link = rawlink.replace('window.open(\'','http://tzxm.ahzwfw.gov.cn')
            index = len(link)
            link = link[0:index-2]
            #time.sleep(0.3) 
            recordDate = datetime.strptime(date, "%Y/%m/%d")
            #print(recordDate)
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
            if result !=u'批复':
                continue
            #time.sleep(5)
            yield scrapy.Request(link, callback=self.get_detail,headers=headers)
         
        count +=1     
        #currDate = datetime.datetime.strptime(currentDate, "%Y/%m/%d")
        #print (currDate)
        #if currDate > datetime.datetime.strptime('2021/05/15', "%Y/%m/%d"): 
        print ('go next page ------------------------------'+str(count))
        nextUrl = 'http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll'
        if count<100 and endFlag=='0':
            #time.sleep(5)
            yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse,headers=headers)
             
    def get_detail(self,response):
        item = GovinvestAnhuiItem()
        investDict = {}
         
        #print(response.text)
        #//*[@id="tab00"]/div[1]/table/tbody/tr[1]/td[1]
        projectCode = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[1]/text()").extract()[0]
        projectCodeValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[2]/text()").extract())
        projectName = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[3]/text()").extract()[0]
        projectNameValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[4]/text()").extract())
         
        projectType = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[1]/text()").extract()[0]
        projectTypeValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[2]/text()").extract())
        projectLegelPerson = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[3]/text()").extract()[0]
        projectLegelPersonValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[4]/text()").extract())
         
        #//*[@id="tab00"]/div[2]/div[2]/table/tbody/tr[1]/td[1]
        approveDepartment = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[1]/text()").extract()[0]
        approveMatter = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[2]/text()").extract()[0]
        approveResult = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[3]/text()").extract()[0]
        approveTime = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[4]/text()").extract()[0]
        approveNo = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[5]/text()").extract()[0]
         
        approveDepartmentValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[1]/text()").extract())
        approveMatterValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[2]/text()").extract())
        approveResultValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[3]/text()").extract())
        approveTimeValue =  commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[4]/text()").extract())
        approveNoValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[5]/span[1]/text()").extract())
        
        investDict[approveTime] = approveTimeValue  #审批时间
        investDict[projectName] = projectNameValue  #项目名称
        investDict[projectLegelPerson] = projectLegelPersonValue  #项目法人单位
        investDict[approveDepartment] = approveDepartmentValue  #审批部门
        investDict[projectCode] = projectCodeValue  #项目代码
        investDict[projectType] = projectTypeValue  #项目类型
        investDict[approveMatter] = approveMatterValue  #审批事项
        investDict[approveResult] = approveResultValue  #审批结果
        investDict[approveNo] = approveNoValue  #审批文号
        item['dic']=investDict
        return item
    
    
    
