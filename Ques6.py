# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier

# df = pd.read_csv("Lipstick.csv")

# X = pd.get_dummies(df[['Age','Income','Gender','Ms']])
# y = df['Buys']

# model = DecisionTreeClassifier()
# model.fit(X, y)

# test = pd.DataFrame([[">35","Medium","Female","Married"]],
#                     columns=['Age','Income','Gender','Ms'])
# test = pd.get_dummies(test).reindex(columns=X.columns, fill_value=0)

# print("Prediction:", model.predict(test)[0])


















