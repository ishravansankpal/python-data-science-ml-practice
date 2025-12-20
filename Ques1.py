# import pandas as pd

# # Read CSV
# df = pd.read_csv("Titanic.csv")

# print("\n--- First 5 Rows ---")
# print(df.head())

# print("\n--- Data types of each column ---")
# print(df.dtypes)

# print("\n--- Indexing Example (Selecting Age & Fare columns) ---")
# print(df[['Age','Fare']].head())

# print("\n--- Sorting by Age ---")
# print(df.sort_values('Age').head())

# print("\n--- Describe attributes ---")
# print(df.describe())

import pandas as pd 

df = pd.read_csv('Titanic.csv')

print(df.head())

print(df.describe())

print(df.dtypes)

print(df.shape)