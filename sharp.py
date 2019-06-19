# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:23:14 2019

@author: user
"""
import resize
import os
from PIL import Image                
from PIL import ImageFilter
'''
im02 = Image.open('./RESIZE/' + '5.jpg')
im = im02.filter(ImageFilter.SHARPEN) 

im.save('./RESIZE/' + '5.jpg')
'''
if __name__ == "__main__":
    imagelist = os.listdir('./RESIZE/')
    
for img in imagelist:
    img1 = Image.open('./RESIZE/' + img)
    orsi = img1.size
    a = orsi[0]
    b = orsi[1]
    print (a,b)
    print (img1)
    img1.show()
    '''
    resize.image_aspect('./RESIZE/' + img, a*10, b*10).change_aspect_rate().past_background().save_result('./RESIZE/' + img)

    img1 = Image.open('./RESIZE/' + img)
    img1.show()
'''
    img2 = img1.filter(ImageFilter.SHARPEN)

    img2.save('./RESIZE/' + img)
    img1 = Image.open('./RESIZE/' + img)
    img1.show()

    resize.image_aspect('./RESIZE/' + img, a*1, b*1).change_aspect_rate().past_background().save_result('./RESIZE/' + img)
    img1 = Image.open('./RESIZE/' + img)
    img1.show()