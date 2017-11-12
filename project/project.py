import pandas as pd
df = pd.read_csv('federalelections2012.csv', names=['state', 'district', 'lastname', 'party', 'votes')

#need to insert a way to add statewide vote totals for each party
=SUMPRODUCT(SUMIF(state:state;List;B:B))

if 'party'="R" then 'votes'=rvotes
  elsif 'party'="D" then 'votes'=dvotes                                                    
 #determining the state winner determines the formula we use to find the wasted votes                                                   
for district 
  if "rvotes">"dvotes" then winner="rep" 
  elsif dvotes>rvotes then winner="dem"
                                                    
#determining number of wasted votes
if winner="rep" then rwaste=rvotes-(dvotes+1)
  dwaste=dvotes
elsif winner=dem then dwaste=dvotes-(rvotes+1)
  rwaste=rvotes

#the efficiency gap formula                                                
EG=(rwaste-dwaste)/rvotes+dvotes

#determining republican or democrat efficiency gap advantage                                                    
if EG>0 then advantage="democrat"
  elsif EG<0 then advantage="republican"
  elsif EG==0 then advantage="no advantage"
                                                    
#determining if efficiency gap is dire enough to constitute illegal gerrymandering
if abs(EG)>=.07
  then gerrymandered="yes"
