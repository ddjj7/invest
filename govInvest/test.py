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
import govInvest.cookieTools as cookieTool

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
    verifyParam = cookieTool.getShandongCookieParam('http://221.214.94.51:8081/icity/ipro/projectlist')
    sig = verifyParam[0]
    timestamp = verifyParam[1]
    t = time.time()
    posturl = 'http://221.214.94.51:8081/icity/api-v2/app.icity.ipro.IproCmd/getProjectList'
    headers = {'Content-Type': 'application/json'}
    packet = {}
    packet['page'] = 1
    packet['rows']='10'
    packet['projectcode']=''
    packet['projectname']=''
    packet['contractor']=''
    packet['projecttype']=''
    data = json.dumps(packet)
    posturl = posturl+'?s='+sig+'&t='+timestamp
    r = requests.post(posturl, data=data, headers=headers)
    print(r.text)
    body = json.loads(r.text)
    
    
    