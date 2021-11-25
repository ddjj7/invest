'''
Created on 2021年9月13日

@author: hewei
'''

import requests
import json 
import random
import time
import io
import re
from datetime import timedelta, datetime
import govInvest.cookieTools as cookieTool
from requests.cookies import RequestsCookieJar

if __name__ == '__main0__':
#     print(int(random.random()*9000+1000))
#     print(int(time.time())*1000)
#     curTime = str(int(random.random()*9000+1000))+str(int(time.time())*1000)
#     print(curTime)
    ############################################
#     print(random.random()+10)
#     
#     url = 'http://tzxm.jxzwfww.gov.cn/icity/ipro/open/publicity'
#     r = requests.get(url)
#     print(r.text)
    ########################################3###
    chars = '0123456789abcdef'
    url = 'http://tzxm.jxzwfww.gov.cn/icity/ipro/open/publicity'
    r = requests.get(url)
    #print(r.text)
    sig = re.findall(r'var __signature = "(.*)"', r.text)[0]
    print(sig)
    
    key = ''
    keyIndex = -1
    for i in range(0,6):
        c = sig[keyIndex+1]
        #print(c)
        key+=c
        keyIndex = chars.find(c)
        if keyIndex <0 or keyIndex >= len(sig):
            keyIndex = i
    print(key)
    timestamp = str(int(random.random()*9000 + 1000)) + '_' + key + '_' + str(int(time.time())*1000).replace('+','-')
    print(timestamp)
    
    tkey = ''
    tkeyIndex = -1
    for i in range(0,6):
        c = timestamp[tkeyIndex+1]
        #print(c)
        tkey+=c
        tkeyIndex = chars.find(c)
        if tkeyIndex <0 or tkeyIndex >= len(timestamp):
            tkeyIndex = i
    print(tkey)
    
    print('s='+sig)
    print('t='+timestamp)
    print('o='+tkey)
    
    param = {'page': "1", 'rows': "10", 'type': "1", 'projectName': "", 'projectCode': "-"}
    posturl = 'http://tzxm.jxzwfww.gov.cn/icity/api-v2/jxtzxm.app.icity.ipro.IproCmd/getDisplayListByPage?s='+sig+'&t='+timestamp+'&o='+tkey
    r = requests.post(posturl,params=param)
    print(r.text)
    time.sleep(5)
    r1 = requests.post(posturl,params=param)
    print(r1.text)
    
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    geturl = 'https://tzxm.zjzwfw.gov.cn/tzxmweb/zwtpages/resultsPublicity/notice_of_publicity_new.html?page=1'
    r = requests.get(geturl,headers=headers, verify=False)
    print(r.status_code)
    cookiejar = r.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print(cookiedict)
    posturl = 'https://tzxm.zjzwfw.gov.cn/publicannouncement.do?method=queryItemList_new'
    #headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    packet = {}
    packet['pageFlag'] = 1
    packet['pageNo']= 0
    packet['area_code']= ''
    packet['area_flag']= 1
    packet['deal_code']= ''
    packet['item_name']= ''
    headers={
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'JSESSIONID='+cookiedict['JSESSIONID']+'; SERVERID='+cookiedict['SERVERID'],
        'referer': 'https://tzxm.zjzwfw.gov.cn/tzxmweb/zwtpages/resultsPublicity/notice_of_publicity_new.html?page=1',
        'sec-fetch-mode': 'cors',
        "sec-fetch-site": 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    r = requests.get('https://tzxm.zjzwfw.gov.cn/publicannouncement.do?method=publicCheck&t=0.3595959892320596', headers=headers, verify=False)
    with open('/home/hewei/下载/test.jpg','wb') as f:
        f.write(r.content)
    
    r = requests.post(posturl, data=packet, headers=headers, verify=False)#,cookies=cookie_jar, verify=False, allow_redirects=True
    print(r.status_code)
    print(r.text)
    
    
    
    