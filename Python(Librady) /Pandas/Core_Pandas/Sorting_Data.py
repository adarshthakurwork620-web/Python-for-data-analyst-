import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")

print(df)
col = df.columns
print(col)
sorting = df.sort_values("Salary") # low to high...
print(sorting)

sorting1 = df.sort_values("Age",ascending=False) #  high to low 
print(sorting1)

# Find top 3 highest salary employees

sorting2 = df.sort_values("Salary",ascending=False).head(3) #  high to low 
print(sorting2)