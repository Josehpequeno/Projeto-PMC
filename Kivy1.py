#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:43:37 2019

@author: hicaro
"""

import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pandas as pd

print(pd.__version__)

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout()  
        self.inside.cols = 2
        
        self.inside.add_widget(Label(text="Nome: "))
        self.nome = TextInput(multiline=False)
        self.inside.add_widget(self.nome)

        self.inside.add_widget(Label(text="Senha: "))
        self.senha = TextInput(multiline=False)
        self.inside.add_widget(self.senha)
        
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        
        self.add_widget(self.inside)
        
        self.submit = Button(text="Entrar", font_size = 40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        
        
    def pressed(self,instance):
        nome = self.nome.text    
        senha = self.senha.text
        email = self.email.text
        
        print("Nome:", nome, "Senha" , senha, "Email:", email)
        self.nome.text = ""
        self.senha.text = ""
        self.email.text = ""

    
class MyApp(App):
    def build(self):
        #return Label(text = "Liliam App")
        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()