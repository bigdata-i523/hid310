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
   if row['DemWasted']>row['RepWasted']:
      val = row['DemWasted']-row['RepWasted']/(row['rvotes']+row['dvotes'])
   elif row['DemWasted']<row['RepWasted']:
      val = row['RepWasted']-row['DemWasted']/(row['rvotes']+row['dvotes'])
   else:
      val = 0
   return val

#Regardless of efficiency gap score, the party with fewer wasted votes in a state has the district advantage.   
def advantage(row):
   if row['DemWasted']>row['RepWasted']:
      val = "Republicans"
   elif row['DemWasted']<row['RepWasted']:
      val = "Democrats"
   else:
      val = "Even"
   return val
      
newdata = data.groupby('state')
newdata['Efficiency_Gap'] = data.apply(eg, axis=1)
newdata['Advantage'] = data.apply(advantage, axis=1)

newdata
