#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:00:05 2019

@author: hicaro
"""

from tkinter import *

janela = Tk()

lb1 = Label(janela,text = "Login: ")
lb2 = Label(janela,text = "Senha: ")

ed1 = Entry(janela,)
ed2 = Entry(janela,)

bt1 = Button(janela,text = "Confirmar")

lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
ed1.grid(row=0,column=1)
ed2.grid(row=1,column=1)
bt1.grid(row=2,column=1)

janela.geometry("350x500+100+100")

janela.mainloop()