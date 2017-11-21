import pandas as pd
import numpy as np
import csv
data = np.genfromtxt("federalelections2012.csv", dtype=None, delimiter=',', names=True, skip_header=0) 

#This function finds the wasted votes from each state race. The wasted votes are every vote for a losing party, and every vote for the winning party beyond those necessary for victory.
def dwaste():
   if data['dvotes']>data['rvotes']:
      return data['dvotes']-((data['rvotes']+data['dvotes'])*.51)
   elsif data['dvotes']<data['rvotes']:
      return data['dvotes']
   else: quit()
      
def rwaste():
   if data['rvotes']>data['dvotes']:
      return data['rvotes']-((data['dvotes']+data['rvotes'])*.51)
   elsif data['rvotes']<data['dvotes']:
      return data['rvotes']
   else: quit()
      
def eg():
  if dwaste()>rwaste():
     return (dwaste()-rwaste())/(data['dvotes']+data['rvotes'])
   elsif dwaste()<rwaste():
     return (rwaste()-dwaste())/(data['dvotes']+data['rvotes'])
   else:
      return 0
   
def advantage():
   if dwaste()>rwaste():
      print("Republicans")
   elsif dwaste()<rwaste():
      print("Democrats")
   else: print("Even")
      

   
   if data['state']==data['state'] and data['district']==data['district']:
    if data['votes']==max(data['votes']):
      max(data['votes'])-(min(data['votes'])+1)
    elif data['votes']==min(data['votes']):
      min(data['votes'])

#This function finds the efficiency gap. The efficiency gap is the wasted votes for party A minus the wasted votes for party B, divided by the total number of votes in the state. 
def eg():
    if data['state']==data['state']:
        (wastedvotes(data['state']['party']=="R")-wastedvotes(data['state']['party']=="D"))/data['votes']
    else: quit()

#Since we fixed in the eg function that democrat wasted votes are always subtracted from republican wasted votes, we need a way of determining the advantage. If the number of wasted votes is positive, republicans had more, and thus the democrats have the advantage. If it is negative, democrats had more, and republicans have the advantage. If it is even, there is no advantage (this is not likely to happen).
def advantage():
    if eg(data['state'])>0:
        print("Democrat")
    elif eg(data['state'])<0:
        print("Republican")
    else: print("No advantage")

#The threshold for an excessively gerrymandered is 7 percent efficiency gap. We find this by finding the absolute value of eg, as this function is party agnostic, it is a simple binary whether the state is gerrymandered or not. The advantage function determines who it is gerrymandered in favor of.
def gerrymander():
    if abs(eg(data['state']))>=.07:
        print("Yes")
    else: print("No")

#This will generate our list of all states, with columns indicating that state's efficiency gap score, the party advantage, and a yes/no column whether the state is excessively gerrymandered.
finallist = ([data['state'], eg(data['state']), advantage(data['state']), gerrymander(data['state'])])
print(finallist.sort(
   key = lambda l: (l[1], l[0])
)
