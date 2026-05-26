import pandas as pd 
df=pd.read_excel("combined_data.xlsx")
print(df)
print()
print("tell about statistics:")
print()
print(df.describe())