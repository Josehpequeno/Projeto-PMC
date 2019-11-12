#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:43:37 2019

@author: hicaro
"""
<Button@ButtonBehavior+Label>
    canvas.before:
        Color:
            rgba:0.1,0.5,0.7,1
        Ellipse:
            pos: self.pos
            size: self.height,self.height
        Ellipse:
            pos: self.x+self.width-self.height,self.y
            size: self.height, self.height
        Rectangle:
            pos: self.x+self.height/2,self.y
            size: self.width-self.height,self.height

            

import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
#from database import Database

class MyGrid(Widget):
    nome = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def btn(self):
        print("Nome", self.nome.text, "Email",self.email.text)
        self.nome.text = ""
        self.email.text = ""


def btn(instance):
    print("Run!")


class Touch(Widget):

    btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(0,1,0,.5, mode='rgba')
            Line(points=(20,30,400,500,60,500))
            Color(1,0,0,.5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50,50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)
        #self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("liliam.kv")


class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass

class LiliamApp(App):
    def build(self):
        return Widgets()
        #return kv
        #return Touch()       
        # return FloatLayout()
        #return MyGrid()

def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


if __name__ == "__main__":
    LiliamApp().run()
