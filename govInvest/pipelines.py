# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import io
import requests 
import json
from openpyxl import Workbook

class GovinvestAnhuiPipeline(object):
    
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
        packet['companyItem']='项目法人单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestJiangsuPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='江苏'
        packet['dateItem']='备案时间'
        packet['idItem']='备案证号'
        packet['companyItem']='申报单位名称'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestShandongPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='山东'
        packet['dateItem']='申报时间'
        packet['idItem']='项目代码'
        packet['companyItem']='项目(法人)单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestHubeiPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='湖北'
        packet['dateItem']='申请日期'
        packet['idItem']='项目代码'
        packet['companyItem']='单位名称'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestGuangdongPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='广东'
        packet['dateItem']='备案申报日期'
        packet['idItem']='备案项目编号'
        packet['companyItem']='建设单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestJiangxiPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='江西'
        packet['dateItem']='备案时间'
        packet['idItem']='项目编号'
        packet['companyItem']='建设单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestZhejiangPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='浙江'
        packet['dateItem']='办理时间'
        packet['idItem']='项目代码'
        packet['companyItem']=''
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestFujianPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='福建'
        packet['dateItem']='申请时间'
        packet['idItem']='项目代码'
        packet['companyItem']='项目（法人）单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestHunanPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='湖南'
        packet['dateItem']='发布日期'
        packet['idItem']='项目代码'
        packet['companyItem']=''
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestHenanPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='河南'
        packet['dateItem']='审批时间'
        packet['idItem']='项目代码'
        packet['companyItem']=''
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestHebeiPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='河北'
        packet['dateItem']='审批日期'
        packet['idItem']='项目代码'
        packet['companyItem']='项目法人单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestBeijingPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='北京'
        packet['dateItem']='立项时间'
        packet['idItem']='项目代码'
        packet['companyItem']='项目单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestGuangxiPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='广西'
        packet['dateItem']='备案时间'
        packet['idItem']='项目代码'
        packet['companyItem']='法人单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class GovinvestShaanxiPipeline(object):
    
    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['province']='陕西'
        packet['dateItem']='申报时间'
        packet['idItem']='项目代码'
        packet['companyItem']='法人单位'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class MpsPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['source'] = u'公安部'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        with io.open('./mps.txt','a',encoding='utf-8')as f:
            for k,v in dic.items():
                f.write(k+':'+str(v)+'\n')
            f.write('==============='+'\n')
        return item
    
class CacPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['source'] = u'网信办'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class CbircPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['source'] = u'银保监会'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        with io.open('./cbirc.txt','a',encoding='utf-8')as f:
            for k,v in dic.items():
                f.write(k+':'+str(v)+'\n')
            f.write('==============='+'\n')
        return item
    
class MiitPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['source'] = u'工信部'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class SasacPipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['source'] = u'国资委'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class ShcpePipeline(object):

    def process_item(self, item, spider):
        dic = item['dic']
        packet = {}
        packet['data'] = dic
        packet['source'] = u'上海票据交易所'
        # send to java server
        #posturl = 'http://10.47.123.120:6666/cdp-mcrsrv-admin/collect/saveCollectInfo'
        posturl = 'http://127.0.0.1:9090/api/recvScrapy1/'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(packet)
        requests.post(posturl, data=data, headers=headers)
        return item
    
class BeikePipeline(object):
    
    def process_item(self, item, spider):
        title = item['title']
        link=item['link']
        position=item['position']
        info=item['info']
        tag=item['tag']
        totalPrice=item['totalPrice']
        unitPrice=item['unitPrice']
        # 持久化存储io操作
        with io.open('../beike.txt','a',encoding='utf-8')as f:
            f.write(title+'\n')
            f.write(link+'\n')
            f.write(position+'\n')
            f.write(info+'\n')
            f.write(tag+'\n')
            f.write(totalPrice+'\n')
            f.write(unitPrice+'\n')
            f.write(r'==============='+'\n')
        return item
    
class BeikeXlsxPipeline(object):
    
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['title','link','position','info','tag','totalPrice','unitPrice'])
    
    def process_item(self, item, spider):
        line = [item['title'],item['link'],item['position'],item['info'],item['tag'],item['totalPrice']+r'万',item['unitPrice']]
        self.ws.append(line)
        self.wb.save('beike.xlsx')
        return item
    
# class CsvPipeline(object):
#
#     def __init__(self):
#         self.file = open("booksdata.csv",'wb')
#         self.exporter = CsvItemExporter(self.file,unicode)
#         self.exporter.start_exporting()
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#
#     def process_item(self,item,spider):
#         self.exporter.export_item(item)
#         return item
    
    # def create_valid_csv(self, item):
    #     for key, value in item.items():
    #         is_string = (isinstance(value, basestring))
    #         if (is_string and ("," in value.encode('utf-8'))):
    #             item[key] = "\"" + value + "\""

    