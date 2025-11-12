# Machine Learning Visualization Cheat Sheet

A plug-and-play guide to plotting in ML — no memorization, no confusion.

---

## 1️⃣ Scatter Plots (Basic Visualization)

**Use For:** Showing distribution or clusters.

```python
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap="viridis", s=50)
plt.title("Cluster Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
```

✅ Color each cluster or class with `c=y_pred`.

---

## 2️⃣ Confusion Matrix (Classification)

**Use For:** Evaluating classification models (actual vs predicted).

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()
```

✅ Dark diagonal = good model (more correct predictions).

---

## ⚡ 3️⃣ ROC Curve (Binary Classification)

**Use For:** Evaluating performance via probability thresholds.

```python
from sklearn.metrics import roc_curve, roc_auc_score

fpr, tpr, _ = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)

plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
plt.plot([0,1],[0,1],'--',color='gray')
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
```

✅ Curve closer to top-left = better model.

---

## 4️⃣ Precision–Recall Curve

**Use For:** When data is imbalanced.

```python
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_test, y_prob)
plt.plot(recall, precision, color="purple")
plt.title("Precision–Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.grid(True)
plt.show()
```

✅ Ideal curve stays high (both high precision & recall).

---

## 5️⃣ Elbow Method (K-Means)

**Use For:** Finding optimal K.

```python
inertia_values = []
K = range(1, 11)

for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    inertia_values.append(km.inertia_)

plt.plot(K, inertia_values, 'bx-')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (SSE)")
plt.title("Elbow Method for K-Means")
plt.grid(True)
plt.show()
```

✅ “Elbow bend” = best K.

---

## 6️⃣ Silhouette Visualization (Optional)

**Use For:** Checking clustering quality.

```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X, y_pred)
print(f"Silhouette Score: {score:.3f}")
```

✅ Higher = better separation between clusters.

---

## 7️⃣ PCA Visualization (for High Dimensions)

**Use For:** Reducing to 2D for visualization.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_pred, cmap='rainbow', s=50)
plt.title("PCA Projection of Data")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
```

✅ Each axis is a “compressed direction of max variance”.

---

## 8️⃣ Feature Distribution (Histograms)

**Use For:** Checking data spread / skew.

```python
df['feature_name'].hist(bins=30, color='skyblue', edgecolor='black')
plt.title("Feature Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

✅ Useful in preprocessing to detect scaling issues or outliers.

---

## 9️⃣ Correlation Heatmap

**Use For:** Understanding relationships between features.

```python
import seaborn as sns

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
```

✅ Bright = strong correlation.
Use before PCA or feature selection.

---

## 1️⃣0️⃣ Actual vs Predicted (Regression)

**Use For:** Seeing regression model accuracy visually.

```python
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()
```

✅ Points close to red line = good fit.

---

# Quick Styling Tips

- `cmap="viridis"` → smooth color map
- `alpha=0.6` → adds transparency
- `marker='x'` → highlights centroids
- `plt.grid(True, alpha=0.3)` → clean visuals
- `plt.tight_layout()` → fixes spacing

---

# Summary Table

| Plot Type           | Use Case                     | Must Know                                 |
| ------------------- | ---------------------------- | ----------------------------------------- |
| Scatter             | Show data points / clusters  | `plt.scatter()`                           |
| Confusion Matrix    | Classification accuracy      | `ConfusionMatrixDisplay()`                |
| ROC / PR Curve      | Probabilistic classification | `roc_curve()`, `precision_recall_curve()` |
| Elbow / Silhouette  | Clustering evaluation        | `KMeans().inertia_`                       |
| PCA Scatter         | Dimensionality reduction     | `PCA(n_components=2)`                     |
| Hist / Heatmap      | Feature analysis             | `df.hist()`, `sns.heatmap()`              |
| Actual vs Predicted | Regression                   | `plt.scatter(y_test, y_pred)`             |

---

> **Pro Tip:** We don’t “learn plotting.” We collect these 10 templates and reuse them forever.
> Just plug in our variables, tweak colors, and we’re done.

---

That’s our **visualization Swiss Army knife** 🔪