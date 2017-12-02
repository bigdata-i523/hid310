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

print("The efficiency gap score for Indiana's state house district map is:")
print((df['dwaste'].sum() - df['rwaste'].sum())/(df['rvotes'].sum()+df['dvotes'].sum())
print("This does not meet the threshold for illegal gerrymandering.")
