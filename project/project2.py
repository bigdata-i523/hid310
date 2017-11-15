import pandas as pd
import numpy as np
import csv
data = np.genfromtxt("federalelections2012.csv", dtype=None, delimiter=',', names=True, skip_header=0) 

def wastedvotes(
  if data['state']==data['state'] and data['district']==data['district']:
    (min(data['votes'])+max(data['votes'])-(min(data['votes'])+1)))
  else quit() 
                          
def eg(
    if data['state']==data['state']:
        (wastedvotes(data['state']['party']=="R"])-wastedvotes(data['state']['party']=="D"]))/data['votes']
    else quit())
    
def advantage(
    if eg>0:
        print("Democrat")
    elif eg<0:
        print("Republican")
    else: print("No advantage"))
                 
def gerrymander(
    if abs(eg())>=.07:
        print("Yes")
    else: print("No")
    
print([data['state'], eg(data['state']), advantage(data['state']), gerrymander(data['state'])])
