import finding_best_K_value as kval
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# Training Final Model
kval.kmeans_model = KMeans(n_clusters=5, random_state=42)
y_pred = kval.kmeans_model.fit_predict(kval.X_scaled)
# it will predict which person belongs to which Cluster
# Then we'll save the each person's belonged cluster number to each person & store in 👇
kval.df["Cluster"] = y_pred
# print(kval.df.head())


plt.figure(figsize=(7, 6))
plt.scatter(
    kval.X_scaled[:, 0], kval.X_scaled[:, 1], c=y_pred, cmap="rainbow", s=70, alpha=0.7
)
plt.scatter(
    kval.kmeans_model.cluster_centers_[:, 0],
    kval.kmeans_model.cluster_centers_[:, 1],
    s=200,
    c="black",
    marker="X",
    label="Centroids",
)
plt.title("Customer Segmentation using K-Means (K=5)")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.legend()
plt.grid(True, alpha=0.3)
# plt.show()


# Evaluating Cluster Quality
score = silhouette_score(kval.X_scaled, y_pred)
print(f"Silhouette Score: {score:.3f}")


# Labelling Segments
cluster_labels = {
    0: "Low Income, High Spending",
    1: "High Income, High Spending",
    2: "Low Income, Low Spending",
    3: "High Income, Low Spending",
    4: "Moderate Income, Moderate Spending",
}

kval.df["Segment"] = kval.df["Cluster"].map(cluster_labels)
print(kval.df[["Annual Income (k$)", "Spending Score (1-100)", "Segment"]].head(10))


kval.df.to_csv("customer_Segments.csv", index=False)
print("✅ Customer segmentation file saved as customer_segments.csv")
