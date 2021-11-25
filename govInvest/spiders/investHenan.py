# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestHenanItem
from scrapy.http import Request
from datetime import timedelta, datetime

  
#河南
class InvestHenanSpider(scrapy.Spider):
    count = 1
    name = 'investHenanSpider'
    allowed_domains = ['tzls.hazw.gov.cn']
    #jszwfw.com.cn
    start_urls = ['http://tzls.hazw.gov.cn/jggs.jspx?apply_date_begin=2017-01-31&pageNo={count}']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestHenanPipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    
    def start_requests(self):
        url = self.start_urls[0].format(count=self.count)
        yield Request(url,headers=self.headers, callback=self.parse)

    def parse(self, response):
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #//*[@id="tableForm"]/table/tbody/tr[2]/td[5]
        for each in response.xpath("//*[@id='tableForm']/table/tr"):
            item = GovinvestHenanItem()
            investDict = {}
            dateEle = each.xpath("./td[5]/text()")
            if not dateEle:
                continue
            date = each.xpath("./td[5]/text()").extract()[0].strip()
            recordDate = datetime.strptime(date, "%Y-%m-%d")
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
                
            projectName = each.xpath("./td[2]/text()").extract()[0].strip()   #项目名称
            projectCode = each.xpath("./td[1]/span/text()").extract()[0].strip()  #项目代码
            approveMatter = each.xpath("./td[3]/text()").extract()[0].strip()  #审批事项
            approveResult = each.xpath("./td[4]/text()").extract()[0].strip()  #审批结果
            
            investDict[u'审批时间'] = date    #审批时间
            investDict[u'项目名称'] = projectName    #项目名称
            investDict[u'项目代码'] = projectCode   #申报单位名称
            investDict[u'审批事项'] = approveMatter   #审批事项
            investDict[u'审批结果'] = approveResult    #审批结果
            
            item['dic']=investDict
            yield item
            
        self.count +=1     
        if self.count<100 and endFlag=='0':
            print ('go next page ------------------------------'+str(self.count))
            nextUrl = self.start_urls[0].format(count=self.count)
            yield Request(nextUrl,headers=self.headers, callback=self.parse)
            
