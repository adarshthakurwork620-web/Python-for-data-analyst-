import pandas as pd 

data = {"Name":["Aman","Riya","Rahul"],
      "Salary":[10000,20000,30000]}

df = pd.DataFrame(data)
print(df)
# add 10% in salary
apply = df["Salary"]+df["Salary"].apply(lambda x: x*0.10)
print(apply)