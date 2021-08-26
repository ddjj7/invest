# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import Govinvest2Item

#import sys
import time
from datetime import timedelta, datetime

import govInvest.commonTools as tool
# reload(sys)
# sys.setdefaultencoding("utf-8")
  
count = 0

#江苏
class Invest2Spider(scrapy.Spider):
    name = 'invest2'
    #allowed_domains = ['222.190.131.17:8075']
    start_urls = ['http://222.190.131.17:8075/portalopenPublicInformation.do?method=querybeianExamineAll']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.Govinvest2Pipeline': 300},
    }

    def parse(self, response):
        global count
        endFlag='0'
        nextUrl = 'http://222.190.131.17:8075/portalopenPublicInformation.do?method=querybeianExamineAll'
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':'2'}, callback=self.parse)
        for each in response.xpath("//*[@id='publicInformationForm']/tr"):
            item = Govinvest2Item()
            dict = {}
            date = each.xpath("./td[7]/text()").extract()[0]
            time.sleep(0.3) 
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
            matter = tool.returnNotNull(each.xpath("./td[2]/text()").extract())
            department = tool.returnNotNull(each.xpath("./td[3]/text()").extract())
            district = tool.returnNotNull(each.xpath("./td[4]/text()").extract())
            result = tool.returnNotNull(each.xpath("./td[5]/text()").extract())
            if result !=u'批复':
                continue
            resultno = tool.returnNotNull(each.xpath("./td[6]/text()").extract())
#             if len(resultno)>0:
#                 resultno = resultno[0]
#             else:
#                 resultno = 'null'
            dict[u'项目名称'] = title    #项目名称
            dict[u'审批事项'] = matter   #审批事项
            dict[u'审批部门'] = department   #审批部门
            dict[u'部门区划'] = district    #部门区划
            dict[u'审批结果'] = result    #审批结果
            dict[u'批复文号'] = resultno   #批复文号
            dict[u'审批时间'] = date    #审批时间
            item['dic']=dict
            yield item
            
        count +=1     
        if count<100 and endFlag=='0':
            print ('go next page ------------------------------'+str(count))
            yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
            
