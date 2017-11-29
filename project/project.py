import pandas as pd
import numpy as np
import csv
data = pd.read_csv("congressdata2012.csv")


def dwaste(row):
    if row['dvotes'] > row['rvotes']:
        val = data['dvotes'] - ((data['rvotes'] + data['dvotes']) * .51)
    elif row['dvotes'] < row['rvotes']:
        val = row['dvotes']
    else:
        val = 0
    return val


def rwaste(row):
    if row['rvotes'] > row['dvotes']:
        val = row['rvotes'] - ((row['dvotes'] + row['rvotes']) * .51)
    elif row['rvotes'] < row['dvotes']:
        val = row['rvotes']
    else:
        val = 0
    return val

data['RepWasted'] = data.apply(rwaste, axis=1)
data['DemWasted'] = data.apply(dwaste, axis=1)


def eg(row):
    if row['DemWasted'] > row['RepWasted']:
        val = row['DemWasted'] - row['RepWasted'] / (row['rvotes'] + row['dvotes'])
    elif row['DemWasted'] < row['RepWasted']:
        val = row['RepWasted'] - row['DemWasted'] / (row['rvotes'] + row['dvotes'])
    else:
        val = 0
    return val


def advantage(row):
    if row['DemWasted'] > row['RepWasted']:
        val = "Republicans"
    elif row['DemWasted'] < row['RepWasted']:
        val = "Democrats"
    else:
        val = "Even"
    return val

newdata = data.groupby('state')
newdata['Efficiency_Gap'] = newdata.apply(eg, axis=1)
newdata['Advantage'] = newdata.apply(advantage, axis=1)
newdata.sort_values(by='Efficiency_Gap', ascending=0)

print(newdata)
