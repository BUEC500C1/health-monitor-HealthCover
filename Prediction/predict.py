# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 05:21:45 2020

@author: 18367
"""

#Import the libraries required
import sys
from sys import path
path.append('../Database')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from database import request_data

#Importing the excel data 
def prediction(time):
    #Replace health.csv with data stored in the database
    file_path = request_data()
    dataset = pd.read_csv(file_path)
    #dataset = pd.read_csv(r'health.csv')
    if time > 0:
        x = []
        yPulse = []
        yBP = []
        yBO = []
        xx=dataset.loc[0:dataset['Time'].size-1,'Time'].values
        Pulse=dataset.loc[0:dataset['Pulse'].size-1,'Pulse'].values
        BP=dataset.loc[0:dataset['BloodPressure'].size-1,'BloodPressure'].values
        BO=dataset.loc[0:dataset['BloodOxygen'].size-1,'BloodOxygen'].values
        for i in range(0,len(xx)):
            if xx[i] < time:
                x.append(xx[i])
                yPulse.append(Pulse[i])
                yBP.append(BP[i])
                yBO.append(BO[i])
        x=np.array([x]).T
        yPulse=np.array([yPulse]).T
        yBP=np.array([yBP]).T
        yBO=np.array([yBO]).T
        regPulse=LinearRegression()
        regPulse.fit(x,yPulse)
        Pulse_pred=int(regPulse.predict(np.array([[time]])))
        print("Pulse prediction: ",Pulse_pred)
        regBP=LinearRegression()
        regBP.fit(x,yBP)
        BP_pred=int(regBP.predict(np.array([[time]])))
        print("Blood pressure prediction: ",BP_pred)
        regBO=LinearRegression()
        regBO.fit(x,yBO)
        BO_pred=int(regBO.predict(np.array([[time]])))
        print("Blood oxygen prediction: ",BO_pred)
        print()
    else:
        print("time should be bigger than 0")
        print()


prediction(3020)
