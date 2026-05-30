import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")

print(df)

df["Full_Name"] = df["First Name"] + " " + df["Last Name"]

print(df["Full_Name"])