import pandas as pd

df = pd.read_csv('house.csv')
df2 = pd.read_csv('senate.csv')
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
#adding these values to our dataframes
df['rwaste'] = df.apply(rwaste, axis=1)
df['dwaste'] = df.apply(dwaste, axis=1)

df2['rwaste'] = df2.apply(rwaste, axis=1)
df2['dwaste'] = df2.apply(dwaste, axis=1)
#applying the efficiency gap formula
rtotal = df['rwaste'].sum()
dtotal = df['dwaste'].sum()
bottom = df['rvotes'].sum() + df['dvotes'].sum()
rtotal2 = df2['rwaste'].sum()
dtotal2 = df2['dwaste'].sum()
bottom2 = df2['rvotes'].sum() + df2['dvotes'].sum()

final = ((dtotal-rtotal)/bottom)*100
final2 = ((dtotal2-rtotal2)/bottom2)*100

def eg():
    if final > 8:
        print("UNCONSTITUTIONAL GERRYMANDER")
    else:
        print("ACCEPTABLE")

def eg2():
    if final2 > 8:
        print("UNCONSTITUTIONAL GERRYMANDER")
    else:
        print("ACCEPTABLE")

#The result
print("Indiana Efficiency Gap Analysis")
print("Gerrymandering standard: gap > 8 percent")
print(" ")
print("House of Representatives:")
print("Democratic waste:", dtotal, "   Republican waste:", rtotal)
print("Total voters:", bottom)
print("Efficiency gap:", format(final, '.2f'), "percent")
eg()
print(" ")
print("State Senate Efficiency Gap:")
print("Democratic waste:", dtotal2, "   Republican waste:", rtotal2)
print("Total voters:", bottom2)
print("Efficiency gap:", format(final2, '.2f'), "percent")
eg2()
