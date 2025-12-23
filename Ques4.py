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
