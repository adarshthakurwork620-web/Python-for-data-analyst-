"""
What is Scatter Plot ?

--> Scatter Plot is used show the relationship between two numerical 
    values using dots.

When do you use a Scatter Plot?

--> I can used Scatter plot, when i can find relationship between two 
    numerical variables, such as exprience and salary.

x = first numeric column
y = second numeric column

"""
import matplotlib.pyplot as plt
import pandas as pd 
data = {
      "Study_hour":[1, 2, 3, 4, 5, 6, 7, 8],
      "Marks"     :[35, 40, 50, 55, 65, 70, 80, 85]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8,5))
plt.scatter(df["Study_hour"],df["Marks"])
plt.title("Relation bewteen Study_hour and Marks")
plt.xlabel("Study hour")
plt.ylabel("Marks")
plt.grid(axis="both")
plt.show()
      
"""
3 insights:-

1. Study hours badhne par marks badh rahe hain ya nahi?
-->yes marks in increased.

2. Highest marks kitne hain?
-->the highest marks is 85.

3. Relationship positive, negative, ya no relationship?
-->they have positive relation.

"""      
