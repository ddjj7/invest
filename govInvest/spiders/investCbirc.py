# -*- coding: utf-8 -*-
import scrapy
from govInvest.items import GovinvestCbircItem
      
import json
import re
import time
from datetime import timedelta, datetime
from scrapy.http import HtmlResponse

#银保监
class ItnvestCbircSpider(scrapy.Spider):
    name = 'investCbirc'
    allowed_domains = ['www.cbirc.gov.cn']
    #start手动改一下页码，做个铺底
    start_urls = ['https://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=927,pageIndex=1,pageSize=18.json',
                  'https://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=928,pageIndex=1,pageSize=18.json']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.GovinvestCbircPipeline': 300},
    }
    
    #只取第一页
    def parse(self, response):
        global count
        zcfg=0
        print(response.text)
        print(response.url)
        body = json.loads(response.text)
        itemId = re.findall(r'data_itemId=(.*?),pageIndex', response.url)[0]
        print(itemId)
        for each in body['data']['rows']:
            docId = each['docId']
            print(docId)
            publishDate = each['publishDate']
            print(publishDate)
            urlPattern = 'https://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId={docId}&itemId={itemId}&generaltype=0'
            articleLink = urlPattern.format(docId=docId,itemId=itemId)
            print(articleLink)
            builddate = each['builddate']
            print(builddate)
            if itemId==927:
                zcfg=0;
            else:
                zcfg=1;
            pdfDownloadUrlPattern = 'https://www.cbirc.gov.cn/cbircweb/download/downloadPdf?docId={docId}&zcfg={zcfg}&itemId={itemId}'
            wordDownloadUrlPattern = 'https://www.cbirc.gov.cn/cbircweb/download/downloadDoc?docId={docId}&zcfg={zcfg}&itemId={itemId}'
            jsonUrlPattern = 'http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectByDocId/data_docId={docId}.json'
            pdfDownloadUrl = pdfDownloadUrlPattern.format(docId=docId,itemId=itemId,zcfg=zcfg)
            wordDownloadUrl = wordDownloadUrlPattern.format(docId=docId,itemId=itemId,zcfg=zcfg)
            jsonUrl = jsonUrlPattern.format(docId=docId)
            print(pdfDownloadUrl)
            print(wordDownloadUrl)
            print(jsonUrl)
            docTitle = each['docTitle']
            print(docTitle)
#             docFileUrl = each['docFileUrl']
#             print(docFileUrl)
#             pdfFileUrl = each['pdfFileUrl']
#             print(pdfFileUrl)
            recordDate = datetime.strptime(publishDate, "%Y-%m-%d %H:%M:%S")
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                print('yesterday > recordDate')
                #continue 
            
            add_params = {}
            docDict = {}
            docDict['publishDate'] = publishDate
            docDict['builddate'] = builddate
            docDict['articleLink'] = articleLink
            docDict['docId'] = docId
            docDict['pdfDownloadUrl'] = pdfDownloadUrl
            docDict['wordDownloadUrl'] = wordDownloadUrl
            docDict['docTitle'] = docTitle
            add_params['docDict'] = docDict
            yield scrapy.Request(jsonUrl, callback=self.get_detail,cb_kwargs=add_params)
            
    def get_detail(self,response,docDict):
        response = HtmlResponse(url=response.url, body=response.body, encoding='utf-8')  
        #print(response.encoding)  #查看网页返回的字符集类型
        item = GovinvestCbircItem()
        #print(response.text)
        body = json.loads(response.text)
        article = body['data']['docClob']
        #print(article)
        docDict['article'] = article
        item['dic']=docDict
        time.sleep(5)
        return item     
    
    
    
     
