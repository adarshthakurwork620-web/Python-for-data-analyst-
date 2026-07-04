"""
What is subplot in Matplotlib?

Subplot is uses to display multiple chart in single display. 

Why do we use subplots?

when we want to show multiple related charts together, such as sales trend,
product comparison.

"""
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphone"],
    "Sales": [50, 120, 40, 80],
    "Profit": [10, 35, 8, 20]
}

df = pd.DataFrame(data)

plt.figure(figsize=(6,5))

#first graph
plt.subplot(2,2,1)
plt.bar(df["Product"],df["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product vs Sales")

#second graph
plt.subplot(2,2,3)
plt.plot(df["Product"],df["Profit"],marker="o")
plt.xlabel("Product")
plt.ylabel(" Profit")
plt.title("Product vs Profit")
plt.grid()


plt.tight_layout()
plt.show()

"""
3 insights:-

1. Highest sales product? --> Mobile
2. Highest profit product? --> Mobile
3. Sales और Profit में same product top है या different? -->Same product (Mobile)

"""