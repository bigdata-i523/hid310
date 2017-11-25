import pandas as pd
import numpy as np
import csv
data = pd.read_csv("congressdata2012.csv") 

#We need to find number of wasted votes for each party. Wasted votes are, for the winning party in a given race, every vote above the number necessary to win. On the flip side, every vote for a losing party is considered wasted.

#Democrat wasted votes.
def dwaste(row):
   if row['dvotes']>row['rvotes']:
      val = data['dvotes']-((data['rvotes']+data['dvotes'])*.51)
   elif row['dvotes']<row['rvotes']:
      val = row['dvotes']
   else: 
      val = 0
   return val

#Republican wasted votes
def rwaste(row):
   if row['rvotes']>row['dvotes']:
      val = row['rvotes']-((row['dvotes']+row['rvotes'])*.51)
   elif row['rvotes']<row['dvotes']:
      val = row['rvotes']
   else: 
      val = 0
   return val
   
data['RepWasted'] = data.apply(rwaste, axis=1)
data['DemWasted'] = data.apply(dwaste, axis=1)

#This contains the efficiency gap formula, which is the number of wasted votes from party A minus the wasted votes from party B, divided by the total number of votes in a given state.       
def eg(row):
   if dwaste()>rwaste():
      return (dwaste()-rwaste())
   elif dwaste()<rwaste():
      return (rwaste()-dwaste())
   else:
      return 0
   
#Regardless of efficiency gap score, the party with fewer wasted votes in a state has the district advantage.   
def advantage(row):
   if dwaste()>rwaste():
      print("Republicans")
   elif dwaste()<rwaste():
      print("Democrats")
   else: print("Even")

#The efficiency gap authors determined 7percent wastedvotes/totalvotes to be the threshold for illegal gerrymandering     
def gerrymander():
   if eg()/(data['rvotes']+data['dvotes'])>=.07:
      print("Yes")
   else: print("")

#Create a list with every state's efficiency gap score, advantage, and gerrymandering yes/no. Sort in order of efficiency gap score.     
prelim = [data, eg(), advantage(), gerrymander()]
finallist = prelim.groupby['state']
print(finallist)

