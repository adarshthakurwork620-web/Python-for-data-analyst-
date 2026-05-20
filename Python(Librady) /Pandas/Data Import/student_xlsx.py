import pandas as pd

data={
    "Name":["Amam","Riya","Rahul","Vipul"],
    "Marks":[60,50,70,80],
    "roll":[1,2,3,4]
}
df=pd.DataFrame(data)
df.to_excel("student.xlsx",index=False)
print("with index")
print()
print(df)  
print()
print("without index")
print()
print(df.to_string(index=False))
print()
print("file is save")