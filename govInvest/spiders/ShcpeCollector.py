# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import os
import pdfplumber
from govInvest.items import ShcpeItem
from scrapy.http import JsonRequest
      
#import time
from datetime import datetime

count=0
#票据
class ShcpeSpider(scrapy.Spider):
    name = 'shcpeSpider'
    #allowed_domains = ['http://disclosure.shcpe.com.cn/']
    start_urls = ['http://disclosure.shcpe.com.cn/ent/public/article/list']
    detail_url = 'https://disclosure.shcpe.com.cn/ent/public/article/detail'
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.ShcpePipeline': 300},
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    
    def start_requests(self):
        payLoad = {'title': '', 'current': 1, 'size': 10, 'userType': 'ADMIN', 'typeCode': 'vip'}
        yield JsonRequest(self.start_urls[0], data=payLoad, headers=self.headers, callback=self.parse)

    def parse(self, response):
        print(response.text)
        body = json.loads(response.text)
        for each in body['data']['dataList']:
            print(each)
            createTime = each['createDate']
            recordDate = datetime.strptime(createTime, "%Y-%m-%d")
            print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            print(yesterday)
            if currDate == recordDate:
                print('currDate == recordDate')
                continue 
            if yesterday > recordDate:
                print('yesterday > recordDate')
                continue 
                
            articleId  = each['articleId']
            payLoad = {'articleId': articleId}
            yield JsonRequest(self.detail_url, data=payLoad, headers=self.headers, callback=self.get_detail)
            
            
    def get_detail(self,response):
        print(response.text)
        item = ShcpeItem()
        investDict = {}
        
        body = json.loads(response.text)
        data = body['data']
        articleId = data['articleId']
        title = data['title']
        summary = data['summary']
        createTime = data['createTime']
        attachments = data['attachments'][0]
        attachmentId = attachments['attachmentId']
        attachmentName = attachments['attachmentName']
        attachmentUrl = attachments['attachmentUrl']
        
        investDict[u'公告id'] = articleId
        investDict[u'标题'] = title
        investDict[u'概要'] = summary
        investDict[u'附件id'] = attachmentId  
        investDict[u'附件名称'] = attachmentName
        investDict[u'附件链接'] = attachmentUrl
        investDict[u'创建时间'] = createTime
        
        r = requests.get(attachmentUrl, headers=self.headers)
        fileName = articleId+'.pdf'
        with open(fileName,'wb') as f:
            f.write(r.content)
            f.close
            
        dataList = self.parseFile(fileName)
        investDict[u'dataList'] = dataList
        
        item['dic']=investDict
        return item
    
    def parseFile(self,file):
        path = os.path.abspath(file)
        
        dataList = []
        with pdfplumber.open(path) as pdf:
            for each in pdf.pages:
                table = each.extract_table()#提取单个表格
                count = 0
                for eachLine in table:
                    count+=1
                    if count == 1:
                        continue
                    dataList.append(eachLine)
        
        print(path)
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")
        
        return dataList
            
    if __name__ == '__main__':
        dataList = []
        with pdfplumber.open('/home/hewei/eclipse-workspace/govInvest/govInvest/A2022050868972048.pdf') as pdf:
            for each in pdf.pages:
                table = each.extract_table()#提取单个表格
                count = 0
                for eachLine in table:
                    count+=1
                    if count == 1:
                        continue
                    dataList.append(eachLine)
        print(len(dataList))
        print(dataList[0])
        print(dataList[2192])
                    
            
            
            
            
            
