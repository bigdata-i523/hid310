import pandas as pd

df = pd.read_csv('house.csv')
#The efficiency gap is the wasted votes from party a minus those from party b, divided by the total number of votes. A wasted vote is any vote cast for a losing candidate, or any vote for a winning candidate beyond the threshold needed to win.
#Finding democrat wasted votes:
def dwaste(row):
    if row['dvotes'] > row['rvotes']:
        val = row['dvotes'] - ((row['dvotes'] + row['rvotes']) * .5)
    else: 
        val = row['dvotes']
    return val
#finding republican wasted votes:
def rwaste(row):
    if row['rvotes'] > row['dvotes']:
        val = row['rvotes'] - ((row['dvotes'] + row['rvotes']) * .5)
    else:
        val = row['rvotes']
    return val
#adding these values to our dataframe
df['rwaste'] = df.apply(rwaste, axis=1)
df['dwaste'] = df.apply(dwaste, axis=1)
#applying the efficiency gap formula
rtotal = df['rwaste'].sum()
dtotal = df['dwaste'].sum()
bottom = df['rvotes'].sum() + df['dvotes'].sum()
#The result
print("The efficiency gap score for the Indiana state house district map is:")
print((dtotal-rtotal)/bottom)
print("This does not reach the threshold for illegal gerrymandering.")
