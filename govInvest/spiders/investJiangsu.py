# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestJiangsuItem

#import sys
#import time
from datetime import timedelta, datetime

import govInvest.commonTools as tool
# reload(sys)
# sys.setdefaultencoding("utf-8")
  
count = 0

#江苏
class InvestJiangsuSpider(scrapy.Spider):
    name = 'investJiangsuSpider'
    #allowed_domains = ['222.190.131.17:8075']
    #jszwfw.com.cn
    start_urls = ['http://222.190.131.17:8075/portalopenPublicInformation.do?method=querybeianExamineAll']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestJiangsuPipeline': 300},
    }

    def parse(self, response):
        global count
        endFlag='0'
        nextUrl = 'http://222.190.131.17:8075/portalopenPublicInformation.do?method=querybeianExamineAll'
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #/html/body/div[7]/div/div/div/div[3]/ul/table/tbody/tr[2]
        for each in response.xpath("//*[@id='publicInformationForm']/tr"):
            item = GovinvestJiangsuItem()
            investDict = {}
            date = each.xpath("./td[5]/text()").extract()[0]
            #time.sleep(0.3) 
            recordDate = datetime.strptime(date, "%Y/%m/%d")
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
            title = tool.returnNotNull(each.xpath("./td[1]/@title").extract())
            name = tool.returnNotNull(each.xpath("./td[2]/text()").extract())
            department = tool.returnNotNull(each.xpath("./td[3]/text()").extract())
            code = tool.returnNotNull(each.xpath("./td[4]/text()").extract())
            date = tool.returnNotNull(each.xpath("./td[5]/text()").extract())
#             if len(resultno)>0:
#                 resultno = resultno[0]
#             else:
#                 resultno = 'null'
            investDict[u'备案时间'] = date    #备案时间
            investDict[u'项目名称'] = title    #项目名称
            investDict[u'申报单位名称'] = name   #申报单位名称
            investDict[u'备案机关'] = department   #备案机关
            investDict[u'备案证号'] = code    #备案证号
            
            item['dic']=investDict
            yield item
            
        count +=1     
        if count<100 and endFlag=='0':
            print ('go next page ------------------------------'+str(count))
            #time.sleep(5)
            yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
            
