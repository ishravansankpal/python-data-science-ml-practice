## Objective
Compute and analyze summary statistics for each feature in the Telecom Churn dataset using Python.

## Tasks Performed
- Calculated minimum and maximum values
- Computed mean and range
- Calculated standard deviation and variance
- Computed percentiles for numerical features
- Displayed each statistic using separate Python commands

## Dataset
- Telecom Churn dataset

import pandas as pd

# Load dataset
df = pd.read_csv("Telecom Churn.csv")

# Print all column names (optional, but useful)
print("Columns in dataset:\n", df.columns)

# Select a numerical column
col = df["account length"]

# Minimum
print("Minimum:", col.min())

# Maximum
print("Maximum:", col.max())

# Mean (Average)
print("Mean:", col.mean())

# Range (Max - Min)
print("Range:", col.max() - col.min())

# Standard Deviation
print("Standard Deviation:", col.std())

# Variance
print("Variance:", col.var())

# Percentiles
print("25th Percentile:", col.quantile(0.25))
print("50th Percentile (Median):", col.quantile(0.50))
print("75th Percentile:", col.quantile(0.75))


# print('Variance:', col.var())


# print('Percentile of 50%:', col.quantile(0.5))
