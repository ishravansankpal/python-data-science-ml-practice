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


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('House Data.csv')

# print(df.head())

# print(df.dtypes)

# new_df = df.select_dtypes(include = 'number') 

# print(new_df.dtypes)

# print(new_df.std())

# print(new_df.var())

# print(new_df.quantile([0.25,0.50,0.75]))

# df.hist(figsize=(12,12))
# plt.show()