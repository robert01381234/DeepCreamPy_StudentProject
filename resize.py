# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:09:38 2019

@author: user
"""
import numpy as np
from PIL import Image
from PIL import ImageFilter
import os, sys

 
class image_aspect():
 
    def __init__(self, image_file, aspect_width, aspect_height):
        self.img = Image.open(image_file)
        self.aspect_width = aspect_width
        self.aspect_height = aspect_height
        self.result_image = None
 
    def change_aspect_rate(self):
        img_width = self.img.size[0]
        img_height = self.img.size[1]
 
        if (img_width / img_height) > (self.aspect_width / self.aspect_height):
            rate = self.aspect_width / img_width
        else:
            rate = self.aspect_height / img_height
 
        rate = round(rate, 1)
        print(rate)
        self.img = self.img.resize((int(img_width * rate), int(img_height * rate)))
        return self
 
    def past_background(self):
        self.result_image = Image.new("RGB", [self.aspect_width, self.aspect_height], (0, 0, 0, 255))
        self.result_image.paste(self.img, (int((self.aspect_width - self.img.size[0]) / 2), int((self.aspect_height - self.img.size[1]) / 2)))
        return self
 
    def save_result(self, file_name):
        self.result_image.save(file_name)
 
"""
if __name__ == "__main__":
    imagelist = os.listdir('./RESIZE/')
    
for img in imagelist:
    img1 = Image.open('./RESIZE/' + img)
    orsi = img1.size
    a = orsi[0]
    b = orsi[1]
    print (a,b)
    print (img1)
    image_aspect('./RESIZE/' + img, a*10, b*10).change_aspect_rate().past_background().save_result('./RESIZE/' + img)
    img1 = Image.open('./RESIZE/' + img)
    img1 = img1.filter(ImageFilter.SHARPEN) 
    image_aspect('./RESIZE/' + img, a*1, b*1).change_aspect_rate().past_background().save_result('./RESIZE/' + img)

"""