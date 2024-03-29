# -*- coding: utf-8 -*-
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
    runlist = ['investGuangdongSpider']

    for spider_name in process.spiders.list():
        if spider_name not in runlist :
            continue
        print("Running spider %s" % (spider_name))
        process.crawl(spider_name)
    process.start()
    