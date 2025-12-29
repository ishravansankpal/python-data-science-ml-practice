# Objective
# Analyze the COVID-19 vaccination data in India using the `covid_vaccine_statewise.csv` dataset.

# Tasks Performed
# - Described the overall structure and attributes of the dataset
# - Analyzed state-wise vaccination data
# - Computed the total number of people vaccinated with:
#   - First dose (state-wise)
#   - Second dose (state-wise)

# Dataset
# - `covid_vaccine_statewise.csv`
# - Contains state-wise COVID-19 vaccination details in India

# Key Concepts Used
# - Data exploration
# - Data aggregation
# - Group-by operations
# - Basic data analytics using Python

# Tools & Libraries
# - Python
# - Pandas

import pandas as pd

# Load dataset
df = pd.read_csv("Covid Vaccine Statewise.csv")

# a. Describe the dataset
print(df.describe(include='all'))

# b. Number of persons state-wise vaccinated with FIRST dose
first_dose = df.groupby("State")["First Dose Administered"].sum()
print(first_dose)

# c. Number of persons state-wise vaccinated with SECOND dose
second_dose = df.groupby("State")["Second Dose Administered"].sum()
print(second_dose)
