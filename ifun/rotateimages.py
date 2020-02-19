#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:06:36 2020

@author: quert
"""

import os
from PIL import Image

def rotateImages(rotationAmt):
	for image in os.listdir(os.getcwd()):
		img = Image.open(image)
		img.rotate(rotationAmt).save(image)
		img.close()

rotateImages(90)
rotateImages(180)
rotateImages(270)

'''
    Ref: https://gist.github.com/leonardreidy/2dcca95a7c14b485dcee06792c6f14e9
'''
