import pandas as pd

data = pd.read_csv("pandas/data/employees.csv")


#check missing values
missing_values=data.isnull().sum()
print(missing_values)

# duplicates count
DC = data.duplicated().sum()
print(DC)

# duplicate rows 
DF=data[data.duplicated()]
print(DF)

# remove
R=data.drop_duplicates(inplace=True)
print(R)

C = data.columns
print(C)

# filter
flt = data[data["Gender"] == "male"]
print(flt)

# advanced filter
aflt = data[(data["Gender"]=="female") & (data["Age"] >25) & (data["Age"]<27)]
print(aflt)

# select
sel = data.loc[:,["Age" , "Gender"]]
print(sel)