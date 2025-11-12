#import the required libraries numpy, pandas, matplotlib
# using numpy create array and prform math poerations
# using pandas craete a data frame and perform filtering and analysis
# using matplot lib using visual representaion of the data 


import numpy as np
import pandas as pd
import matplotlib as plt

arr = np.array([10, 20, 30, 40, 50])
arr_squared = arr ** 2
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
print("Array:", arr)
print("Squared:", arr_squared)
print("Sum:", arr_sum)
print("Mean:", arr_mean)

# pandas 


df = pd.read_csv('tested.csv')
print(df.head())  


first_numeric_col = df.select_dtypes(include='number').columns[0]
mean_val = df[first_numeric_col].mean()
filtered_df = df[df[first_numeric_col] > mean_val]
print(f"Rows where {first_numeric_col} > mean:", len(filtered_df))
print(df.describe())

# matplotlib

plt.figure(figsize=(8,4))
plt.hist(df[first_numeric_col], bins=20, color='skyblue', edgecolor='black')
plt.title(f'Histogram of {first_numeric_col}')
plt.xlabel(first_numeric_col)
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


