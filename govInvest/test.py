'''
Created on 2021年9月13日

@author: hewei
'''

import requests
import json 
import random
import time
import re
from datetime import timedelta, datetime

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
    url = 'https://www.gdtz.gov.cn/tybm/apply3!searchMore3.action?isCity=false&actionCityId='
    r = requests.get(url, headers=headers)
    #print(r.text)
    url2 = 'https://www.gdtz.gov.cn/tybm/apply3!applyView.action?id=ff8080817bc8f1db017bc9ebcf40654f'
    r2 = requests.get(url2, headers=headers)
    print(r2.text)
    
    
    