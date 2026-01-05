# 24. Perform the following operations using Python on a suitable data set,
# counting unique values of data, format of each column, converting variable
# data type (e.g. from long to short, vice versa), identifying missing values
# and filling in the missing values.

import pandas as pd

# Load the Titanic dataset from CSV file into a DataFrame
df = pd.read_csv('Titanic.csv')

# Display the first 5 rows of the dataset
print(df.head())

# Show number of unique values in each column
print("Unique values in each column")
print(df.nunique())

# Display data types of each column
print(df.dtypes)

# Convert 'Pclass' column to float type
df['Pclass'] = df['Pclass'].astype(float)

# Check data types again to confirm conversion
print(df.dtypes)

# Check for missing values in each column
print(df.isnull().sum())

# Fill missing values in 'Age' with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Remove 'Cabin' column (if it exists)
df.drop(columns=['Cabin'], inplace=True, errors='ignore')

# Fill missing values in 'Fare' with the median fare
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# Check again for missing values after cleaning
print(df.isnull().sum())



