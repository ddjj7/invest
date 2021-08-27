# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from govInvest.items import GovinvestMiitItem
      
import time
import requests
import re
import json
from datetime import timedelta, datetime
from bs4 import BeautifulSoup

import govInvest.cookieTools as cookieTool

   
endFlag = '0'
headers = None

#工信
class MiitSpider(scrapy.Spider):
    name = 'miitSpider'
    zcjdCount = 1
    wjgsCount = 1
    filePgCount = {'个人信息':1,'融资租赁':1,'数据':1,'车辆':1}
    allowed_domains = ['www.miit.gov.cn']
    listUrl = 'https://www.miit.gov.cn/api-gateway/jpaas-publish-server/front/page/build/unit'
    start_urls = ['https://www.miit.gov.cn/zwgk/wjgs/index.html',
                  'https://www.miit.gov.cn/zwgk/zcjd/index.html',
                  'https://www.miit.gov.cn/search-front-server/api/search/info']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.MiitPipeline': 300},
    }
    
    def start_requests(self):
        global headers
        if not headers:
            headers = cookieTool.getMpsHeaderWithCookie(self.start_urls[0])
        for url in self.start_urls:
            if url == 'https://www.miit.gov.cn/search-front-server/api/search/info':
                keyWordList = [r'个人信息',r'融资租赁',r'数据',r'车辆']
                for word in keyWordList:
                    fullUrl = url+'?'
                    params = self.genParams()
                    params['q'] = word
                    params['p'] = str(self.filePgCount[params['q']])
                    add_params = {}
                    add_params['params'] = params
                    for paramKey in params:
                        fullUrl+='&'+paramKey+'='+params[paramKey]
                    print(fullUrl)
                    #yield Request(fullUrl,headers=headers, callback=self.parse_fileRepo, cb_kwargs=add_params)
            else:
                print(url)
                yield Request(url,headers=headers, callback=self.parse)
    
              
    def parse(self, response):
        global endFlag
        endFlag = '0'
        print(response.url)
        articleType = ''
        if 'wjgs' in response.url:
            count = self.wjgsCount 
            self.wjgsCount+=1
            articleType = 'wjgs'
        if 'zcjd' in response.url:
            count = self.zcjdCount 
            self.zcjdCount+=1
            articleType = 'zcjd'
        print (articleType+':$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        authorizedReadUnitId = re.findall(r'authorizedReadUnitId = "(.*)";', response.text)[0]
        path = '//*[@id="{authId}"]/@querydata'.format(authId=authorizedReadUnitId)
        strParams = response.xpath(path)[0].extract()
        dictParams = eval(strParams)
        paramJson = '{"pageNo":'+str(count)+',"pageSize":"24"}'
        dictParams['paramJson'] = paramJson
        print(dictParams)
        
        r = requests.get(self.listUrl, headers=headers, params=dictParams)
        body = json.loads(r.text)
        strHtml = body['data']['html']
        pageSoup = BeautifulSoup(strHtml,'html.parser')
        lis = pageSoup.find_all('li', class_='cf')
        for item in lis:
            date = item.find('span').text
            rawlink = item.find('a').get('href')
            title = item.find('a').text
            print(date)
            print(title)
            link = 'https://www.miit.gov.cn'+rawlink
            #print(link)
            recordDate = datetime.strptime(date, "%Y-%m-%d")
            #print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                pass
                #print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                pass
                #print('yesterday > recordDate')
                #endFlag='1'
                #continue 
            add_params = {}
            add_params['date'] = date
            add_params['title'] = title
            add_params['link'] = link
            if articleType =='wjgs':
                add_params['articleType'] = r'文件公示'
            elif articleType =='zcjd':
                add_params['articleType'] = r'政策解读'
            yield scrapy.Request(link, callback=self.get_detail,headers=headers,cb_kwargs=add_params)
          
        if count<5 and endFlag=='0':
            print ('go next '+articleType+' article page ------------------------------'+str(count))
            time.sleep(5)
            yield scrapy.Request(response.url+'?a='+str(count), callback=self.parse,headers=headers)
            
    def parse_fileRepo(self, response, params):
        global endFlag
        endFlag = '0'
        #print(response.text)
        print (params['q']+':$$$$$$$$$$$$$$$$$$'+str(self.filePgCount[params['q']])+'$$$$$$$$$$$$$$$$$$')
        body = json.loads(response.text)
        dataResults = body['data']['searchResult']['dataResults']
        count = self.filePgCount[params['q']]
        count+=1
        self.filePgCount[params['q']] = count
        for item in dataResults:
            title = item['groupData'][0]['data']['title']
            print(title)
            publishtimeint = int(item['groupData'][0]['data']['publishtime'])
            publishtime_local = time.localtime(publishtimeint/1000)
            publishtime = time.strftime("%Y-%m-%d", publishtime_local)
            print('publishtime='+publishtime)
            deploytimeint = int(item['groupData'][0]['data']['deploytime'])
            deploytime_local = time.localtime(deploytimeint/1000)
            deploytime = time.strftime("%Y-%m-%d", deploytime_local)
            print('deploytime='+deploytime)
            rawlink = item['groupData'][0]['data']['url']
            link = 'https://www.miit.gov.cn'+rawlink
            print(link)
            recordDate = datetime.strptime(deploytime, "%Y-%m-%d")
            #print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                pass
                #print('currDate == recordDate')
                #continue 
            if yesterday > recordDate:
                pass
                #print('yesterday > recordDate')
                #endFlag='1'
                #continue 
            add_params = {}
            add_params['date'] = publishtime
            add_params['title'] = title
            add_params['link'] = link
            add_params['articleType'] = r'政策文件'
            yield scrapy.Request(link, callback=self.get_detail,headers=headers,cb_kwargs=add_params)
          
        if self.filePgCount[params['q']]<2 or endFlag=='0':
            print ('go next '+params['q']+' page ------------------------------'+str(self.filePgCount[params['q']]))
            url = response.url
            print(url)
            index = url.index('&p=')
            partUrl = url[0:index+3]
            print(partUrl)
            url = partUrl+str(self.filePgCount[params['q']])
            print(url)
            params['p'] = str(self.filePgCount[params['q']])
            add_params = {}
            add_params['params'] = params
            time.sleep(5)
            yield scrapy.Request(url, callback=self.parse_fileRepo, headers=headers, cb_kwargs=add_params)
            
             
    def get_detail(self,response,date,title,link,articleType):
        item = GovinvestMiitItem()
        docDict = {}
        #print(response.text)
        text = ''
        for each in response.xpath("//*[@id='con_con']"):
            text = each.xpath("./p").xpath('string(.)').extract()
            #print(text)
        docDict['date'] = date
        #print(date)
        docDict['title'] = title
        #print(title)
        docDict['link'] = link
        docDict['text'] = text
        docDict['type'] = articleType
        item['dic']=docDict
        time.sleep(5)
        return item
    
    def genParams(self):
        params = {}
        params['websiteid']='110000000000000'
        params['scope']='basic'
        params['pg']='10'
        params['cateid']='57'
        params['pos']='title_text,infocontent,titlepy'
        params['_cus_eq_typename']=''
        params['_cus_eq_publishgroupname']=''
        params['_cus_eq_themename']=''
        params['begin']=''
        params['end']=''
        params['dateField']='deploytime'
        params['selectFields']='title,content,deploytime,_index,url,cdate,infoextends,infocontentattribute,columnname,filenumbername,publishgroupname,publishtime,metaid,bexxgk,columnid,xxgkextend1,xxgkextend2,themename,typename,indexcode,createdate'
        params['group']='distinct'
        params['highlightConfigs']='[{"field":"infocontent","numberOfFragments":2,"fragmentOffset":0,"fragmentSize":30,"noMatchSize":145}]'
        params['highlightFields']='title_text,infocontent,webid'
        params['level']='6'
        params['sortFields']='[{"name":"deploytime","type":"desc"}]'
        return params
    
    
    
     
