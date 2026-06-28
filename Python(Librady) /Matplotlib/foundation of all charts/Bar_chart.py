"""
What is a Bar Chart?

-> A bar chart is used to compare values across different categories.

When do you use a Bar Chart?

-> I use a bar chart when I want to compare categories, such as sales by 
product.

"""
import pandas as pd
import matplotlib.pyplot as plt

data ={
        "Product": ["Laptop", "Mobile", "Tablet", "Headphone"],
        "Sales": [50, 120, 40, 80]
      }

df= pd.DataFrame(data)
plt.figure(figsize=(8,5))
plt.bar(df["Product"],df["Sales"])
plt.title("Product by Sales")
plt.xlabel("product")
plt.ylabel("Sales")
plt.grid(axis="y")
plt.show()

"""
3 insights:-

1. Highest selling product?-->Mobile(120)
2. Lowest selling product?-->Tablet(40)
3. Mobile sales Headphone sales से कितनी ज्यादा है?--> 120-80 = 40↑

"""