import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

dataset = load_iris()

X = dataset.data
y_true = dataset.target

df = pd.DataFrame(X, columns=dataset.feature_names)
# print(df.head())

"""
It contains 4 numeric columns :
sepal length
sepal width
petal length
petal width
"""

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Now finding optimal Number of Clusters (Elbow Method)
inertia_values = []
k_vals = range(1, 11)

for k in k_vals:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_scaled)
    inertia_values.append(model.inertia_)

plt.figure(figsize=(6, 5))
plt.plot(k_vals, inertia_values, "bx-")
plt.xlabel("Number of Clusters (k_vals)")
plt.ylabel("Inertia (SSE)")
plt.title("Elbow Method for Optimal k_val")
plt.grid(True, alpha=0.3)
plt.show()
