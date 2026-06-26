import pandas as pd
import matplotlib.pyplot as plt
#pyplot = plotting module

Data ={
         "months":["Jan", "Feb", "Mar", "Apr"],
         "sales" :[100, 150, 120, 180],
      }

df = pd.DataFrame(Data)
#Add Title
plt.title("Monthly sales")
# X Label
plt.xlabel("months")
# # Y Label
plt.ylabel("sales")

plt.plot(df["months"],df["sales"])
plt.show()