# -*- coding: utf-8 -*-
import requests
import re
import execjs
import hashlib
import json
from requests.utils import add_dict_to_cookiejar

#url = 'https://www.mps.gov.cn/n6557558/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

'''
公安部
'''
def getMpsHeaderWithCookie(url):
    # 使用session保持会话
    res1 = requests.get(url, headers=headers)
    #print(res1.text)
    cookiejar = res1.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    #print(cookiejar)
    print(cookiedict)
    jsl_clearance_s = re.findall(r'cookie=(.*?);location', res1.text)[0]
    # 执行js代码
    jsl_clearance_s = str(execjs.eval(jsl_clearance_s)).split('=')[1].split(';')[0]
    # add_dict_to_cookiejar方法添加cookie
    #add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': jsl_clearance_s})
    #cookiedict['__jsl_clearance_s'] = jsl_clearance_s
    #__jsl_clearance_s=1628565425.41|-1|RzuwzFWX8ZtPtb458AaFArcZRd0%3D
    #print(cookiedict)
    __jsluid_s = cookiedict['__jsluid_s']
    headers['cookie'] = '__jsl_clearance_s='+jsl_clearance_s+";__jsluid_s="+__jsluid_s
    print(headers)
    res2 = requests.get(url, headers=headers)
    print(res2.text)
    # 提取go方法中的参数
    data = json.loads(re.findall(r';go\((.*?)\)', res2.text)[0])
    jsl_clearance_s = getClearance(data)
    # 修改cookie
    #add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': jsl_clearance_s})
    headers['cookie']= '__jsl_clearance_s='+jsl_clearance_s+";__jsluid_s="+__jsluid_s
    print(headers)
    return headers
    
"""
通过加密对比得到正确cookie参数
:param data: 参数
:return: 返回正确cookie参数
"""
def getClearance(data):
    chars = len(data['chars'])
    for i in range(chars):
        for j in range(chars):
            clearance = data['bts'][0] + data['chars'][i] + data['chars'][j] + data['bts'][1]
            encrypt = None
            if data['ha'] == 'md5':
                encrypt = hashlib.md5()
            elif data['ha'] == 'sha1':
                encrypt = hashlib.sha1()
            elif data['ha'] == 'sha256':
                encrypt = hashlib.sha256()
            encrypt.update(clearance.encode())
            result = encrypt.hexdigest()
            if result == data['ct']:
                return clearance
            
            

"""
jsl_clearance_s = getCookie(data)
# 修改cookie
add_dict_to_cookiejar(session.cookies, {'__jsl_clearance_s': jsl_clearance_s})
res3 = session.get(url, headers=header)
res3.encoding = 'utf-8'
print(res3.text)
"""

'''
安徽政府投资
'''
def get_unsbox(arg1):
    charList = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd,
             0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
             0x22, 0x25, 0xc, 0x24]
    va = []
    ret = ''
    for i in charList:
        va.append(arg1[i-1])
    ret = "".join(va)
    return ret

def get_hexxor(s1, constVar):
    ret = ''
    for i in range(len(s1)):
        if i % 2 != 0: continue
        xorChar1 = int(s1[i: i+2], 16)
        xorChar2 = int(constVar[i: i+2], 16)
        xorRes = (xorChar1 ^ xorChar2)
        hexRes = hex(xorRes)[2:]
        if len(hexRes) == 1:
            hexRes = '0' + hexRes
        ret += hexRes
    return ret

def getAHHeaderWithCookie(url):
    r = requests.get(url, headers=headers)
    arg1 = re.findall("arg1=\'(.*?)\'", r.text)[0]
    var1 = get_unsbox(arg1)
    var2 = get_hexxor(var1,'3000176000856006061501533003690027800375')
    print(var2)
    headers['cookie']='acw_sc__v2='+var2
    print(headers)
    return headers

if __name__ == '__main__':
    headers=getMpsHeaderWithCookie('https://www.miit.gov.cn/zwgk/wjgs/index.html')
    print(headers)
    res3 = requests.get('https://www.miit.gov.cn/zwgk/wjgs/index.html', headers=headers)
    res3.encoding = 'utf-8'
    print(res3.text)
#     headers = getAHHeaderWithCookie('http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll')
#     print(headers)
#     r = requests.get('http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll', headers=headers)
#     print(r.text)


