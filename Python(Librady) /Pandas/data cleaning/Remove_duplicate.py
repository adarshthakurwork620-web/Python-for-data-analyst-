import pandas as pd
df=pd.read_excel("pandas/combined_data.xlsx")
d=df.drop_duplicates(subset="Resturant_ID")
print(d)
print(df.duplicated(subset="Resturant_ID").sum())