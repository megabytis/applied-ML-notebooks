"""
######################################
Customer Segmentation using K-Means
######################################
"""

# Goal: Automatically group customers based on their Annual Income and Spending Score, so businesses can target them better.

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "../../../datasets/Mall_Customers.csv")

df = pd.read_csv(file_path)
# print(df.head)

# Selecting Features for Clustering
# We ahve to focus on Annual Income and Spending Score, since they are the most relevant and visualizable features
X = df[["Annual Income (k$)", "Spending Score (1-100)"]].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Now finding Optimal K (Elbow Method)
inertia = []
k_vals = range(1, 11)

for k in k_vals:
    kmeans_model = KMeans(n_clusters=k, random_state=42)
    kmeans_model.fit(X_scaled)
    inertia.append(kmeans_model.inertia_)

plt.figure(figsize=(6, 5))
plt.plot(k_vals, inertia, "bx-")
plt.xlabel("Number of clusters (k_vals)")
plt.ylabel("Inertia (SSE)")
plt.title("Elbow Method for optimal k_val")
plt.grid(True, alpha=0.3)
# plt.show()


"""
From the plotted Elbow graph we could able to see that at k=5 the elbow slightly bend,
that's the sweet spot
"""
