# 21. Write a program to cluster a set of points using K-means for IRIS dataset. Consider, K=4, clusters. Consider Euclidean distance as the 
# distance measure. Randomly initialize a cluster mean as one of the data
# points. Iterate at least for 10 iterations. After iterations are over, print the
# final cluster means for each of the clusters.

             
import pandas as pd
from sklearn.cluster import KMeans

# Load IRIS dataset
df = pd.read_csv("IRIS.csv")

# Use only numeric columns (sepal/petal measurements)
X = df.select_dtypes(include='number')

# Run K-Means: 4 clusters, random init, 10 iterations
kmeans = KMeans(n_clusters=4,
                init='random',     # random initial centroids
                max_iter=10,       # at least 10 iterations
                n_init=1,          # run only once (as required)
                random_state=42)

# Fit model
kmeans.fit(X)

# Print final cluster means (centroids)
print("Final Cluster Means (Centroids):")
print(kmeans.cluster_centers_)

