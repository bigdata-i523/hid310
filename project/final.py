import pandas as pd

df = pd.read_csv('house.csv')

def dwaste(row):
    if row['dvotes'] > row['rvotes']:
        val = row['dvotes'] - ((row['dvotes'] + row['rvotes']) * .5)
    else: 
        val = row['dvotes']
    return val

def rwaste(row):
    if row['rvotes'] > row['dvotes']:
        val = row['rvotes'] - ((row['dvotes'] + row['rvotes']) * .5)
    else:
        val = row['rvotes']
    return val

df['rwaste'] = df.apply(rwaste, axis=1)
df['dwaste'] = df.apply(dwaste, axis=1)

rtotal = df['rwaste'].sum()
dtotal = df['dwaste'].sum()
bottom = df['rvotes'].sum() + df['dvotes'].sum()

print("The efficiency gap score for the Indiana state house district map is:")
print((dtotal-rtotal)/bottom)
print("This does not reach the threshold for illegal gerrymandering.")
