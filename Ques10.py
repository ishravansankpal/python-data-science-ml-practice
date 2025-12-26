# K-Means Clustering (Manual Implementation)

# Objective
# To perform K-Means clustering on a given set of 2D data points using predefined initial centroids and analyze cluster assignments and centroid updates.

# Dataset
# A collection of 8 data points:
# - P1 = [2, 10]
# - P2 = [2, 5]
# - P3 = [8, 4]
# - P4 = [5, 8]
# - P5 = [7, 5]
# - P6 = [6, 4]
# - P7 = [1, 2]
# - P8 = [4, 9]

# Initial Cluster Centroids
# - Cluster C1 (m1) = P1 = [2, 10]
# - Cluster C2 (m2) = P4 = [5, 8]
# - Cluster C3 (m3) = P7 = [1, 2]

# Methodology
# - Euclidean distance is used as the distance measure.
# - Each point is assigned to the nearest centroid.
# - New centroids are computed by calculating the mean of points in each cluster.
# - Clustering is performed step-by-step for academic understanding.

# Tasks Performed
# - Determine the cluster to which point P6 belongs
# - Calculate the population of the cluster around centroid m3
# - Compute the updated values of centroids m1,m2, and m3

import numpy as np

# Given points
points = np.array([
    [2,10],  # P1
    [2,5],   # P2
    [8,4],   # P3
    [5,8],   # P4
    [7,5],   # P5
    [6,4],   # P6
    [1,2],   # P7
    [4,9]    # P8
])

# Initial centroids
m1 = points[0]   # P1
m2 = points[3]   # P4
m3 = points[6]   # P7

# Distance function
def dist(a, b):
    return np.sqrt(np.sum((a - b)**2))

# Step 1: Assign each point to the nearest centroid
C1 = []
C2 = []
C3 = []

for p in points:
    d1 = dist(p, m1)
    d2 = dist(p, m2)
    d3 = dist(p, m3)

    if d1 < d2 and d1 < d3:
        C1.append(p)
    elif d2 < d1 and d2 < d3:
        C2.append(p)
    else:
        C3.append(p)

C1 = np.array(C1)
C2 = np.array(C2)
C3 = np.array(C3)

# Step 2: Update centroids
new_m1 = C1.mean(axis=0)
new_m2 = C2.mean(axis=0)
new_m3 = C3.mean(axis=0)

# ----- PRINT ANSWERS -----

print("Cluster 1 (C1):\n", C1)
print("Cluster 2 (C2):\n", C2)
print("Cluster 3 (C3):\n", C3)

# 1) Which cluster does P6 belong to?
P6 = points[5]
if any((P6 == x).all() for x in C1):
    print("\n1) P6 belongs to: Cluster 1")
elif any((P6 == x).all() for x in C2):
    print("\n1) P6 belongs to: Cluster 2")
else:
    print("\n1) P6 belongs to: Cluster 3")

# 2) Population around m3 (cluster 3)
print("2) Population of Cluster 3:", len(C3))

# 3) Updated centroids
print("\n3) Updated m1:", new_m1)
print("   Updated m2:", new_m2)
print("   Updated m3:", new_m3)

