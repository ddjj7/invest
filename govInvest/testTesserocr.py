'''
Created on 2021年12月2日

@author: hewei
'''

import tesserocr
from PIL import Image

# print(tesserocr.tesseract_version())  # print tesseract-ocr version
# print(tesserocr.get_languages())  # prints tessdata path and list of available languages

# image = Image.open('/home/hewei/下载/test3.jpg')
# print(tesserocr.image_to_text(image))  # print ocr text from image
# or
# print(tesserocr.file_to_text('/home/hewei/下载/test0.jpg'))
# print(tesserocr.file_to_text('/home/hewei/下载/test1.jpg'))
#print(tesserocr.file_to_text('/home/hewei/下载/2019-11-27 15-41-50.png'))
#print(tesserocr.file_to_text('/home/hewei/下载/test3.jpg'))

import ddddocr

ocr = ddddocr.DdddOcr()
with open('/home/hewei/下载/test3.jpg', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

print(res)

