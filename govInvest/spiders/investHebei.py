# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestHebeiItem
import govInvest.commonTools as commonTool
from datetime import timedelta, datetime
import re


#河北
class InvestHebeiSpider(scrapy.Spider):
    count = 1
    name = 'investHebeiSpider'
    packet = {}
    allowed_domains = ['tzxm.hbzwfw.gov.cn']
    start_urls = ['http://tzxm.hbzwfw.gov.cn/sbglweb/gsxxList']
    detail_url = 'http://tzxm.hbzwfw.gov.cn/sbglweb/xminfo?xmdm={xmdm}&sxid={sxid}&xzqh=130000'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestHebeiPipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    
    def start_requests(self):
        self.initPacket()
        yield scrapy.FormRequest(self.start_urls[0], formdata = self.packet, callback=self.parse,headers=self.headers)

    def parse(self, response):
        global count
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        #print(response.text)
        #//*[@id="form"]/table/tbody/tr[1]/td[6]
        for each in response.xpath("//*[@id='form']/table/tbody/tr"):
            date = each.xpath("./td[6]/text()").extract()[0].strip()
            print(date)
            recordDate = datetime.strptime(date, "%Y-%m-%d")
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
            #//*[@id="form"]/table/tbody/tr[1]/td[2]/a
            detailInfo = each.xpath("./td[2]/a/@href").extract()[0].strip()
            detail = re.findall(r'javascript:openXmInfo(.*);', detailInfo)[0]
            detailTup = eval(detail)
            #print(detailTup)
            detailUrl = self.detail_url.format(xmdm=detailTup[0],sxid=detailTup[1])
            print(detailUrl)
            yield scrapy.Request(detailUrl, callback=self.get_detail,headers=self.headers)
         
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        if self.count<50 and endFlag=='0':
            self.packet['page'] = str(self.count)
            yield scrapy.FormRequest(self.start_urls[0], formdata = self.packet,headers=self.headers, callback=self.parse)
             
    def get_detail(self,response):
        #print(response.text)
        item = GovinvestHebeiItem()
        investDict = {}
        #/html/body/table[2]/tbody/tr[1]/td[1]/b
        projectCode = response.xpath("/html/body/table[2]/tr[1]/td[1]/b/text()").extract()[0].strip()
        projectCodeValue = response.xpath("/html/body/table[2]/tr[1]/td[2]/text()").extract()[0].strip()
        projectName = response.xpath("/html/body/table[2]/tr[1]/td[3]/b/text()").extract()[0].strip()
        projectNameValue = response.xpath("/html/body/table[2]/tr[1]/td[4]/text()").extract()[0].strip()
        
        projectLegelPersonValue = ''
        projectTypeValue = ''
        if commonTool.returnNotNull(response.xpath("/html/body/table[2]/tr[2]/td[1]/b/text()")):
            projectType = response.xpath("/html/body/table[2]/tr[2]/td[1]/b/text()").extract()[0].strip()
        if commonTool.returnNotNull(response.xpath("/html/body/table[2]/tr[2]/td[2]/text()")):
            projectTypeValue = response.xpath("/html/body/table[2]/tr[2]/td[2]/text()").extract()[0].strip()
        if commonTool.returnNotNull(response.xpath("/html/body/table[2]/tr[2]/td[3]/b/text()")):
            projectLegelPerson = response.xpath("/html/body/table[2]/tr[2]/td[3]/b/text()").extract()[0].strip()
        if commonTool.returnNotNull(response.xpath("/html/body/table[2]/tr[2]/td[4]/text()")):
            c = response.xpath("/html/body/table[2]/tr[2]/td[4]/text()").extract()[0].strip()
        
         
        #//*[@id='itemInfos']/fieldset/table/tbody/tr/th[1]
        approveDepartment = response.xpath("/html/body/table[4]/tr[1]/td[1]/b/text()").extract()[0].strip()
        approveMatter = response.xpath("/html/body/table[4]/tr[1]/td[2]/b/text()").extract()[0].strip()
        approveResult = response.xpath("/html/body/table[4]/tr[1]/td[3]/b/text()").extract()[0].strip()
        approveTime = response.xpath("/html/body/table[4]/tr[1]/td[4]/b/text()").extract()[0].strip()
        approveNo = response.xpath("/html/body/table[4]/tr[1]/td[5]/b/text()").extract()[0].strip()
        
        #//*[@id='itemInfos']/fieldset/div[2]/table/tbody/tr/td[1]
        approveDepartmentValue = commonTool.returnNotNull(response.xpath("/html/body/table[4]/tr[2]/td[1]/text()").extract()).strip()
        approveMatterValue = commonTool.returnNotNull(response.xpath("/html/body/table[4]/tr[2]/td[2]/text()").extract()).strip()
        approveResultValue = commonTool.returnNotNull(response.xpath("/html/body/table[4]/tr[2]/td[3]/text()").extract()).strip()
        approveTimeValue =  commonTool.returnNotNull(response.xpath("/html/body/table[4]/tr[2]/td[4]/text()").extract()).strip()
        approveNoValue = commonTool.returnNotNull(response.xpath("/html/body/table[4]/tr[2]/td[5]/text()").extract()).strip()
        
        investDict[approveTime] = approveTimeValue  #审批时间
        investDict[projectName] = self.localStrip(projectNameValue)  #项目名称
        if projectLegelPersonValue:
            investDict[projectLegelPerson] = self.localStrip(projectLegelPersonValue)  #项目法人单位
        investDict[approveDepartment] = self.localStrip(approveDepartmentValue)  #审批部门
        investDict[projectCode] = self.localStrip(projectCodeValue)  #项目代码
        if projectTypeValue:
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
        
    def initPacket(self):
        self.packet['xzqh'] = '130000'
        self.packet['rows'] = '10'
        self.packet['page'] = '1'
        
        