import pandas as pd

d2=pd.read_excel("pandas/data/February_23.xlsx")
d3=pd.read_excel("pandas/data/January_23.xlsx")
d4=pd.read_excel("pandas/data/March_2023.xlsx")
d1=pd.read_excel("pandas/data/April_23.xlsx")
comb=pd.concat([d1,d2,d3,d4])
print(comb)