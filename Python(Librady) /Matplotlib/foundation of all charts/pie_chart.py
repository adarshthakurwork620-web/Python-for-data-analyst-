"""
What is a Pie Chart?

-> A pie chart is used to show parts of a whole.

When do you use a Pie Chart?

-> I use a pie chart when I want to show percentage distribution 
   or share of total, such as gender distribution.

"""
import pandas as pd
import matplotlib.pyplot as plt

data ={
        "Category": ["Food", "Travel", "Shopping", "Rent"],
        "Expense": [5000, 3000, 2000, 10000]
      }
df= pd.DataFrame(data)

plt.figure(figsize=(8,5))
plt.title("Expense by Category")
plt.pie(df["Expense"],labels=df["Category"],autopct="%1.1f%%",startangle=90)
# autopct="%1.1f%%" ->percentage show
# startangle=90 = chart rotate/start position
plt.show()

"""
3 insights:-

1. Highest expense category?-->Rent
2. Lowest expense category?-->Shopping
3. Rent ka total expense me approx share kitna hai?
-->Rent ka total expense approx 50%.

"""