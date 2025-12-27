# import pandas as pd
# import matplotlib.pyplot as plt

# # 1. Load Data
# df = pd.read_csv('IRIS.csv')

# # 2. List features and types
# print(df.dtypes)

# # 3. Histogram
# df.hist(figsize=(10,10))
# plt.show()

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('IRIS.csv') 

print(df.dtypes)

df.hist(figsize=(10,10))
plt.show()