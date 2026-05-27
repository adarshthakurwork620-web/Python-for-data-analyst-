import pandas as pd 
df=pd.read_excel("pandas/combined_data.xlsx")
print(df)

print(df["Resturant_ID"].nunique())
print(df["deliver_status"].nunique())
print(df["quantity"].nunique())
print(df["payment_method"].nunique())