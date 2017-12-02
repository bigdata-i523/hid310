import numpy as np
import pandas as pd
import csv

df = pd.read_csv('house.csv')

def dwaste():
    if row['dvotes'] > row['rvotes']:
        val = row['dvotes'] - ((row['dvotes'] + row['rvotes']) * .5)
    else: 
        val = row['dvotes']
    return val
        
def rwaste():
    if row['rvotes'] > row['dvotes']
        val = row['rvotes'] - ((row['dvotes'] + row['rvotes']) * .5)
    else:
        val = row['rvotes']
    return val
        
def gap():
    val = (df.apply(rwaste) - df.apply(dwaste))/(df['dvotes']+df['rvotes'])
    print(val)
    
gap    
