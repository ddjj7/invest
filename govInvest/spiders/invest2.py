# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import Govinvest2Item

#import sys
import time
import datetime
# reload(sys)
# sys.setdefaultencoding("utf-8")
  
count = 0

class Invest2Spider(scrapy.Spider):
    name = 'invest2'
    #allowed_domains = ['222.190.131.17:8075']
    start_urls = ['http://222.190.131.17:8075/portalopenPublicInformation.do?method=queryExamineAll']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.Govinvest2Pipeline': 300},
    }

    def parse(self, response):
        global count
        currentDate = ''
        nextUrl = 'http://222.190.131.17:8075/portalopenPublicInformation.do?method=queryExamineAll'
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':'2'}, callback=self.parse)
        for each in response.xpath("//*[@id='publicInformationForm']/tr"):
            item = Govinvest2Item()
            dict = {}
            date = each.xpath("./td[7]/text()").extract()[0]
            currentDate = date
            time.sleep(0.3) 
            if datetime.datetime.strptime(currentDate, "%Y/%m/%d") < datetime.datetime.strptime('2021/04/01', "%Y/%m/%d"):
                break 
            #do sth. here
            title = each.xpath("./td[1]/@title").extract()[0]
            matter = each.xpath("./td[2]/text()").extract()[0]
            department = each.xpath("./td[3]/text()").extract()[0]
            district = each.xpath("./td[4]/text()").extract()[0]
            result = each.xpath("./td[5]/text()").extract()[0]
            resultno = each.xpath("./td[6]/text()").extract()
            if len(resultno)>0:
                resultno = resultno[0]
            else:
                resultno = 'null'
            dict[u'项目名称'] = title
            dict[u'审批事项'] = matter
            dict[u'审批部门'] = department
            dict[u'部门区划'] = district
            dict[u'审批结果'] = result
            dict[u'批复文号'] = resultno
            dict[u'审批时间'] = date
            item['dic']=dict
            yield item
            
        count +=1     
        if count <3:
            print ('go next page ------------------------------'+str(count))
            yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
            
