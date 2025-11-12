# how many women were more than 40 years old ?


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tested.csv")

women_over_40 = data[(data["Sex"] == "female") & (data["Age"] > 40)]

count = women_over_40.shape[0]
print("Number of women aged more than 40 years on the Titanic:", count)

other_people = data.shape[0] - count

labels = ["Women over 40", "Other People"]
sizes = [count, other_people]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Women aged more than 40 years on the Titanic")
plt.show()
