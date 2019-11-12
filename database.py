#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:43:37 2019

@author: hicaro
"""

import datetime

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
        self.email = None
        self.rt = None

    def setResult(self,resultado):
        self.rt = resultado

    def load(self):
        self.file = open(self.filename,"r")
        self.users = {}

        for line in self.file:
            email, senha, nome, created = line.strip().split(";")
            self.users[email] = (senha, nome, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1
                

    def get_user_nome(self, nome):
        for user in self.users:
            if self.users[user][1] == nome:
                return user
        return -1

    def add_user(self, email, senha, nome):
        if email.strip() not in self.users:
            self.users[email.strip()] = (senha.strip(), nome.strip(), Database.get_date())
            self.save()
            return 1
        else:
            print("Email já cadastrado")
            return -1
    
    def validate(self, email, senha):
        self.email = email
        e = self.get_user_nome(email)
        if self.get_user(email) != 1 and e == -1:
            return (self.users[email][0] == senha)
        else:
            if e != -1:
                self.email = e
                email = e
                if self.get_user(email) != 1:
                    return (self.users[email][0] == senha)
            else:    
                return False
    
    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                print(self.users[user][0])
                print(self.users[user][1])
                f.write(user + ";" + str(self.users[user][0]) + ";" + str(self.users[user][1]) + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
        