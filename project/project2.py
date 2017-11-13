import pandas as pd
import numpy as np
df = pd.read_csv('federalelections2012.csv')
    state=df.state
    district=df.district
    lastname=df.lastname
    party=df.party
    votes=df.votes   

def state(state)
                 
def votes(votes)
                 
def wastedvotes(
    if state=state and district=district:
        max(votes)
            if max(party="R"):
                (votes("D")+(votes("R")-(votes("D")+1)))
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
