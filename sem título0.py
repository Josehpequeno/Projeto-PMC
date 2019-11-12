#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:16:32 2019

@author: hicaro
"""
from datetime import datetime
from pytrends import pytrends
trends = pytrends()

keywords = ["Vale S.A."]
titles = ["Interest over time","Related queries"]
time = "all"
for title in titles:
  print(trends.download_report(keywords, title, time))
  
  
"""
pytrend = TrendReq()
year = datetime.utcnow().strftime('%Y')
month = datetime.utcnow().strftime('%m')
mt = int(month) - 4 
sm = "" 
if mt <= 9:
    sm = "0" + str(mt) 
else: 
    sm = str(mt)
    
dat = year + sm 
top_games = pytrend.top_charts( geo='US', date=dat)"""