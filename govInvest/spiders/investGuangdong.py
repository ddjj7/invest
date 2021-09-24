# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestGuangdongItem

#import sys
#import time
from datetime import timedelta, datetime
import govInvest.commonTools as commonTool

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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    def parse(self, response):
        headers = self.headers
#         cookie1 = response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(",")[0].split(";")[0].split("=")[1]
#         cookie2 = response.headers.getlist('Set-Cookie')[1].decode("utf-8").split(",")[0].split(";")[0].split("=")[1]
#         headers['cookie']= 'JSESSIONID='+cookie1+";__jsluid_s="+cookie2
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #//*[@id="mainForm"]/div/div[2]/table/tbody/tr[3]
        for each in response.xpath("//*[@id='mainForm']/div/div[2]/table/tr"):
            projectId = each.xpath("./td[1]/text()").extract()
            if not projectId:
                continue
            projectId = projectId[0].strip()
            #projectName = each.xpath("./td[2]/div/a/text()").extract()[0].strip()
            rawlink = each.xpath("./td[2]/div/a/@href").extract()[0].strip()
            link = 'https://www.gdtz.gov.cn'+rawlink
            #process = each.xpath("./td[3]/div/text()").extract()[0].strip()
            #state = each.xpath("./td[4]/text()").extract()[0].strip()
            date = each.xpath("./td[5]/div/text()").extract()[0].strip()
            print(date)
            #time.sleep(0.3) 
            recordDate = datetime.strptime(date, "%Y-%m-%d")
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            if currDate == recordDate:
                print('currDate == recordDate')
                continue 
            if yesterday > recordDate:
                endFlag='1'
                continue 
                print('yesterday > recordDate')
            
            #time.sleep(5)
            yield scrapy.Request(link, callback=self.get_detail,headers=headers)
        self.count +=1     
        if self.count<100 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            #time.sleep(5)
            yield scrapy.FormRequest(self.start_urls[0], formdata = {'page.pageNo':str(self.count)},headers=headers, callback=self.parse)
            
            
    def get_detail(self,response):
        #print(response.text)
        item = GovinvestGuangdongItem()
        investDict = {}
        projectCode = response.xpath("//*[@id='hytab']/tr[2]/td[1]/text()").extract()[0]
        projectCodeValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[2]/td[2]/text()").extract())
        projectName = response.xpath("//*[@id='hytab']/tr[3]/td[1]/text()").extract()[0]
        projectNameValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[3]/td[2]/text()").extract())
        projectPlace = response.xpath("//*[@id='hytab']/tr[4]/td[1]/text()").extract()[0]
        projectPlaceValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[4]/td[2]/text()").extract())
        projectInvest = response.xpath("//*[@id='hytab']/tr[5]/td[1]/text()").extract()[0]
        projectInvestValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[5]/td[2]/text()").extract())
        projectContent = response.xpath("//*[@id='hytab']/tr[6]/td[1]/text()").extract()[0]
        projectContentValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[6]/td[2]/text()").extract())
        enterpriseName = response.xpath("//*[@id='hytab']/tr[7]/td[1]/text()").extract()[0]
        enterpriseNameValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[7]/td[2]/text()").extract())
        examineUnit = response.xpath("//*[@id='hytab']/tr[8]/td[1]/text()").extract()[0]
        examineUnitValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[8]/td[2]/text()").extract())
        approveDate = response.xpath("//*[@id='hytab']/tr[9]/td[1]/text()").extract()[0]
        approveDateValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[9]/td[2]/text()").extract())
        finishDate = response.xpath("//*[@id='hytab']/tr[10]/td[1]/text()").extract()[0]
        finishDateValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[10]/td[2]/text()").extract())
        period = response.xpath("//*[@id='hytab']/tr[11]/td[1]/text()").extract()[0]
        periodValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[11]/td[2]/text()").extract())
        projectStat = response.xpath("//*[@id='hytab']/tr[12]/td[1]/text()").extract()[0]
        projectStatValue = commonTool.returnNotNull(response.xpath("//*[@id='hytab']/tr[12]/td[2]/text()").extract())
        
        investDict[approveDate] = approveDateValue  #备案申报日期
        investDict[projectName] = projectNameValue  #项目名称
        investDict[enterpriseName] = enterpriseNameValue  #建设单位
        investDict[projectCode] = projectCodeValue  #备案项目编号
        investDict[projectPlace] = projectPlaceValue  #项目所在地
        investDict[projectInvest] = projectInvestValue  #项目总投资
        investDict[projectContent] = projectContentValue  #项目规模及内容
        investDict[examineUnit] = examineUnitValue  #备案机关
        investDict[finishDate] = finishDateValue  #复核通过日期    
        investDict[period] = periodValue  #项目起止年限    
        investDict[projectStat] = projectStatValue  #项目当前状态
        print(investDict)
        item['dic']=investDict
        return item
            
            
            
