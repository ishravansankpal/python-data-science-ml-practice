#  Objective
# Analyze the House Price Prediction dataset using descriptive statistics and data visualization techniques in Python.

# Tasks Performed
# - Computed standard deviation for each feature
# - Computed variance for each feature
# - Calculated percentiles using separate Python commands
# - Created histograms for all numerical features to visualize their distributions

# Dataset
# - House Price Prediction dataset


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("House Data.csv")

# Select only numeric columns
df = df.select_dtypes(include='number')

# Standard deviation
print(df.std())

# Variance
print(df.var())

# Percentiles
print(df.quantile([0.25,0.50,0.75]))

# Histogram for numeric columns
df.hist(figsize=(12,12))
plt.show()
