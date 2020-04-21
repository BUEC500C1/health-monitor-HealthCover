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
        yHR = []
        yBPL = []
        yBPH = []
        yBO = []
        yawRR = []
        xx=dataset.loc[0:dataset['Time'].size-1,'Time'].values
        HR=dataset.loc[0:dataset['HeartRate'].size-1,'HeartRate'].values
        BPL=dataset.loc[0:dataset['BloodPressureLow'].size-1,'BloodPressureLow'].values
        BPH = dataset.loc[0:dataset['BloodPressureHigh'].size - 1, 'BloodPressureHigh'].values
        BO=dataset.loc[0:dataset['BloodOxygen'].size-1,'BloodOxygen'].values
        awRR = dataset.loc[0:dataset['awRR'].size - 1, 'awRR'].values
        for i in range(0,len(xx)):
            if xx[i] < time:
                x.append(xx[i])
                yHR.append(HR[i])
                yBPL.append(BPL[i])
                yBPH.append(BPH[i])
                yBO.append(BO[i])
                yawRR.append(awRR[i])
        x=np.array([x]).T
        yHR=np.array([yHR]).T
        yBPL=np.array([yBPL]).T
        yBPH = np.array([yBPH]).T
        yBO=np.array([yBO]).T
        yawRR=np.array([yawRR]).T
        regPulse=LinearRegression()
        regPulse.fit(x,yHR)
        Pulse_pred=int(regPulse.predict(np.array([[time]])))
        print("Heart Rate prediction: ",Pulse_pred)
        regBPL=LinearRegression()
        regBPL.fit(x,yBPL)
        BPL_pred=int(regBPL.predict(np.array([[time]])))
        print("Blood pressure low prediction: ",BPL_pred)
        regBPH = LinearRegression()
        regBPH.fit(x, yBPH)
        BPH_pred = int(regBPH.predict(np.array([[time]])))
        print("Blood pressure high prediction: ", BPH_pred)
        regBO=LinearRegression()
        regBO.fit(x,yBO)
        BO_pred=int(regBO.predict(np.array([[time]])))
        print("Blood oxygen prediction: ",BO_pred)
        regawRR = LinearRegression()
        regawRR.fit(x, yawRR)
        awRR_pred = int(regawRR.predict(np.array([[time]])))
        print("awRR prediction: ", awRR_pred)
        print()
    else:
        print("time should be bigger than 0")
        print()

