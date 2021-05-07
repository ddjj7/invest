# # -*- coding: utf-8 -*-
# import scrapy
# from govInvest.items import GovinvestItem
#      
# import sys
# import time
# import datetime
# reload(sys)
# sys.setdefaultencoding("utf-8")
#   
# count = 0
#   
# class ItnvestSpider(scrapy.Spider):
#     name = 'invest'
#     allowed_domains = ['tzxm.ahzwfw.gov.cn']
#     start_urls = ['http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll']
#     custom_settings = {
#         'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestPipeline': 300},
#     }
#              
#     def parse(self, response):
#         global count
#         currentDate = ''
#         print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
#         for each in response.xpath("//*[@id='publicInformationForm']/tr"):
#             date = each.xpath("./td[5]/text()").extract()
#             rawlink = each.xpath("./td[1]/a[1]/@onclick").extract()
#             link = rawlink[0].replace('window.open(\'','http://tzxm.ahzwfw.gov.cn')
#             index = len(link)
#             link = link[0:index-2]
#             currentDate = date[0]
#             time.sleep(0.3) 
#             if datetime.datetime.strptime(currentDate, "%Y/%m/%d") < datetime.datetime.strptime('2021/04/01', "%Y/%m/%d"):
#                 break 
#             yield scrapy.Request(link, callback=self.get_detail)
#         
#         count +=1     
#         #currDate = datetime.datetime.strptime(currentDate, "%Y/%m/%d")
#         #print (currDate)
#         #if currDate > datetime.datetime.strptime('2021/05/15', "%Y/%m/%d"): 
#         print ('go next page ------------------------------'+str(count))
#         nextUrl = 'http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll'
#         if count<3:
#             yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
#             
#     def get_detail(self,response):
#         item = GovinvestItem()
#         dict = {}
#         
#         #//*[@id="tab00"]/div[1]/table/tbody/tr[1]/td[1]
#         projectCode = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[1]/text()").extract()[0]
#         projectCodeValue = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[2]/text()").extract()[0]
#         projectName = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[3]/text()").extract()[0]
#         projectNameValue = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[4]/text()").extract()[0]
#         
#         projectType = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[1]/text()").extract()[0]
#         projectTypeValue = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[2]/text()").extract()[0]
#         projectLegelPerson = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[3]/text()").extract()[0]
#         projectLegelPersonValue = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[4]/text()").extract()[0]
#         
#         dict[projectCode] = projectCodeValue
#         dict[projectName] = projectNameValue
#         dict[projectType] = projectTypeValue
#         dict[projectLegelPerson] = projectLegelPersonValue
#         
#         #//*[@id="tab00"]/div[2]/div[2]/table/tbody/tr[1]/td[1]
#         approveDepartment = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[1]/text()").extract()[0]
#         approveMatter = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[2]/text()").extract()[0]
#         approveResult = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[3]/text()").extract()[0]
#         approveTime = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[4]/text()").extract()[0]
#         approveNo = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[5]/text()").extract()[0]
#         
#         approveDepartmentValue = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[1]/text()").extract()[0]
#         approveMatterValue = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[2]/text()").extract()[0]
#         approveResultValue = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[3]/text()").extract()[0]
#         approveTimeValue =  response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[4]/text()").extract()[0]
#         approveNoValue = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[5]/span[1]/text()").extract()[0]
#         
#         dict[approveDepartment] = approveDepartmentValue
#         dict[approveMatter] = approveMatterValue
#         dict[approveResult] = approveResultValue
#         dict[approveTime] = approveTimeValue
#         dict[approveNo] = approveNoValue
#         item['dic']=dict
#         return item
#     
