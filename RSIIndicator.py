# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:39:38 2019

@author: Meraz
"""

import pandas as pd

#RSI=100-(100/(1+RS))
#RS=(Average gain over specified period)/(Average loss over the same period)
#RSI generally calculated over 14 periods(can be 14 days, 14 weeks, 14 months, etc)
#If RSI>70, then it is generally overbrought. If RSI<30, then it is generally oversold

#Pseudo Program:
    #Take the average closing section of the data table.
    #Find the percent change in each row. Do this with percentChange=(N-O)/O.
    #To calculate the percent change, loop through average closing section and apply the 
    #formula to each row.Add each of the percent change to an average closing percent change list.
    #Create another two new lists. One list that has upward movement(if no gains, then replace loss with 0).
    #The second list has downward movement (if no losses, then replace gain with 0). Both lists should have no 
    #negative values.
    #Create lists for average upward movement and average downward movement. for first value in list, take
    #average of first n period. For second value in list, multiply previous item in the list (n-1) and
    #add it by current upward/ downward movement. Divide the whole thing by n.
    #(Yesterday[from average upward movement]* (n-1)+today[from upward movement])/n
    #Relative Strength=Average Upward Gain/Average Downward Gain
    #Relative Strength Indicator=100-(100/(relativeStrength[i]+1)
    
    
def RSI(data, n):
    
    changeList=[]
    upMovementList=[]
    downMovementList=[]
    x=0
    a=n
    b=0
    c=n
    sumUp=0
    sumDown=0
    averageUpwardList=[]
    averageDownwardList=[]
    relativeStrength=[]
    relativeStrengthIndicator=[]
    
    for i in range(len(data)):
        
        nextChange=(data[1]-data[0])
        changeList.append(nextChange)
        data.pop(0)
              
        if(len(data)-1==True):
            changeList.append(data[1]-data[0])
            break
    
    for i in range(len(changeList)):
        if(changeList[i]>0):
            upMovementList.append(changeList[i])
        else:
            upMovementList.append(0)
        if(changeList[i]<0):
            downMovementList.append(changeList[i]*-1)
        else:
            downMovementList.append(0)
    
    while(x<n):
        
        sumUp+=upMovementList[x]
        sumDown+=downMovementList[x]
        x+=1

    averageUpwardList.append(sumUp/n)
    averageDownwardList.append(sumDown/n)
    
    
    
    while(a<len(upMovementList)):

        averageUpwardList.append((averageUpwardList[b]*(n-1)+upMovementList[c])/n)
        averageDownwardList.append((averageDownwardList[b]*(n-1)+downMovementList[c])/n)
        b+=1
        c+=1
        a+=1
    
    for i in range(len(averageDownwardList)):
        relativeStrength.append(averageUpwardList[i]/averageDownwardList[i])
        relativeStrengthIndicator.append(100-(100/(relativeStrength[i]+1)))
          
    return ("RELATIVE STRENGTH INDICATOR:", relativeStrengthIndicator)
    
BoeingData=pd.read_csv("BA.csv")

adjCloseBoeing=[]

for i in range(len(BoeingData.adjClose)):
    
    adjCloseBoeing.append(BoeingData.adjClose[i])
    
print("RSI of Boeing:", RSI(adjCloseBoeing,14))






    