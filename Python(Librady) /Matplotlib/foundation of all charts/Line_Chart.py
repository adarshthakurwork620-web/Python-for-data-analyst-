"""
What is a Line Chart?

A line chart is used to show trends or changes in data over time. It connects data points with lines, making it easy to understand whether values are increasing, decreasing, or fluctuating.

"""

'''
When do you use Line Chart?

I use a line chart when the data is ordered or time-based, such as monthly sales, yearly revenue, daily temperature, or website traffic.
'''

import pandas as pd
import matplotlib.pyplot as plt
#pyplot = plotting module

Data ={
         "months":["Jan","Feb","Mar","Apr","May","Jun"],
         "sales" :[120,180,160,220,250,240],
      }

df = pd.DataFrame(Data)
#Add Title
plt.title("Monthly sales")
# X Label
plt.xlabel("months")
# # Y Label
plt.ylabel("sales")

plt.plot(df["months"],df["sales"], marker="o")
plt.show()

'''
3 insights:-

1. Highest sales month?--->May
2. Lowest sales month?--->Jan
3. Overall trend increasing or fluctuating? 

---> fluctuating but mostly increasing
Jan 120 → Feb 180 ↑
Feb 180 → Mar 160 ↓
Mar 160 → Apr 220 ↑
Apr 220 → May 250 ↑
May 250 → Jun 240 ↓

'''

