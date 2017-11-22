import pandas as pd
import numpy as np
import csv
data = np.genfromtxt("congressdata2012.csv", dtype=None, delimiter=',', names=True, skip_header=0) 

#We need to find number of wasted votes for each party. Wasted votes are, for the winning party in a given race, every vote above the number necessary to win. On the flip side, every vote for a losing party is considered wasted.

#Democrat wasted votes.
def dwaste():
   if data['dvotes']>data['rvotes']:
      return data['dvotes']-((data['rvotes']+data['dvotes'])*.51)
   elif data['dvotes']<data['rvotes']:
      return data['dvotes']
   else: 
      return 0

#Republican wasted votes
def rwaste():
   if data['rvotes']>data['dvotes']:
      return data['rvotes']-((data['dvotes']+data['rvotes'])*.51)
   elif data['rvotes']<data['dvotes']:
      return data['rvotes']
   else: 
      return 0

#This contains the efficiency gap formula, which is the number of wasted votes from party A minus the wasted votes from party B, divided by the total number of votes in a given state.       
def eg():
  if dwaste()>rwaste():
     return (dwaste()-rwaste())/(data['dvotes']+data['rvotes'])
  elif dwaste()<rwaste():
     return (rwaste()-dwaste())/(data['dvotes']+data['rvotes'])
  else:
     return 0

#Regardless of efficiency gap score, the party with fewer wasted votes in a state has the district advantage.   
def advantage():
   if dwaste()>rwaste():
      print("Republicans")
   elif dwaste()<rwaste():
      print("Democrats")
   else: print("Even")

#The efficiency gap authors determined 7percent wastedvotes/totalvotes to be the threshold for illegal gerrymandering     
def gerrymander():
   if eg()>=.07:
      print("Yes")
   else: print("")

#Create a list with every state's efficiency gap score, advantage, and gerrymandering yes/no. Sort in order of efficiency gap score.     
print(data.groupby('state')[eg(), advantage(), gerrymander()].apply(list))
