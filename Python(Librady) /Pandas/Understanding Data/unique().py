import pandas as pd 
df=pd.read_excel("pandas/combined_data.xlsx")
print(df)

print(df["Resturant_ID"].unique())
print(df["deliver_status"].unique())
print(df["quantity"].unique())
print(df["payment_method"].unique())