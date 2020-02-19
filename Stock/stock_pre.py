#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:41:24 2020

@author: quert
"""

from datetime import date, timedelta
from urllib.request import urlopen
from dateutil import rrule
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
import json
import time


def craw_one_month(stock_number, date):
    url = (
        "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+
        date.strftime('%Y%m%d')+
        "stockNo="+
        str(stock_number)
        )
    data = json.loads(urlopen(url).read())
    return pd.DataFrame(data['data'], columns=data['fields'])

def craw_stock(stock_number, start_month):
    