#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:57:42 2019

@author: hicaro
"""

from pytrends.request import TrendReq
import csv
import pandas as pd
import numpy as np

pytrends = TrendReq(hl='pt-BR', tz=360)

kw_list = ["Vale S.A."]
pytrends.build_payload(kw_list, cat=0, timeframe='2019-08-01T00 2019-08-03T23', geo='', gprop='')
dic = pytrends.interest_over_time() 
data = pd.DataFrame(dic)
datas = data.drop('isPartial', inplace=True, axis=1)
dat = data.to_numpy()
print(dic)
np.savetxt("/home/hicaro/Área de Trabalho/Projeto PMC/avaliar.csv", dat, delimiter=",")