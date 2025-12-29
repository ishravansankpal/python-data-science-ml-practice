# import pandas as pd

# # Load dataset
# df = pd.read_csv("Covid Vaccine Statewise.csv")

# # a. Describe the dataset
# print(df.describe(include='all'))

# # b. Number of persons state-wise vaccinated with FIRST dose
# first_dose = df.groupby("State")["First Dose Administered"].sum()
# print(first_dose)

# # c. Number of persons state-wise vaccinated with SECOND dose
# second_dose = df.groupby("State")["Second Dose Administered"].sum()
# print(second_dose)


import pandas as pd 

df = pd.read_csv('Covid Vaccine Statewise.csv')

print(df.describe())

first_dose = df.groupby('State')['First Dose Administered'].sum()
print(first_dose)

second_dose = df.groupby('State')['Second Dose Administered'].sum()
print(second_dose)