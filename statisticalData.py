# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:16:26 2019

@author: Meraz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

def meanRoundedToNDigits(dataCol, n):
    average=round(dataCol.mean(), n)
    return average

def perChange(dataCol):
    
    percentChangeList=[]
    
    for i in range(len(dataCol)):
        
        nextPercentChange=((dataCol[1]-dataCol[0])/dataCol[0])
        percentChangeList.append(nextPercentChange)
        dataCol.pop(0)
              
        if(len(dataCol)-1==True):
            percentChangeList.append((dataCol[1]-dataCol[0])/dataCol[0])
            break
    
    return percentChangeList

def rangeDataSet(dataCol,n):
    range=round(dataCol.max()-dataCol.min(),n)
    return range

def sampleStandardDevRounded(dataCol,n):
    sampleStandardDev=round(statistics.stdev(dataCol), n)
    return sampleStandardDev

def quartileOne(dataCol):
    
    sortedCol=sorted(dataCol)
    medianOfList=statistics.median(sortedCol)
    Q1List=[]
    for i in range(len(sortedCol)):
        if(sortedCol[i]<=medianOfList):
            Q1List.append(sortedCol[i])
        else:
            break
    Q1=round(statistics.median(Q1List),2)
    
    return Q1
    
def quartileThree(dataColumn):
    
    sortedColumn=sorted(dataColumn)
    medianOfList=statistics.median(sortedColumn)
    for i in range(len(sortedColumn)):
        x=0
        if(sortedColumn[x]<=medianOfList):
            sortedColumn.pop(x)
            x=+1
        else:
            break
        
    Q3=round(statistics.median(sortedColumn),2)
    
    return Q3

def showOutliers(data):
    
    Q1=quartileOne(data)
    Q3=quartileThree(data)
    IQR=quartileThree(data)-quartileOne(data)
    lowerOutlier=Q1-(1.5*IQR)
    upperOutlier=Q3+(1.5*IQR)
    outlierList=[]
    
    for i in range(len(data)):
        if(data[i]<lowerOutlier):
            outlierList.append(data[i])
        if(data[i]>upperOutlier):
            outlierList.append(data[i])
    
    return outlierList

print("Outliers:",showOutliers([1,2,5,6,7,9,12,15,18,19,38]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    