import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")

#One Column Rename
rename = df.rename(columns= {"Years Of Experience":"Experience"}) #अगर inplace=True नहीं दिया तो original df नहीं बदलेगा।

print(rename)
#Multiple Columns Rename
rename1 = df.rename(columns= {"Years Of Experience":"Experience",
                   "Job Title":"Role"},inplace=True)  #Permanent Change (inplace=True)

print(rename1)
