import finding_best_k_val as kval
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

model = kval.KMeans(n_clusters=3, random_state=42)
y_pred = model.fit_predict(kval.X_scaled)
print(f"Cluster Centers:\n{model.cluster_centers_}")

plt.figure(figsize=(6, 5))
plt.scatter(
    kval.X_scaled[:, 0], kval.X_scaled[:, 1], c=y_pred, cmap="viridis", s=60, alpha=0.7
)
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color="red",
    s=200,
    marker="x",
    label="Centroids",
)
plt.title("K-Means Clustering on Iris Dataset (2D View)")
plt.xlabel("Feature 1 (Scaled)")
plt.ylabel("Feature 2 (Scaled)")
plt.legend()
plt.show()

# Evaluating Cluster Quality
score = kval.silhouette_score(kval.X_scaled, y_pred)
print(f"Silhouette Score: {score:.3f}")

# Now Comparision with Actual Score
comparision = kval.pd.DataFrame({"Actual": kval.y_true, "Predicted": y_pred})
print(comparision.head(10))


# Visualization

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    kval.X_scaled[:, 0],
    kval.X_scaled[:, 1],
    kval.X_scaled[:, 2],
    c=y_pred,
    cmap="viridis",
    s=60,
)
ax.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    model.cluster_centers_[:, 2],
    color="red",
    s=200,
    marker="x",
    label="Centroids",
)
ax.set_title("K-Means Clustering on Iris (3D View)")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")
ax.legend()
plt.show()
