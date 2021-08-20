# 
# import requests
# import re
# 
# def get_unsbox(arg1):
#     charList = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd,
#              0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
#              0x22, 0x25, 0xc, 0x24]
#     va = []
#     ret = ''
#     for i in charList:
#         va.append(arg1[i-1])
#     ret = "".join(va)
#     return ret
# 
# def get_hexxor(s1, constVar):
#     ret = ''
#     for i in range(len(s1)):
#         if i % 2 != 0: continue
#         xorChar1 = int(s1[i: i+2], 16)
#         xorChar2 = int(constVar[i: i+2], 16)
#         xorRes = (xorChar1 ^ xorChar2)
#         hexRes = hex(xorRes)[2:]
#         if len(hexRes) == 1:
#             hexRes = '0' + hexRes
#         ret += hexRes
#     return ret
#     
# if __name__ == '__main__':
#     url = 'http://tzxm.ahzwfw.gov.cn/portalopenPublicInformation.do?method=queryExamineAll'
#     # 第一次请求获取js代码
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
#     r = requests.get(url, headers=headers)
#     # 重js中匹配出 arg1
#     arg1 = re.findall("arg1=\'(.*?)\'", r.text)[0]
# 
#     #arg1 = 'E47DC2AF11D45B585C11C0CC36200F97DD105D48'
#     var1 = get_unsbox(arg1)
#     var2 = get_hexxor(var1,'3000176000856006061501533003690027800375')
#     print(var2)
#     
#     # 二次请求携带cookie 获取html文件
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
#            "cookie": "acw_sc__v2=%s" % var2}
#     print(headers)
#     r = requests.get(url, headers=headers)
#     print(r.text)
