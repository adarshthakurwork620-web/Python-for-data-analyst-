import pandas as pd 

df=pd.read_csv("pandas/data/employees.csv")


# Calculate average Salary by Department.

Salary_by_Department = df.groupby("Department")["Salary"].mean().reset_index()
print(Salary_by_Department)

print("----------------------------------------------------------------")
# Count Department by Gender using groupby().

Department_by_Gender = df.groupby("Gender")["Department"].count().reset_index()
print(Department_by_Gender)

print("----------------------------------------------------------------")
# Find total Salary by Department.

total_Salary_by_Department = df.groupby("Department")["Salary"].sum().reset_index()
print(total_Salary_by_Department)

print("----------------------------------------------------------------")
# Find average Age by Gender.

Age_by_Gender = df.groupby("Gender")["Age"].mean().reset_index()
print(Age_by_Gender)

print("----------------------------------------------------------------")
# Find the Department with the highest Salary.

Department_by_highest_Salary = df.groupby("Department")["Salary"].max().reset_index()
print(Department_by_highest_Salary)

print("----------------------------------------------------------------")
# Find total number of employees in each Department.

total_number_of_employees_by_Department = df.groupby("Department").size().reset_index(name="Total number of employees")
print(total_number_of_employees_by_Department)

print("----------------------------------------------------------------")
# Find Job Title wise average Salary.

Job_Title_wise_average_Salary = df.groupby("Job Title")["Salary"].mean().reset_index()
print(Job_Title_wise_average_Salary)

print("----------------------------------------------------------------")
# Which Gender has higher  Salary?

Gender_by_highest_Salary = df.groupby("Gender")["Salary"].max().reset_index()
print(Gender_by_highest_Salary)