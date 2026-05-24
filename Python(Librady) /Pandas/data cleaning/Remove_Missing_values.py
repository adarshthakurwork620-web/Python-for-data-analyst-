import pandas as pd
import numpy as np

data={
    "Name":["Amam","Riya","Rahul","Vipul"],
    "Marks":[60,70,80,np.nan],
    "roll":[1,2,3,4]
}
df=pd.DataFrame(data)
#find missing value
missing_value=df.isnull()
print(missing_value.sum())
#remove missing value
fmv=df.dropna()# remove null row...
print(fmv)

