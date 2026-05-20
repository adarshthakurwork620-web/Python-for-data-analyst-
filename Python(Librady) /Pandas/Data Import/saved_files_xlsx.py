import pandas as pd

d1=pd.read_excel("data/April_23.xlsx")
d2=pd.read_excel("data/February_23.xlsx")
d3=pd.read_excel("data/January_23.xlsx")
d4=pd.read_excel("data/March_2023.xlsx")
df=pd.concat([d1,d2,d3,d4],ignore_index=True)
df.to_excel("combined_data.xlsx",index=False)
print("file saved successsfully")