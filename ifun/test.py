#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:06:00 2019

@author: quert
"""

# age = int(input('Age :'))
# print(age)

import os, sys

path = '/Users/quert/Documents/GitHub'
items = os.listdir(path)

for file in items:
	print file

