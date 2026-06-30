"""
What is a Histogram?

--> A histogram is used to show the distribution of numerical data. 
    It groups continuous values into ranges called bins 
    and shows how many values fall into each range.

When do you use a Histogram?

--> I use a histogram when I want to understand the distribution 
    or spread of numeric data, such as salary.

"""
import pandas as pd 
import matplotlib.pyplot as plt

data={
    "Age": [22, 25, 27, 29, 30, 32, 35, 36, 40, 45, 48, 50]
}

df =pd.DataFrame(data)

plt.figure(figsize=(8,5))
plt.hist(df["Age"],bins=4)
plt.xlabel("Age Range")
plt.ylabel("Number of Employees")
plt.title("Age distribution")
plt.show()

"""
3 insights:-

1. Youngest age?-->22
2. Oldest age?-->50
3. Age values mostly kis range me hain?-->29-36

"""