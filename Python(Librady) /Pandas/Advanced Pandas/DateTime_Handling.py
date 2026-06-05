import pandas as pd 

data = {"Name":["Aman","Riya","Rahul"],
      "Joining_Date":["2023-01-15","15/03/2022","07-10-2021"]}

df = pd.DataFrame(data)
print(df)

print("------------------------")

# Convert to Date Format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"],dayfirst=True,format="mixed")

print(df["Joining_Date"])

print("------------------------")
year = df["Joining_Date"].dt.year #Get Year
date = df["Joining_Date"].dt.day  #Get day
month = df["Joining_Date"].dt.month #Get Month
print(month)
print("------------------------")

print(date)
print("------------------------")

print(year)

print("------------------------")
# Find employees who joined in 2023

employees = df[df["Joining_Date"].dt.year==2023]
print(employees)

print("------------------------")

# Sort by Joining_Date

sort = df.sort_values("Joining_Date")
print(sort)