# Objective
# Build a Decision Tree classifier step-by-step without using any machine learning libraries
# to analyze customer responses to a promotional offer in a cosmetics shop.

# Problem Description
# The dataset contains customer attributes such as age, income, gender, and marital status,
# along with a target variable indicating whether the customer purchased a new lipstick.

# Tasks Performed
# - Implemented a Decision Tree from scratch using Python
# - Calculated entropy and information gain manually
# - Identified the root node based on maximum information gain
# - Used the target variable **Buys** for classification

# Dataset
# - Customer purchase response dataset (cosmetics shop)

import pandas as pd
import math

# Load dataset
df = pd.read_csv("Lipstick.csv")

# Function to calculate entropy
def entropy(col):
    values = col.value_counts()
    total = len(col)
    return sum([ -(v/total) * math.log2(v/total) for v in values ])

# Total entropy of target
total_entropy = entropy(df['Buys'])

# Function to compute information gain
def info_gain(df, attribute, target):
    total = len(df)
    weighted_entropy = 0

    for value, subset in df.groupby(attribute):
        weighted_entropy += (len(subset)/total) * entropy(subset[target])
    
    return total_entropy - weighted_entropy

# Calculate IG for each attribute
attributes = ['Age', 'Income', 'Gender', 'Ms']
gains = {attr: info_gain(df, attr, 'Buys') for attr in attributes}

# Find root node
root_node = max(gains, key=gains.get)

print("Information Gain per attribute:", gains)
print("Root Node:", root_node)

