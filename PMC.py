#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:25:50 2019

@author: hicaro
"""
from keras.models import Sequential
from keras.layers import Dense
from keras import losses
from keras.optimizers import SGD
from keras import initializers
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from bot import getDados


class PMC:

    result = None
    queda = False

    def __init__(self):

        dd = getDados()

        #coleta de dados
        dataset = np.loadtxt('vale.csv', delimiter = ',')

        #np.savetxt("/home/hicaro/Área de Trabalho/Projeto PMC/resultados.csv", dataset, delimiter=",")
        #print(dataset)
        #separação dos dados em amostras(x) e saida desejada(y) 
        #dados = dataset
        scaler = StandardScaler().fit(dataset)
        dataset = scaler.transform(dataset)
        dataset.tofile('dadosbaixados.csv', sep = ',')
        X = dataset[:,1:5]
        Y = dataset[:,0]

        #criando o modelo sequencial
        model = Sequential()

        model.add(Dense(100,kernel_initializer=initializers.RandomUniform(minval=-1, maxval=1, seed=4),input_dim=4, activation='tanh'))
        model.add(Dense(50,kernel_initializer=initializers.RandomUniform(minval=-1, maxval=1, seed=4), activation='tanh'))
        model.add(Dense(50,kernel_initializer=initializers.RandomUniform(minval=-1, maxval=1, seed=4), activation='tanh'))
        model.add(Dense(1,kernel_initializer=initializers.RandomUniform(minval=-1, maxval=1, seed=4),activation='tanh'))
        # Compile Model
        #compilando o modelo com a função de erro quadratico , algoritmo de otimização
        #gradiente descendente(sgd) com taxa de aprendizado 0.5 e metrica para avaliação a acurácia
        model.compile(loss=losses.mean_squared_error, optimizer=SGD(lr=0.001,momentum=0.0), metrics=["accuracy","mse"])
        # Avaliação do modelo com base no nome da metrica 

        history = model.fit(X, Y, epochs=6000, batch_size=168,verbose=1)
        scores = model.evaluate(X, Y)
            
        # Making predictions
        # calculate predictions
        predictions = model.predict(X, batch_size=168)
        predictions = (predictions > 0)
        rounded = [round(x[0]) for x in predictions]
        #print(rounded)
        rounded = np.array(rounded)
        dataset = np.column_stack((dataset, rounded))
        
        
        plt.plot(history.history['mean_squared_error'])
        plt.title('Modelo EQM')
        plt.ylabel('mse')
        plt.xlabel('epocas')
        plt.legend(['treinamento','teste'],loc='upper left')
        plt.show()  
        
        print("\n%s: %.6f" % (model.metrics_names[0], scores[0]))
        print("\n%s: %.6f" % (model.metrics_names[1], scores[1]))
        print("\n%s: %.6f" % (model.metrics_names[2], scores[2]))

        #Fase de operação
        dd.getDados_do_dia()

        #coleta de dados
        dataset = np.loadtxt('valetoday.csv', delimiter = ',')

        #print(dataset)
        #separação dos dados em amostras(x) e saida desejada(y) 
        #dados = dataset
        scaler = StandardScaler().fit(dataset)
        dataset = scaler.transform(dataset)
        entrada = dataset[:,1:5]
        dataset.tofile('dadosreais.csv', sep = ',')

        predictions_1 = model.predict(entrada)
        predictions_1.tofile('dadosprevistos.csv', sep = ',')
        predictions = (predictions_1 > 0)
        i = 0
        total = 0
        for prediction in predictions:
            if prediction == True:
                i = i + 1
            total = total + 1

        i = round((i/total) * 100,2)
        if i < 50:
            self.queda = True
            i = 100 - i
        self.result = str(i) + " %"

    def getResult(self):
        return self.result