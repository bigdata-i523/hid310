import pandas as pd
import numpy as np
import csv
data = np.genfromtxt("federalelections2012.csv", dtype=None, delimiter=',', names=True, skip_header=0) 
                 
def wastedvotes(
    if data['state']=data['state'] and data['district']=data['district']:
       find max(data['votes'])
            if max(data['party']="R"):
                for data['votes', 'party'](data['votes'="D"]+(data['votes'="R")-(data['votes'="D"]+1)))
            else (votes("R")+(votes("D")-(votes("R")+1))))
                 
def eg(
    if state=state and district=district:
        state((wastedvotes("R")-wastedvotes("D"))/state(votes))
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
