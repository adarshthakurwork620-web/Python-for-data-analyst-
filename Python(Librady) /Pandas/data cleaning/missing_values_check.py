import pandas as pd
df=pd.read_excel("pandas/combined_data.xlsx")
print(df)

#find missing values...
missing_values = df.isnull()
print(missing_values)

# har column me kitne missing values hai..
print(missing_values.sum())

#agr koi row me missing values hai toh fill aise krte  hai...
df["quantity"] = df["quantity"].fillna(df["quantity"].mean())
print(df["quantity"])