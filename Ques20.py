# import pandas as pd
# from sklearn.cluster import KMeans

# # Load IRIS dataset
# df = pd.read_csv("IRIS.csv")

# # Use only numeric columns (sepal/petal measurements)
# X = df.select_dtypes(include='number')

# # Run K-Means: 4 clusters, random init, 10 iterations
# kmeans = KMeans(n_clusters=3,
#                 init='random',     # random initial centroids
#                 max_iter=10,       # at least 10 iterations
#                 n_init=1,          # run only once (as required)
#                 random_state=42)

# # Fit model
# kmeans.fit(X)

# # Print final cluster means (centroids)
# print("Final Cluster Means (Centroids):")
# print(kmeans.cluster_centers_)

# import pandas as pd 
# from sklearn.cluster import KMeans

# df = pd.read_csv('IRIS.csv')

# X = df.select_dtypes(include = 'number')
# KMeans = KMeans(n_clusters=3, init='random', max_iter=10, n_init=1, random_state=42)

# KMeans.fit(X)

# print(KMeans.cluster_centers_)

import pandas as pd 
from sklearn.cluster import KMeans

df = pd.read_csv('IRIS.csv')

X = df.select_dtypes(include='numbers')
KMeans = KMeans(n_clusters=3, init='random', max_iter=10, n_init=1, random_state=1)

KMeans.fit(X)

print(KMeans.cluster_centers_)