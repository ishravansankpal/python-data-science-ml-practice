# Objective
# Explore and identify patterns in the Titanic dataset using data visualization.

# Description
# The Titanic dataset contains information about 891 passengers who boarded the Titanic.
# Using the Seaborn visualization library, this analysis focuses on discovering patterns
# and relationships between different passenger attributes and survival outcomes.

# Tasks Performed
# - Load the inbuilt Titanic dataset
# - Perform exploratory data analysis (EDA)
# - Visualize relationships between features using Seaborn
# - Identify patterns related to survival based on attributes such as:
#   - Gender
#   - Passenger class
#   - Age
#   - Fare

# Dataset
# - Titanic dataset (inbuilt Seaborn dataset)
# - Total records: 891 passengers

# Tools & Libraries
# - Python
# - Pandas
# - Seaborn
# - Matplotlib

# Outcome
# The visual analysis helps in understanding key factors that influenced passenger
# survival and highlights meaningful patterns within the dataset.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = pd.read_csv("Titanic.csv")

# Survival by Gender
sns.countplot(x="Survived", hue="Sex", data=titanic)
plt.show()

# Survival by Passenger Class
sns.countplot(x="Pclass", hue="Survived", data=titanic)
plt.show()
