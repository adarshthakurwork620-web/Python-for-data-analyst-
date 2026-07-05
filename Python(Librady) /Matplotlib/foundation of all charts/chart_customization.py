'''
Why is chart customization important?

--> Chart Customization improved readability and presentation quality.
    it improved understanding the chart by adding title,lable,legends, 
    grid lines, and proper formatting.

'''
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 180, 160, 220, 250, 240],
    "Profit": [20, 45, 35, 60, 75, 70]
}

df = pd.DataFrame(data)
plt.figure(figsize=(8,6))

plt.plot(df["Month"],df["Sales"], marker="o", linestyle="-",label="Sales")
plt.plot(df["Month"],df["Profit"], marker="s", linestyle="--",label="Profit")

plt.title("Monthly Sales and Profit Trend")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.grid()
plt.legend() #Legend बताता है कौन सी line किस data की है.

plt.tight_layout() #Charts overlap न हों, इसलिए use करते हैं.
plt.show()