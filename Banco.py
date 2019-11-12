#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 19:28:55 2019

@author: hicaro
"""
import sqlite3
class Banco():
     
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()
     
    def createTable(self):
        c = self.conexao.cursor()
     
        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement ,
                     nome text,
                     email text,
                     usuario text,
                     senha text)""")
        self.conexao.commit()
        c.close()