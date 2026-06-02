import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")

print(df)
col = df.columns
print(col)

# Lowercase
df["name"] = df["First Name"].str.lower()
print(df["name"])

# Contains Text
df["Email"]=df["Email"].str.contains("gmail")
print(df["Email"])

# Replace Text
df["Department"]=df["Department"].str.replace("Product", "p")
print(df["Department"])