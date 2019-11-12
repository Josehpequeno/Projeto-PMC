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

class getDados:

    def __init__(self):
        pytrends = TrendReq(hl='pt-BR', tz=360)

        kw_list = ["Vale S.A.", "Vale Limited", "petrobras","Brumadinho","Trem da Vale"]
        pytrends.build_payload(kw_list, cat=0, timeframe='2019-07-25T01 2019-07-31T23', geo='', gprop='')
        dic = pytrends.interest_over_time() 
        data = pd.DataFrame(dic)
        datas = data.drop('isPartial', inplace=True, axis=1)
        #print(data)
        #print(data.to_numpy())
        #dat = data.to_numpy() #editing dat will reflect in df
        dat = data.to_numpy()
        print(dat)
        #dat.savetxt("/home/hicaro/Área de Trabalho/Projeto PMC/vale.csv")
        np.savetxt("/home/hicaro/Área de Trabalho/Projeto PMC/vale.csv", dat, delimiter=",")

        #df = pd.DataFrame(pytrends.suggestions(kw_list[0])) 

        #df.to_csv('file1.csv')
    def getDados_do_dia(self):
        pytrends = TrendReq(hl='pt-BR', tz=360)

        kw_list = ["Vale S.A.", "Vale Limited", "petrobras","Brumadinho","Trem da Vale"]
        pytrends.build_payload(kw_list, cat=0, timeframe='2019-08-01T12 2019-08-01T16', geo='', gprop='')
        dic = pytrends.interest_over_time()

        data = pd.DataFrame(dic)
        #data = data.drop('isPartial', inplace=True, axis=1)
        data.to_numpy()

        np.savetxt("/home/hicaro/Área de Trabalho/Projeto PMC/valetoday.csv", data, delimiter=",")
