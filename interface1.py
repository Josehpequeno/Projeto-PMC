#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:12:40 2019

@author: hicaro
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:10:23 2019

@author: hicaro
"""
from functools import partial
from tkinter import *

def bt_click():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 =  int(ed1.get())
        num2 =  int(ed2.get())
        lb["text"] = num1 + num2
    else:
        lb["text"] = "valores informados inválidos"
        
        
janela = Tk()

#bt1 = Button(janela, width=20, text="botão 1")
#bt1.place(x=95, y=250)
#bt1["command"] = partial(bt_click, bt1)

"""
ed1 = Entry(janela)
ed1.place(x = 100, y = 200)
ed2 = Entry(janela)
ed2.place(x = 100, y = 225)

bt2 = Button(janela, width=20, text="Soma", command = bt_click )
bt2.place(x=100, y=250)
#bt2["command"] = partial(bt_click, bt2)

lb = Label(janela, text="label")
lb.place(x = 100, y =320)
"""
"""
lb1 = Label(janela, text ="side1", bg = "green" )
lb2 = Label(janela, text ="side2", bg = "red" )
lb3 = Label(janela, text ="anchor1", bg = "yellow" )
lb4 = Label(janela, text ="anchor2", bg = "blue" )

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side = BOTTOM,anchor=SW)
"""
"""
lb1 = Label(janela, text = "linha1",bg= "white")
lb2 = Label(janela, text = "linha2",bg= "yellow")
lb3 = Label(janela, text = "linha2",bg= "blue")

lb1.pack(side=TOP,fill=BOTH, expand=1)
lb2.pack(side=TOP,fill=BOTH,expand=1)
lb3.pack(side=TOP, fill=BOTH,expand=1)
"""
"""
lb1 = Label(janela,text="ESPAÇO",width = "15",height=3,bg = "blue")
lbHORIZONTAL = Label(janela,text="horizontal",bg="yellow")
lbVERTICAL = Label(janela,text="vertical",bg="yellow")

lb1.grid(row=0,column = 0)
lbHORIZONTAL.grid(row=1,column=0,sticky=E)
lbVERTICAL.grid(row=0,column=1,sticky=S)
"""

lb1 = Label(janela, width= 15,height = 6,bg="red")
lb2 = Label(janela, width= 15,height = 6,bg="blue")
lb3 = Label(janela, width= 15,height = 6,bg="black")
lb4 = Label(janela, width= 15,height = 6,bg="yellow")

lb5 = Label(janela,height = 3,bg="green")
lb6 = Label(janela, width= 5,bg="pink")

lb1.grid(row = 0,column=0)
lb2.grid(row = 1,column=0)
lb3.grid(row = 0,column=1)
lb4.grid(row = 1,column=1)

lb5.grid(row=2,column=0,columnspan=2,sticky=W+E)
lb6.grid(row=0,column=2,rowspan=2,sticky=N+S)


janela.title("janela principal")#titulo
#janela["bg"] = "blue" #background da janela

#larguraXaltura+Esquerda do video+Topo do video
#300x300+100+100
janela.geometry("350x500")#gerenciador de leiaute place
 

janela.mainloop()