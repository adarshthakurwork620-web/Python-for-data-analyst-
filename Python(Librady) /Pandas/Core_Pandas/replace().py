import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")

print(df)
col = df.columns
print(col)

# Single Value Replace

df["Department"] = df["Department"].replace("Product", "p")
print(df["Department"])

#  Before Convert male/female to MALE/FEMALE
print(df["Gender"])
# Convert male/female to MALE/FEMALE

df["Gender1"] = df["Gender"].replace({"male":"MALE","female":"FEMALE"})
print(df["Gender1"])