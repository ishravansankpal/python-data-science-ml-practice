# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load Titanic dataset
# df = pd.read_csv("Titanic.csv")

# # Survival by Gender
# sns.countplot(x="Survived", hue="Sex", data=titanic)
# plt.show()

# # Survival by Passenger Class
# sns.countplot(x="Pclass", hue="Survived", data=titanic)
# plt.show()

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('Titanic.csv')

sns.countplot(x = 'Survived', hue='Sex', data = df)
plt.show()

sns.countplot(x = 'Pclass', hue = 'Survived', data = df)
plt.show()

sns.countplot(x = 'Age', hue = 'Survived', data = df)
plt.show()