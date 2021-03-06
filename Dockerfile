./govInvest/                                                                                        0000755 0001750 0001750 00000000000 14046630351 012165  5                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  ./govInvest/run.py                                                                                  0000664 0001750 0001750 00000001123 14046643312 013343  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-
# @Time    : 25/12/2016 5:35 PM
# @Author  : ddvv
# @Site    :
# @File    : run.py
# @Software: PyCharm

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

if __name__ == '__main__':
    setting = get_project_settings()
    process = CrawlerProcess(setting)
    didntWorkSpider = ['invest1','invest2']

    for spider_name in process.spiders.list():
        if spider_name in didntWorkSpider :
            continue
        print("Running spider %s" % (spider_name))
        process.crawl(spider_name)
    process.start()
                                                                                                                                                                                                                                                                                                                                                                                                                                                 ./govInvest/items.pyc                                                                               0000664 0001750 0001750 00000001560 14045206640 014026  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
2�`c           @   s[   d  d l  Z  d e  j f d �  �  YZ d e  j f d �  �  YZ d e  j f d �  �  YZ d S(   i����Nt   Govinvest1Itemc           B   s   e  Z e j �  Z RS(    (   t   __name__t
   __module__t   scrapyt   Fieldt   dic(    (    (    s:   /home/hewei/eclipse-workspace/govInvest/govInvest/items.pyR       s   	t   Govinvest2Itemc           B   s   e  Z e j �  Z RS(    (   R   R   R   R   R   (    (    (    s:   /home/hewei/eclipse-workspace/govInvest/govInvest/items.pyR      s   t   Govinvest3Itemc           B   s   e  Z e j �  Z RS(    (   R   R   R   R   R   (    (    (    s:   /home/hewei/eclipse-workspace/govInvest/govInvest/items.pyR      s   (   R   t   ItemR    R   R   (    (    (    s:   /home/hewei/eclipse-workspace/govInvest/govInvest/items.pyt   <module>   s                                                                                                                                                   ./govInvest/settings.py                                                                             0000664 0001750 0001750 00000006255 14045206451 014410  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-

# Scrapy settings for govInvest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'govInvest'

SPIDER_MODULES = ['govInvest.spiders']
NEWSPIDER_MODULE = 'govInvest.spiders'

FEED_EXPORT_ENCODING='UTF-8'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'govInvest (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'govInvest.middlewares.GovinvestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'govInvest.middlewares.GovinvestDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'govInvest.pipelines.Govinvest1Pipeline': 300,
    'govInvest.pipelines.Govinvest2Pipeline': 300,
    'govInvest.pipelines.Govinvest3Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
                                                                                                                                                                                                                                                                                                                                                   ./govInvest/pipelines.pyc                                                                           0000664 0001750 0001750 00000004632 14046453474 014712  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
�M�`c           @   sj   d  d l  Z  d  d l Z d  d l Z d e f d �  �  YZ d e f d �  �  YZ d e f d �  �  YZ d S(   i����Nt   Govinvest1Pipelinec           B   s   e  Z d  �  Z RS(   c   	      C   sy   | d } i  } | | d <d | d <d | d <d | d <d	 } i d
 d 6} t  j | � } t j | d | d | �} | S(   Nt   dict   datas   安徽t   provinces   审批时间t   dateItems   项目代码t   idItems&   http://127.0.0.1:9090/api/recvScrapy1/s   application/jsons   Content-Typet   headers(   t   jsont   dumpst   requestst   post(	   t   selft   itemt   spiderR   t   packett   posturlR   R   t   r(    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyt   process_item   s    




(   t   __name__t
   __module__R   (    (    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyR       s   t   Govinvest2Pipelinec           B   s   e  Z d  �  Z RS(   c   	      C   sy   | d } i  } | | d <d | d <d | d <d | d <d	 } i d
 d 6} t  j | � } t j | d | d | �} | S(   NR   R   s   江苏R   s   审批时间R   s   批复文号R   s&   http://127.0.0.1:9090/api/recvScrapy1/s   application/jsons   Content-TypeR   (   R   R   R	   R
   (	   R   R   R   R   R   R   R   R   R   (    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyR   0   s    




(   R   R   R   (    (    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyR   %   s   t   Govinvest3Pipelinec           B   s   e  Z d  �  Z RS(   c   	      C   sy   | d } i  } | | d <d | d <d | d <d | d <d	 } i d
 d 6} t  j | � } t j | d | d | �} | S(   NR   R   s   山东R   s   申报时间R   s   项目代码R   s&   http://127.0.0.1:9090/api/recvScrapy1/s   application/jsons   Content-TypeR   (   R   R   R	   R
   (	   R   R   R   R   R   R   R   R   R   (    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyR   J   s    




(   R   R   R   (    (    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyR   ?   s   (   t   ioR	   R   t   objectR    R   R   (    (    (    s>   /home/hewei/eclipse-workspace/govInvest/govInvest/pipelines.pyt   <module>   s
                                                                                                         ./govInvest/commonTools.py                                                                          0000664 0001750 0001750 00000000250 14046627751 015061  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-
'''
Created on 2021年5月12日

@author: hewei
'''

def returnNotNull(fieldList):
    if len(fieldList)>0:
        return fieldList[0]
                                                                                                                                                                                                                                                                                                                                                                ./govInvest/middlewares.py                                                                          0000664 0001750 0001750 00000007023 14017121375 015042  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class GovinvestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GovinvestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ./govInvest/commonTools.pyc                                                                         0000664 0001750 0001750 00000000670 14046630351 015220  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
�/�`c           @   s   d  Z  d �  Z d S(   s-   
Created on 2021年5月12日

@author: hewei
c         C   s   t  |  � d k r |  d Sd  S(   Ni    (   t   len(   t	   fieldList(    (    s@   /home/hewei/eclipse-workspace/govInvest/govInvest/commonTools.pyt   returnNotNull   s    N(   t   __doc__R   (    (    (    s@   /home/hewei/eclipse-workspace/govInvest/govInvest/commonTools.pyt   <module>   s                                                                           ./govInvest/__init__.pyc                                                                            0000644 0001750 0001750 00000000224 14017131233 014430  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
K0!^c           @   s   d  S(   N(    (    (    (    s=   /home/hewei/eclipse-workspace/govInvest/govInvest/__init__.pyt   <module>   t                                                                                                                                                                                                                                                                                                                                                                                ./govInvest/pipelines.py                                                                            0000664 0001750 0001750 00000006117 14046446723 014546  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import io
import requests 
import json

class Govinvest1Pipeline(object):
    
#     def process_item(self, item, spider):
#         dic = item['dic']
#         # 持久化存储io操作
#         with io.open('./govinvest_pipe.txt','a',encoding='utf-8')as f:
#             for k,v in dic.items():
#                 f.write(k+':'+v+'\n')
#             f.write('==============='.decode('utf-8')+'\n')
#         return item

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='安徽'
        packet['dateItem']='审批时间'
        packet['idItem']='项目代码'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        r = requests.post(posturl, data=data, headers=headers)
        return item
    
class Govinvest2Pipeline(object):

#     def process_item(self, item, spider):
#         dic = item['dic']
#         # 持久化存储io操作
#         with io.open('./govinvest_pipe2.txt','a',encoding='utf-8')as f:
#             for k,v in dic.items():
#                 f.write(k+':'+v+'\n')
#             f.write('==============='.decode('utf-8')+'\n')
#         return item
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='江苏'
        packet['dateItem']='审批时间'
        packet['idItem']='批复文号'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        r = requests.post(posturl, data=data, headers=headers)
        return item
    
class Govinvest3Pipeline(object):

#     def process_item(self, item, spider):
#         dic = item['dic']
#         # 持久化存储io操作
#         with io.open('./govinvest_pipe3.txt','a',encoding='utf-8')as f:
#             for k,v in dic.items():
#                 f.write(k+':'+v+'\n')
#             f.write('==============='.decode('utf-8')+'\n')
#         return item
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='山东'
        packet['dateItem']='申报时间'
        packet['idItem']='项目代码'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        r = requests.post(posturl, data=data, headers=headers)
        return item
                                                                                                                                                                                                                                                                                                                                                                                                                                                     ./govInvest/spiders/                                                                                0000755 0001750 0001750 00000000000 14046641563 013645  5                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  ./govInvest/spiders/invest3.pyc                                                                     0000664 0001750 0001750 00000006226 14046641563 015765  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
qC�`c           @   s�   d  d l  Z  d  d l m Z d  d l Z d  d l m Z m Z d  d l Z d  d l Z d  d l j	 Z
 d a d e  j f d �  �  YZ d S(   i����N(   t   Govinvest3Item(   t	   timedeltat   datetimei   t   Invest3Spiderc           B   s4   e  Z d  Z d g Z i i d d 6d 6Z d �  Z RS(   t   invest3s0   http://221.214.94.51:8081/icity/ipro/projectlisti,  s&   govInvest.pipelines.Govinvest3Pipelinet   ITEM_PIPELINESc         c   s�  d } d } t  j  �  } d t t � d GHi d d 6} i  } t | d <d | d <d	 | d
 <d	 | d <d	 | d <d	 | d <t j | � } | d t t t | d � � � } t j | d | d | �} t j	 | j
 � }	 x�|	 d D]�}
 t �  } i  } |
 d } t j | d � } t j t j �  j d � d � } t j t j �  t d � j d � d � } | | k ryd GHq� n  | | k r�d } d GHq� n  |
 d } |
 d } |
 d } t | � d k  r�q� n  |
 d } |
 d } | d k r�q� n  |
 d } |
 d  } | | d! <| | d" <| | d# <| | d$ <d% | d& <| | d' <| | d( <| | d) <| | d* <| Vq� Wt d+ 7a | d k r�d, t t � GHt  j d � d- } t j | d. i t t � d/ 6d0 |  j �Vn  d  S(1   Nt   0sL   http://221.214.94.51:8081/icity/api-v2/app.icity.ipro.IproCmd/getProjectLists   $$$$$$$$$$$$$$$$$$s   application/jsons   Content-Typet   pagei
   t   limitt    t   projectcodet   projectnamet
   contractort   projecttypes%   ?s=eb54861620379457861&t=7045_e72466_i�  t   datat   headerst
   APPLY_DATEs   %Y-%m-%di����s   currDate == recordDatet   1s   yesterday > recordDatet   PROJECT_CODEt   PROJECT_NAMEt   ENTERPRISE_NAMEi   t   CONTACT_NAMEt   STATUSt   99t   SEQ_IDt   PROJECT_TYPEu   项目代码u   项目名称u   项目(法人)单位u   项目法人u	   已赋码u   项目阶段u   seqIdu   项目类型u   申报时间u   dici   s+   go next page ------------------------------s0   http://221.214.94.51:8081/icity/ipro/projectlistt   formdatat   pageNot   callback(   t   timet   strt   countt   jsont   dumpst   intt   roundt   requestst   postt   loadst   textR    R   t   strptimet   nowt   strftimet   todayR   t   lent   sleept   scrapyt   FormRequestt   parse(   t   selft   responset   endFlagt   posturlt   tR   t   packetR   t   rt   bodyt   eacht   itemt   dictt	   applyDatet
   recordDatet   currDatet	   yesterdayt   projectCodet   projectNamet   enterpriseNamet   contactNamet   statust   seqIdt   projectTypet   startUrl(    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest3.pyR0      sr    





$	
!+















	
(   t   __name__t
   __module__t   namet
   start_urlst   custom_settingsR0   (    (    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest3.pyR      s
   	(   R.   t   govInvest.itemsR    R   R   R   R$   R    t   govInvest.commonToolst   commonToolst   toolR   t   SpiderR   (    (    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest3.pyt   <module>   s                                                                                                                                                                                                                                                                                                                                                                             ./govInvest/spiders/invest1.py                                                                      0000664 0001750 0001750 00000012334 14046640562 015613  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-
import scrapy
from govInvest.items import Govinvest1Item
      
#import sys
import time
from datetime import timedelta, datetime

import govInvest.commonTools as tool

# reload(sys)
# sys.setdefaultencoding("utf-8")
   
count = 0
  
#安徽 
class Itnvest1Spider(scrapy.Spider):
    name = 'invest1'
    allowed_domains = ['tzxm.ahzwfw.gov.cn']
    start_urls = ['http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.Govinvest1Pipeline': 300},
    }
              
    def parse(self, response):
        global count
        endFlag='0'
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        for each in response.xpath("//*[@id='publicInformationForm']/tr"):
            date = each.xpath("./td[5]/text()").extract()[0]
            result = each.xpath("./td[4]/text()").extract()[0]
            rawlink = each.xpath("./td[1]/a[1]/@onclick").extract()[0]
            link = rawlink.replace('window.open(\'','http://tzxm.ahzwfw.gov.cn')
            index = len(link)
            link = link[0:index-2]
            time.sleep(0.3) 
            recordDate = datetime.strptime(date, "%Y/%m/%d")
            #print(recordDate)
            currDate = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(currDate)
            yesterday = datetime.strptime((datetime.today()+ timedelta(-1)).strftime("%Y-%m-%d"), "%Y-%m-%d")
            #print(yesterday)
            if currDate == recordDate:
                #print('currDate == recordDate')
                continue 
            if yesterday > recordDate:
                #print('yesterday > recordDate')
                endFlag='1'
                continue 
            if result !=u'批复':
                continue
            yield scrapy.Request(link, callback=self.get_detail)
         
        count +=1     
        #currDate = datetime.datetime.strptime(currentDate, "%Y/%m/%d")
        #print (currDate)
        #if currDate > datetime.datetime.strptime('2021/05/15', "%Y/%m/%d"): 
        print ('go next page ------------------------------'+str(count))
        nextUrl = 'http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll'
        if endFlag=='0':
            yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
             
    def get_detail(self,response):
        item = Govinvest1Item()
        dict = {}
         
        #//*[@id="tab00"]/div[1]/table/tbody/tr[1]/td[1]
        projectCode = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[1]/text()").extract()[0]
        projectCodeValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[2]/text()").extract())
        projectName = response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[3]/text()").extract()[0]
        projectNameValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[1]/td[4]/text()").extract())
         
        projectType = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[1]/text()").extract()[0]
        projectTypeValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[2]/text()").extract())
        projectLegelPerson = response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[3]/text()").extract()[0]
        projectLegelPersonValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[1]/table/tr[2]/td[4]/text()").extract())
         
        dict[projectCode] = projectCodeValue
        dict[projectName] = projectNameValue
        dict[projectType] = projectTypeValue
        dict[projectLegelPerson] = projectLegelPersonValue
         
        #//*[@id="tab00"]/div[2]/div[2]/table/tbody/tr[1]/td[1]
        approveDepartment = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[1]/text()").extract()[0]
        approveMatter = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[2]/text()").extract()[0]
        approveResult = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[3]/text()").extract()[0]
        approveTime = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[4]/text()").extract()[0]
        approveNo = response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[5]/text()").extract()[0]
         
        approveDepartmentValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[1]/text()").extract())
        approveMatterValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[2]/text()").extract())
        approveResultValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[3]/text()").extract())
        approveTimeValue =  tool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[4]/text()").extract())
        approveNoValue = tool.returnNotNull(response.xpath("//*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[5]/span[1]/text()").extract())
         
        dict[approveDepartment] = approveDepartmentValue
        dict[approveMatter] = approveMatterValue
        dict[approveResult] = approveResultValue
        dict[approveTime] = approveTimeValue
        dict[approveNo] = approveNoValue
        item['dic']=dict
        return item
    
    
    
     
                                                                                                                                                                                                                                                                                                    ./govInvest/spiders/invest2.py                                                                      0000664 0001750 0001750 00000006067 14046641543 015622  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-
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
    start_urls = ['http://222.190.131.17:8075/portalopenPublicInformation.do?method=queryExamineAll']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.Govinvest2Pipeline': 300},
    }

    def parse(self, response):
        global count
        endFlag='0'
        nextUrl = 'http://222.190.131.17:8075/portalopenPublicInformation.do?method=queryExamineAll'
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
        if endFlag=='0':
            print ('go next page ------------------------------'+str(count))
            yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ./govInvest/spiders/__init__.pyc                                                                    0000644 0001750 0001750 00000000234 14017131233 016102  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
K0!^c           @   s   d  S(   N(    (    (    (    sE   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/__init__.pyt   <module>   t                                                                                                                                                                                                                                                                                                                                                                        ./govInvest/spiders/invest2.pyc                                                                     0000664 0001750 0001750 00000005272 14046641563 015764  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
cC�`c           @   sp   d  d l  Z  d  d l m Z d  d l Z d  d l m Z m Z d  d l j Z d a	 d e  j
 f d �  �  YZ d S(   i����N(   t   Govinvest2Item(   t	   timedeltat   datetimei    t   Invest2Spiderc           B   s4   e  Z d  Z d g Z i i d d 6d 6Z d �  Z RS(   t   invest2sP   http://222.190.131.17:8075/portalopenPublicInformation.do?method=queryExamineAlli,  s&   govInvest.pipelines.Govinvest2Pipelinet   ITEM_PIPELINESc         c   sq  d } d } d t  t � d GHx�| j d � D]�} t �  } i  } | j d � j �  d } t j d � t j | d � } t j t j	 �  j
 d	 � d	 � }	 t j t j �  t d
 � j
 d	 � d	 � }
 |	 | k r� d GHq/ n  |
 | k r� d } d GHq/ n  t j | j d � j �  � } t j | j d � j �  � } t j | j d � j �  � } t j | j d � j �  � } t j | j d � j �  � } | d k r�q/ n  t j | j d � j �  � } | | d <| | d <| | d <| | d <| | d <| | d <| | d <| | d <| Vq/ Wt d 7a | d k rmd t  t � GHt j | d i t  t � d  6d! |  j �Vn  d  S("   Nt   0sP   http://222.190.131.17:8075/portalopenPublicInformation.do?method=queryExamineAlls   $$$$$$$$$$$$$$$$$$s#   //*[@id='publicInformationForm']/trs   ./td[7]/text()i    g333333�?s   %Y/%m/%ds   %Y-%m-%di����s   currDate == recordDatet   1s   yesterday > recordDates   ./td[1]/@titles   ./td[2]/text()s   ./td[3]/text()s   ./td[4]/text()s   ./td[5]/text()u   批复s   ./td[6]/text()u   项目名称u   审批事项u   审批部门u   部门区划u   审批结果u   批复文号u   审批时间t   dici   s+   go next page ------------------------------t   formdatat   pageNot   callback(   t   strt   countt   xpathR    t   extractt   timet   sleepR   t   strptimet   nowt   strftimet   todayR   t   toolt   returnNotNullt   scrapyt   FormRequestt   parse(   t   selft   responset   endFlagt   nextUrlt   eacht   itemt   dictt   datet
   recordDatet   currDatet	   yesterdayt   titlet   mattert
   departmentt   districtt   resultt   resultno(    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest2.pyR      sN    	!+







	
(   t   __name__t
   __module__t   namet
   start_urlst   custom_settingsR   (    (    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest2.pyR      s
   	(   R   t   govInvest.itemsR    R   R   R   t   govInvest.commonToolst   commonToolsR   R   t   SpiderR   (    (    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest2.pyt   <module>   s                                                                                                                                                                                                                                                                                                                                         ./govInvest/spiders/invest3.py                                                                      0000664 0001750 0001750 00000006710 14046641561 015616  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-
import scrapy
from govInvest.items import Govinvest3Item

#import sys
import time
from datetime import timedelta, datetime
import requests 
import json

import govInvest.commonTools as tool
# reload(sys)
# sys.setdefaultencoding("utf-8")
  
count = 1

#山东
class Invest3Spider(scrapy.Spider):
    name = 'invest3'
    #allowed_domains = ['221.214.94.51:8081']
    start_urls = ['http://221.214.94.51:8081/icity/ipro/projectlist']
    custom_settings = {
        'ITEM_PIPELINES': {'govInvest.pipelines.Govinvest3Pipeline': 300},
    }

    def parse(self, response):
        global count
        endFlag='0'
        posturl = 'http://221.214.94.51:8081/icity/api-v2/app.icity.ipro.IproCmd/getProjectList'
        t = time.time()
        print ('$$$$$$$$$$$$$$$$$$'+str(count)+'$$$$$$$$$$$$$$$$$$')
        #yield scrapy.FormRequest(nextUrl, formdata = {'pageNo':'2'}, callback=self.parse)
        headers = {'Content-Type': 'application/json'}
        packet = {}
        packet['page'] = count
        packet['limit']=10
        packet['projectcode']=''
        packet['projectname']=''
        packet['contractor']=''
        packet['projecttype']=''
        data = json.dumps(packet)
        posturl = posturl+'?s=eb54861620379457861&t=7045_e72466_'+str(int(round(t * 1000)))
        r = requests.post(posturl, data=data, headers=headers)
        body = json.loads(r.text)
        for each in body['data']:
            item = Govinvest3Item()
            dict = {}
            applyDate = each['APPLY_DATE']
            recordDate = datetime.strptime(applyDate, "%Y-%m-%d")
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
            
            projectCode = each['PROJECT_CODE']
            projectName = each['PROJECT_NAME']
            enterpriseName = each['ENTERPRISE_NAME']
            if len(enterpriseName)<5:
                continue
            
            contactName = each['CONTACT_NAME']
            status = each['STATUS']
            if status !='99':
                continue
            
            seqId = each['SEQ_ID']
            projectType = each['PROJECT_TYPE']
            
            dict[u'项目代码'] = projectCode   #项目代码
            dict[u'项目名称'] = projectName   #项目名称
            dict[u'项目(法人)单位'] = enterpriseName  #项目(法人)单位
            dict[u'项目法人'] = contactName   #项目法人
            dict[u'项目阶段'] = u'已赋码'   #项目阶段  99=已赋码
            dict[u'seqId'] = seqId
            dict[u'项目类型'] = projectType  #项目类型
            dict[u'申报时间'] = applyDate   #申报时间
            item[u'dic']=dict
            yield item
            
        count +=1     
        if endFlag=='0':
            print ('go next page ------------------------------'+str(count))
            time.sleep(5) 
            startUrl = 'http://221.214.94.51:8081/icity/ipro/projectlist'  #没用
            yield scrapy.FormRequest(startUrl, formdata = {'pageNo':str(count)}, callback=self.parse)
            
                                                        ./govInvest/spiders/invest1.pyc                                                                     0000664 0001750 0001750 00000011105 14046641441 015746  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
rA�`c           @   sp   d  d l  Z  d  d l m Z d  d l Z d  d l m Z m Z d  d l j Z d a	 d e  j
 f d �  �  YZ d S(   i����N(   t   Govinvest1Item(   t	   timedeltat   datetimei    t   Itnvest1Spiderc           B   sF   e  Z d  Z d g Z d g Z i i d d 6d 6Z d �  Z d �  Z RS(   t   invest1s   tzxm.ahzwfw.gov.cnsO   http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAlli,  s&   govInvest.pipelines.Govinvest1Pipelinet   ITEM_PIPELINESc         c   s�  d } d t  t � d GHxO| j d � D]>} | j d � j �  d } | j d � j �  d } | j d � j �  d } | j d d	 � } t | � } | d | d
 !} t j d � t j	 | d � }	 t j	 t j
 �  j d � d � }
 t j	 t j �  t d � j d � d � } |
 |	 k r&q) n  | |	 k r>d } q) n  | d k rPq) n  t j | d |  j �Vq) Wt d 7a d t  t � GHd } | d k r�t j | d i t  t � d 6d |  j �Vn  d  S(   Nt   0s   $$$$$$$$$$$$$$$$$$s#   //*[@id='publicInformationForm']/trs   ./td[5]/text()i    s   ./td[4]/text()s   ./td[1]/a[1]/@onclicks   window.open('s   http://tzxm.ahzwfw.gov.cni   g333333�?s   %Y/%m/%ds   %Y-%m-%di����t   1u   批复t   callbacki   s+   go next page ------------------------------sO   http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAllt   formdatat   pageNo(   t   strt   countt   xpatht   extractt   replacet   lent   timet   sleepR   t   strptimet   nowt   strftimet   todayR   t   scrapyt   Requestt
   get_detailt   FormRequestt   parse(   t   selft   responset   endFlagt   eacht   datet   resultt   rawlinkt   linkt   indext
   recordDatet   currDatet	   yesterdayt   nextUrl(    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest1.pyR      s4    !+
c         C   sf  t  �  } i  } | j d � j �  d } t j | j d � j �  � } | j d � j �  d } t j | j d � j �  � } | j d � j �  d } t j | j d � j �  � }	 | j d � j �  d }
 t j | j d	 � j �  � } | | | <| | | <|	 | | <| | |
 <| j d
 � j �  d } | j d � j �  d } | j d � j �  d } | j d � j �  d } | j d � j �  d } t j | j d � j �  � } t j | j d � j �  � } t j | j d � j �  � } t j | j d � j �  � } t j | j d � j �  � } | | | <| | | <| | | <| | | <| | | <| | d <| S(   Ns0   //*[@id='tab00']/div[1]/table/tr[1]/td[1]/text()i    s0   //*[@id='tab00']/div[1]/table/tr[1]/td[2]/text()s0   //*[@id='tab00']/div[1]/table/tr[1]/td[3]/text()s0   //*[@id='tab00']/div[1]/table/tr[1]/td[4]/text()s0   //*[@id='tab00']/div[1]/table/tr[2]/td[1]/text()s0   //*[@id='tab00']/div[1]/table/tr[2]/td[2]/text()s0   //*[@id='tab00']/div[1]/table/tr[2]/td[3]/text()s0   //*[@id='tab00']/div[1]/table/tr[2]/td[4]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[1]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[2]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[3]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[4]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[1]/td[5]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[1]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[2]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[3]/text()s7   //*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[4]/text()s?   //*[@id='tab00']/div[2]/div[2]/table/tr[2]/td[5]/span[1]/text()t   dic(   R    R   R   t   toolt   returnNotNull(   R   R   t   itemt   dictt   projectCodet   projectCodeValuet   projectNamet   projectNameValuet   projectTypet   projectTypeValuet   projectLegelPersont   projectLegelPersonValuet   approveDepartmentt   approveMattert   approveResultt   approveTimet	   approveNot   approveDepartmentValuet   approveMatterValuet   approveResultValuet   approveTimeValuet   approveNoValue(    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest1.pyR   ?   s>    	









(   t   __name__t
   __module__t   namet   allowed_domainst
   start_urlst   custom_settingsR   R   (    (    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest1.pyR      s   			&(   R   t   govInvest.itemsR    R   R   R   t   govInvest.commonToolst   commonToolsR*   R   t   SpiderR   (    (    (    sD   /home/hewei/eclipse-workspace/govInvest/govInvest/spiders/invest1.pyt   <module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                              ./govInvest/spiders/__init__.py                                                                     0000644 0001750 0001750 00000000241 13610230113 015730  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
                                                                                                                                                                                                                                                                                                                                                               ./govInvest/settings.pyc                                                                            0000664 0001750 0001750 00000001021 14045206640 014535  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  �
)�`c           @   s@   d  Z  d g Z d Z d Z e Z i d d 6d d 6d d 6Z d S(   t	   govInvests   govInvest.spiderss   UTF-8i,  s&   govInvest.pipelines.Govinvest1Pipelines&   govInvest.pipelines.Govinvest2Pipelines&   govInvest.pipelines.Govinvest3PipelineN(   t   BOT_NAMEt   SPIDER_MODULESt   NEWSPIDER_MODULEt   FEED_EXPORT_ENCODINGt   Truet   ROBOTSTXT_OBEYt   ITEM_PIPELINES(    (    (    s=   /home/hewei/eclipse-workspace/govInvest/govInvest/settings.pyt   <module>   s   	-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ./govInvest/__init__.py                                                                             0000644 0001750 0001750 00000000000 13610230113 014250  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  ./govInvest/items.py                                                                                0000664 0001750 0001750 00000001201 14045206462 013655  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Govinvest1Item(scrapy.Item):
    # define the fields for your item here like:
#     department = scrapy.Field()
#     result = scrapy.Field()
#     matter = scrapy.Field()
#     title = scrapy.Field()
#     date = scrapy.Field()
#     rawlink = scrapy.Field()
#     link = scrapy.Field()
    dic = scrapy.Field()
    pass

class Govinvest2Item(scrapy.Item):
    dic = scrapy.Field()
    pass

class Govinvest3Item(scrapy.Item):
    dic = scrapy.Field()
    pass



                                                                                                                                                                                                                                                                                                                                                                                               ./scrapy.cfg                                                                                        0000644 0001750 0001750 00000000405 14017121375 012161  0                                                                                                    ustar   hewei                           hewei                                                                                                                                                                                                                  # Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.io/en/latest/deploy.html

[settings]
default = govInvest.settings

[deploy]
#url = http://localhost:6800/
project = govInvest
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           