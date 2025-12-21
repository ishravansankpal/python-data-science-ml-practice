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


# import pandas as pd

# df = pd.read_csv('Telecom Churn.csv')

# print(df.head())

# print(df.columns)

# col = df['account length']

# print('Minimum:', col.min())

# print('Maximum:', col.max())

# print('Mean:', col.mean())

# print('Range:', col.max() - col.min())

# print('Standard Deviation:', col.std())

# print('Variance:', col.var())

# print('Percentile of 50%:', col.quantile(0.5))