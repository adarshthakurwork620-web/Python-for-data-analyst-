'''
What is a Box Plot?

--> A box plot is used to show the distribution, spread, median, 
    quartiles, and outliers of numerical data.

When do you use Box Plot?

--> I use a box plot when I want to check data spread and detect 
    outliers, such as unusual salaries, ages.

'''
import pandas as pd
import matplotlib.pyplot as plt

data ={"Marks": [35, 40, 42, 45, 50, 55, 60, 62, 65, 70, 85, 100]}

df =pd.DataFrame(data)

plt.figure(figsize=(6,5))
plt.boxplot(df["Marks"])
plt.title("Marks boxplot")
plt.ylabel("Marks")
plt.show()

"""
3 insights :-

1. Lowest marks?--> 35
2. Highest marks?--> 100
3. Kya koi outlier lag raha hai? -->100
"""