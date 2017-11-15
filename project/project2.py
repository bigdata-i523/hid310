import pandas as pd
import numpy as np
import csv
data = np.genfromtxt("federalelections2012.csv", dtype=None, delimiter=',', names=True, skip_header=0) 

def wastedvotes(
  if data['state']=data['state'] and data['district']=data['district']:
    (min(data['votes'])+max(data['votes'])-(min(data['votes'])+1)))
  else quit() 
                          
def eg(
    if data['state']=data['state']:
        (wastedvotes(data['state', 'party'="R"]-data['state', 'party'="D")/data)
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
    
print([state, eg(state), advantage(state), gerrymander(state)])
