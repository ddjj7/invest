# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestGuangdongItem

#import sys
import time
from datetime import timedelta, datetime
import requests

from scrapy.http.cookies import CookieJar

# reload(sys)
# sys.setdefaultencoding("utf-8")
  
#广东
class InvestGuangdongSpider(scrapy.Spider):
    count = 1
    cookie_jar = CookieJar()
    name = 'investGuangdongSpider'
    allowed_domains = ['www.gdtz.gov.cn']
    start_urls = ['https://www.gdtz.gov.cn/tybm/apply3!searchMore3.action?isCity=false&actionCityId=']
    detail_url = 'https://www.gdtz.gov.cn/tybm/apply3!applyView.action?id={id}'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestGuangdongPipeline': 300},
    }

    def parse(self, response):
#         cookie = response.headers.getlist('Set-Cookie')[0].split(';')[0]
#         print(cookie)
#         cookie1 = response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0].split("=")
#         print(cookie1)
        self.cookie_jar.extract_cookies(response, response.request)
        print(self.cookie_jar)
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #//*[@id="mainForm"]/div/div[2]/table/tbody/tr[3]
        for each in response.xpath("//*[@id='mainForm']/div/div[2]/table/tr"):
            projectId = each.xpath("./td[1]/text()").extract()
            if not projectId:
                continue
            projectId = projectId[0].strip()
            projectName = each.xpath("./td[2]/div/a/text()").extract()[0].strip()
            rawlink = each.xpath("./td[2]/div/a/@href").extract()[0].strip()
            link = 'https://www.gdtz.gov.cn'+rawlink
            process = each.xpath("./td[3]/div/text()").extract()[0].strip()
            state = each.xpath("./td[4]/text()").extract()[0].strip()
            date = each.xpath("./td[5]/div/text()").extract()[0].strip()
            print(projectId)
            print(projectName)
            print(link)
            print(process)
            print(state)
            print(date)
            time.sleep(0.3) 
            recordDate = datetime.strptime(date, "%Y-%m-%d")
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
            #do sth. here
            item = GovinvestGuangdongItem()
            investDict = {}
            investDict[u'项目编号'] = projectId
            investDict[u'项目名称'] = projectName
            investDict[u'进度'] = process
            investDict[u'状态'] = state
            investDict[u'备案通过日期'] = date
            item['dic']=investDict
            yield item
            #yield scrapy.Request(self.detail_url.format(id=projectId), callback=self.get_detail,meta={'cookiejar': self.cookie_jar})
        #https://www.gdtz.gov.cn/tybm/apply3!applyView.action?id=ff8080817b4f9304017b51d97f5f79f3
        #                       /tybm/apply3!applyView.action?id=ff8080817b35eb68017b37fd51f96b1a
        self.count +=1     
        if self.count<20 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            time.sleep(1)
            yield scrapy.FormRequest(self.start_urls[0], formdata = {'page.pageNo':str(self.count)},meta={'cookiejar': self.cookie_jar}, callback=self.parse)
            
            
    def get_detail(self,response):
        item = GovinvestGuangdongItem()
        cookie = response.headers.getlist('Set-Cookie')#[0].split(';')[0]
        print(cookie)
        print(response.text)
#         r = requests.get(response.url)
#         print(r.text)
        investDict = {}
#         projectCode = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[1]/text()").extract()[0]
#         projectCodeValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[2]/text()").extract())
#         projectName = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[3]/text()").extract()[0]
#         projectNameValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[4]/text()").extract())
#          
#         projectType = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[1]/text()").extract()[0]
#         projectTypeValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[2]/text()").extract())
#         projectLegelPerson = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[3]/text()").extract()[0]
#         projectLegelPersonValue = commonTool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[4]/text()").extract())
         
         
#         investDict[approveDepartment] = approveDepartmentValue
#         investDict[approveMatter] = approveMatterValue
#         investDict[approveResult] = approveResultValue
#         investDict[approveTime] = approveTimeValue
#         investDict[approveNo] = approveNoValue
        item['dic']=investDict
        return item
            
            
            
