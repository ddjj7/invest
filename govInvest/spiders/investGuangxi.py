# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestGuangxiItem
from datetime import timedelta, datetime

#广西
class InvestGuangxiSpider(scrapy.Spider):
    count = 1
    name = 'investGuangxiSpider'
    packet = {}
    allowed_domains = ['zxsp.fgw.gxzf.gov.cn']
    start_urls = ['http://zxsp.fgw.gxzf.gov.cn/listRecordProjectPublicity.jspx?pageNo={num}&projectSearch=']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestGuangxiPipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    
    def start_requests(self):
        startUrl = self.start_urls[0].format(num=self.count)
        yield scrapy.Request(startUrl,headers=self.headers, callback=self.parse)

    def parse(self, response):
        global count
        innerLine = 0
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        print ('$$$$$$$$$$$$$$$$$$'+str(innerLine)+'$$$$$$$$$$$$$$$$$$')
        #print(response.text)
        #print(response.xpath("//*[@id='listRecordPublicityForm']/div/div[5]/div[2]/div[3]/div/table/tr").extract())
        #//*[@id="listRecordPublicityForm"]/div/div[5]/div[2]/div[3]/div/table/tbody/tr[2]/td[1]
        for each in response.xpath("//*[@id='listRecordPublicityForm']/div/div[5]/div[2]/div[3]/div/table/tr"):
            item = GovinvestGuangxiItem()
            investDict = {}
            innerLine +=1
            if innerLine == 1 or innerLine == 12:
                continue
            projectName = each.xpath("./td[2]/text()").extract()[0].strip() #项目名称
            #print(projectName)
            date = each.xpath("./td[6]/text()").extract()[0].strip()
            print(date)
            tempDate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
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
            
            projectCode = each.xpath("./td[1]/text()").extract()[0].strip() #项目代码
            projectName = each.xpath("./td[2]/text()").extract()[0].strip() #项目名称
            projectLegel = each.xpath("./td[3]/text()").extract()[0].strip() #法人单位
            approveDepartment = each.xpath("./td[4]/text()").extract()[0].strip() #备案部门
            status = each.xpath("./td[5]/text()").extract()[0].strip() #备案状态
            
            investDict['备案时间'] = date  #备案时间
            investDict['项目名称'] = projectName  #项目名称
            investDict['法人单位'] = projectLegel  #法人单位
            investDict['项目代码'] = projectCode  #项目代码
            investDict['备案部门'] = approveDepartment  #备案部门
            investDict['备案状态'] = status  #备案状态
            item['dic']=investDict
            yield item
         
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        if self.count<4 and endFlag=='0':
            nextUrl = self.start_urls[0].format(num=self.count)
            yield scrapy.Request(nextUrl,headers=self.headers, callback=self.parse)
             
        
        