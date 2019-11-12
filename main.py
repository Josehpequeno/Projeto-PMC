#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:43:37 2019

@author: hicaro
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import Database
from kivy.config import Config 
from PMC import PMC

Config.set('graphics', 'width', '360') 
Config.set('graphics', 'height', '600')

class CriarContaWindow(Screen):
    nome = ObjectProperty(None)
    email = ObjectProperty(None)
    senha = ObjectProperty(None)

    def enviar(self):
        if self.nome.text == "":
            invalidForm(0) 
        elif self.email.text == "":
            invalidForm(1)
        elif self.senha.text == "":
            invalidForm(2)
        elif self.email.text.count("@") != 1 or self.email.text.count(".") == 0:
            invalidForm(3)
        else:
            if db.add_user(self.email.text, self.senha.text, self.nome.text) == -1:
                invalidForm(4)
                
                self.reset()

                sm.current = "create"
            else:
                db.validate(self.email.text, self.senha.text)
                MainWindow.current = self.email.text
                
                self.reset()

                sm.current = "main"

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.nome.text = ""
        self.senha.text = ""
    
class LoginWindow(Screen):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)

    def loginBtn(self):
        if self.email.text == "":
            invalidLogin(1)
        elif self.senha.text == "":
            invalidLogin(1)
        elif db.validate(self.email.text, self.senha.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin(0)

    def criarBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.senha.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    rt = ObjectProperty(None)
    current = ""
    

    def sair(self):
        sm.current = "login"

    def on_enter(self, *args):
        senha, nome, created = db.get_user(db.email)
        self.n.text = "Nome do Usuário: " + nome
        self.email.text = "Email: " + db.email
        self.created.text = "Criado Em: " + created
    def executarBtn(self):
        p = PMC()
        db.setResult(p.result)
        if p.queda == False:
            self.rt.text = db.rt + " da ação ficar estável ou subir"
        else:
            self.rt.text = db.rt + " da ação cair"

class gerenciadorWindow(ScreenManager):
    pass

def invalidLogin(a):
    if a == 0:
        pop = Popup(title='Erro no Login',
                    content = Label(text = 'nome de usuário \nou senha inválido.'),
                    size_hint=(None,None), size=(360,300))
        pop.open()
    else:
        pop = Popup(title='Erro no Login',
                    content = Label(text = 'campo nome de usuário ou senha não preenchido.'),
                    size_hint=(None,None), size=(360,300))
        pop.open()
def invalidForm(a):
    if a == 0:
        pop = Popup(title='Erro no formulário',
                    content=Label(text='Campo de Nome vazio.'),
                    size_hint=(None,None), size=(360,300))
    elif a == 1:
        pop = Popup(title='Erro no formulário',
                    content=Label(text='Campo de Email vazio.'),
                    size_hint=(None,None), size=(360,300))
    elif a == 2:
        pop = Popup(title='Erro no formulário',
                    content=Label(text='Campo de Senha vazio.'),
                    size_hint=(None,None), size=(360,300))
    elif a == 3:
        pop = Popup(title='Erro no formulário',
                    content=Label(text='Campo de Email com formato incorreto.'),
                    size_hint=(None,None), size=(360,300))
    elif a == 4:
        pop = Popup(title='Erro no formulário',
                    content=Label(text='Email já cadastrado.'),
                    size_hint=(None,None), size=(360,300))

    pop.open()

kv = Builder.load_file("liliam.kv")

sm = gerenciadorWindow()
db = Database("users.txt")

screens = [LoginWindow(name="login"), CriarContaWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class LiliamApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    LiliamApp().run()








