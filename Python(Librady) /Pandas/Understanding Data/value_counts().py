import pandas as pd 
df=pd.read_excel("pandas/combined_data.xlsx")
print(df)
print("tell about frequency:")
print(df["Resturant_ID"].value_counts())
print(df["deliver_status"].value_counts())
print(df["quantity"].value_counts())
print(df["payment_method"].value_counts())