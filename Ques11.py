## Objective
To analyze the Iris flower dataset by identifying feature types and visualizing feature distributions using histograms.

# Description
# This experiment explores the Iris dataset to understand its structure and feature characteristics.  
# Each feature is analyzed based on its data type, and histograms are generated to visualize the distribution of values.

# Dataset
# - Iris Flower Dataset (inbuilt / CSV-based)

# Features and Types
# The dataset contains the following features:
# - Sepal Length – Numeric
# - Sepal Width – Numeric
# - Petal Length – Numeric
# - Petal Width – Numeric
# - Species – Nominal (categorical)

# Tasks Performed
# - Listed all features present in the dataset along with their data types
# - Generated a histogram for each numeric feature
# - Observed and analyzed feature distributions

# Tools & Libraries
# - Python
# - Pandas
# - Matplotlib / Seaborn

# Purpose
# This analysis provides insight into the distribution and spread of Iris dataset features, which is useful for data understanding and preprocessing in machine learning workflows.



import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('IRIS.csv')

# 2. List features and types
print(df.dtypes)

# 3. Histogram
df.hist(figsize=(10,10))
plt.show()
