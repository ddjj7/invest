# -*- coding: utf-8 -*-

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
    
class GovinvestMpsPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        r = requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestCacPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        r = requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestCbircPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        r = requests.post(posturl, data=data, headers=headers)
        return item
    