#  Objective
# Use a Decision Tree model to predict customer response to a lipstick offer using library-based implementation.

# Tasks Performed
# - Train a Decision Tree model using the cosmetics shop dataset
# - Predict customer response for given test cases
# - Analyze decisions based on trained model

# Test Cases 
# 1. Age > 35, Income = Medium, Gender = Female, Marital Status = Married

# Tools Used
# - Python
# - Scikit-learn

# Dataset
# - Cosmetics shop customer dataset

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("Lipstick.csv")

X = pd.get_dummies(df[['Age','Income','Gender','Ms']])
y = df['Buys']

model = DecisionTreeClassifier()
model.fit(X, y)

test = pd.DataFrame([[">35","Medium","Female","Married"]],
                    columns=['Age','Income','Gender','Ms'])
test = pd.get_dummies(test).reindex(columns=X.columns, fill_value=0)

print("Prediction:", model.predict(test)[0])



















