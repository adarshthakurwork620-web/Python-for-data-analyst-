import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")

print(df)
col = df.columns
print(col)

# Add ₹1000 to Salary
df["Salary"] = df["Salary"] + 1000

print(df["Salary"])

# String Update
df["Department"] = df["Department"].str.upper()

print(df["Department"])

# Normalize Names

df["Name"] = df["First Name"].str.title()
print(df["Name"])