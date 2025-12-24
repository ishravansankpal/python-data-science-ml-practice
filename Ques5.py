#  Objective
# Predict customer response to a lipstick offer using a Decision Tree model
# implemented with machine learning libraries.

#  Tasks Performed
# - Trained a Decision Tree classifier using the given dataset
# - Used library-based implementation (scikit-learn)
# - Predicted the outcome for the following test data:

#   Age < 21  
#   Income = Low  
#   Gender = Female  
#   Marital Status = Married  

# Implementation
# - Decision Tree implemented using Python ML libraries
# - Model trained on previous dataset and used for prediction



import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("Lipstick.csv")

X = pd.get_dummies(df[['Age','Income','Gender','Ms']])
y = df['Buys']

model = DecisionTreeClassifier()
model.fit(X, y)

test = pd.DataFrame([["<21","Low","Female","Married"]], columns=['Age','Income','Gender','Ms'])
test = pd.get_dummies(test).reindex(columns=X.columns, fill_value=0)

print("Prediction: ", model.predict(test)[0])



