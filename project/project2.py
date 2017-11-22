import pandas as pd
import numpy as np
import csv
data = np.genfromtxt("congressdata2012.csv", dtype=None, delimiter=',', names=True, skip_header=0) 

#This function finds the wasted votes from each state race. The wasted votes are every vote for a losing party, and every vote for the winning party beyond those necessary for victory.
def dwaste():
   if data['dvotes']>data['rvotes']:
      return data['dvotes']-((data['rvotes']+data['dvotes'])*.51)
   elif data['dvotes']<data['rvotes']:
      return data['dvotes']
   else: quit()
      
def rwaste():
   if data['rvotes']>data['dvotes']:
      return data['rvotes']-((data['dvotes']+data['rvotes'])*.51)
   elif data['rvotes']<data['dvotes']:
      return data['rvotes']
   else: quit()
      
def eg():
  if dwaste()>rwaste():
     return (dwaste()-rwaste())/(data['dvotes']+data['rvotes'])
  elif dwaste()<rwaste():
     return (rwaste()-dwaste())/(data['dvotes']+data['rvotes'])
  else:
     return 0
   
def advantage():
   if dwaste()>rwaste():
      print("Republicans")
   elif dwaste()<rwaste():
      print("Democrats")
   else: print("Even")
      
def gerrymander():
   if eg()>=.07:
      print("Yes")
   else: print("")
    
print(data.groupby('state')[eg(), advantage(), gerrymander()].apply(list))
