import pandas as pd 
Data = {"Name":["Aman","Riya","Rahul","Pooja"],
        "Department":["IT","HR","IT","HR"],
        "Gender":["Male","Female","Male","Female"],
        "Salary":[20000,18000,25000,22000]
       }

df = pd.DataFrame(Data)
print(df)

print("------------------------------------------------")
# Avg salary by Gender
avg = pd.pivot_table(df, values="Salary", index="Department")
print(avg)
print("------------------------------------------------")
# Total Salary by Department
# values  = kya calculate karna , index   = row groups
# columns = side groups , aggfunc = kaise calculate karna
TD = pd.pivot_table(                                                 
    df,
    values="Salary",
    index="Department",
    aggfunc="sum"
)
print(TD)
print("------------------------------------------------")
#  Count employees by Department
count = pd.pivot_table(df,values="Name",index="Department",aggfunc="count")
print(count)
print("------------------------------------------------")
# Avg salary by Department and Gender
avg_salary = pd.pivot_table(df,values="Salary" , index="Department" , columns="Gender", aggfunc="mean")
print(avg_salary)
print("------------------------------------------------")
#Max salary by Department
max = pd.pivot_table(df, values="Salary", index="Department",aggfunc="max")
print(max)