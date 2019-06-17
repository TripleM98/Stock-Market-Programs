# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:46:12 2019

@author: Meraz
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def PE_Times_PBV(totalShares,pricePerShare): #THIS FUNCTION CAN BE IMPROVED. NEEDS A LOT OF WORK.
    
    incomeData=pd.read_csv("fedExIncomeStatement.csv") #Read the Income Statement file.
    balanceData=pd.read_csv("fedexBalanceSheet.csv") #Read the Balance Sheet file.
    equity=balanceData["5/31/2018"].str.replace("$","") #Remove the $ sign in specified column
    newEquity=equity.str.replace(" ","") #Remove white space in specified column
    finalEquityList=newEquity.str.replace(",","").astype(float) #Remove comma and convert strings to float in specified column
    totalEquity=finalEquityList[28] #Access equity value from specified column
    bookValue=(totalEquity*1000)/totalShares #Calculate book value.Mulitply equity by 1000 since the value is in terms of millions
    pricePerBook=pricePerShare/bookValue #Calculate P/BV ratio
    safety=1/pricePerBook #Find safety value. Higher the number, the better.
    income=incomeData["5/31/2018"].str.replace("$","")#Remove $ sign.
    incomeList=income.str.replace(",","").astype(float)#Remove comma and convert string to float
    netIncome=incomeList[16]#Access net income value from specified column.
    earningsPerShare=(netIncome*1000)/totalShares#Calculate earnings per share(EPS). Mulitply net income by 1000 since the value is in terms of millions 
    pricePerEarnings=pricePerShare/earningsPerShare#Calculate P/E ratio.
    earningsReturn=1/pricePerEarnings#Calculate annual return from earnings
    isFavorable=False#Set company's favorability to false
    
    if(pricePerBook*pricePerEarnings<22.5):
        isFavorable=True #If P/E * P/BV is less than 22.5, then set company's favorability to true.
    
    
    return ("Favorable Company: "+str(isFavorable), "Safety:"+str(round(safety*100,2))+"%",
            "Return:"+str(round(earningsReturn*100,2))+"%")
    
   
dfIncome=pd.read_csv("fedexIncomeStatement.csv")
dfBalance=pd.read_csv("fedexBalanceSheet.csv")


print(PE_Times_PBV(260575000,150.55))

