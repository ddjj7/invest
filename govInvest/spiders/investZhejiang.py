# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestZhejiangItem
from datetime import timedelta, datetime
import govInvest.cookieTools as cookieTool
import json

#浙江
class InvestZhejiangSpider(scrapy.Spider):
    name = 'investZhejiangSpider'
    allowed_domains = ['tzxm.zjzwfw.gov.cn']
    start_urls = ['https://tzxm.zjzwfw.gov.cn/tzxmweb/zwtpages/resultsPublicity/notice_of_publicity_new.html?page=1']
    posturl = 'https://tzxm.zjzwfw.gov.cn/publicannouncement.do?method=queryItemList_new'
    pdfurl = 'https://tzxm.zjzwfw.gov.cn/publicannouncement.do?method=downFile&sendid={sendid}&flag=0'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestZhejiangPipeline': 300},
    }
    headers={
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        #'cookie': 'JSESSIONID='+cookiedict['JSESSIONID']+'; SERVERID='+cookiedict['SERVERID'],
        'referer': 'https://tzxm.zjzwfw.gov.cn/tzxmweb/zwtpages/resultsPublicity/notice_of_publicity_new.html?page=1',
        'sec-fetch-mode': 'cors',
        "sec-fetch-site": 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    count = 0
    packet = {}
    JSESSIONID = ''
    SERVERID = ''

    def start_requests(self):
        self.initVerifyParam()
        self.initParam()
        yield scrapy.FormRequest(self.posturl, formdata = self.packet, callback=self.parse,headers=self.headers)
              
    def parse(self, response):
        endFlag='0'
        print(response.text)
        print ('$$$$$$$$$$$$$$$$$$'+str(self.count)+'$$$$$$$$$$$$$$$$$$')
        body = json.loads(response.text)
        for each in body[0]['itemList']:
            item = GovinvestZhejiangItem()
            investDict = {}
            date = each['DEAL_TIME']
            recordDate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            if currDate == recordDate:
                print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                print('yesterday > recordDate')
                #endFlag='1'
                #continue 
            
            investDict['办理时间'] = each['DEAL_TIME']  #办理时间
            investDict['项目名称'] = each['apply_project_name']  #项目名称
            investDict['项目代码'] = each['deal_code']  #项目代码
            investDict['审批监管事项'] = each['ITEM_NAME']  #审批监管事项
            investDict['办理状态'] = each['DEAL_NAME']  #办理状态
            investDict['管理部门'] = each['DEPT_NAME']  #管理部门
            investDict['projectuuid'] = each['projectuuid']  
            investDict['SENDID'] = each['SENDID']  
            investDict['备案pdf'] = self.pdfurl.format(sendid=each['SENDID'])
            item['dic']=investDict
            yield item
         
        self.count +=1     
        print ('go next page ------------------------------'+str(self.count))
        if self.count<4 and endFlag=='0':
            self.packet['pageNo']= str(self.count)
            yield scrapy.FormRequest(self.posturl, formdata = self.packet, callback=self.parse,headers=self.headers)
             
#     def get_detail(self,response):
#         item = GovinvestZhejiangItem()
#         investDict = {}
#          
#         investDict[approveTime] = approveTimeValue  #审批时间
#         investDict[projectName] = projectNameValue  #项目名称
#         investDict[projectLegelPerson] = projectLegelPersonValue  #项目法人单位
#         investDict[approveDepartment] = approveDepartmentValue  #审批部门
#         investDict[projectCode] = projectCodeValue  #项目代码
#         investDict[projectType] = projectTypeValue  #项目类型
#         investDict[approveMatter] = approveMatterValue  #审批事项
#         investDict[approveResult] = approveResultValue  #审批结果
#         investDict[approveNo] = approveNoValue  #审批文号
#         item['dic']=investDict
#         return item
    
    def initVerifyParam(self):
        cookieDict = cookieTool.getZhejiangCookieParam(self.start_urls[0])
        self.JSESSIONID = cookieDict['JSESSIONID']
        self.SERVERID = cookieDict['SERVERID']
        self.headers['cookie'] = 'JSESSIONID='+self.JSESSIONID+'; SERVERID='+self.SERVERID
        print(self.headers)
        
    def initParam(self):
        self.packet['pageFlag'] = '1'
        self.packet['pageNo']= str(self.count)
        self.packet['area_code']= ''
        self.packet['area_flag']= '1'
        self.packet['deal_code']= ''
        self.packet['item_name']= ''
#         self.packet['Txtidcode']= ''
    
