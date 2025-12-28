import pandas as pd
import matplotlib.pyplot as plt


# 1. Load Data
df = pd.read_csv('IRIS.csv')

# 2. Create box plot for each feature
plt.figure(figsize=(10, 8))
df.boxplot()
plt.title("Box Plots of Iris Dataset Features")
plt.show()


