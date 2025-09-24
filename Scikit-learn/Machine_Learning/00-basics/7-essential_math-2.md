## 4️⃣ Distance of a Point from a Plane (or Hyperplane)

Given a point **P = (x₀, y₀, z₀)** and plane: **ax + by + cz + d = 0**,  
the perpendicular distance is = |ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²)

→ In vector form (for hyperplane `wᵀx + b = 0` and point **x₀**): Distance = |wᵀx₀ + b| / ||w||

> 📌 Used in **SVM** to maximize margin → finds the hyperplane that keeps data points farthest from decision boundary.

---

## 5️⃣ Instance-Based vs Model-Based Learning

| Feature              | Instance-Based Learning            | Model-Based Learning                              |
| -------------------- | ---------------------------------- | ------------------------------------------------- |
| **What it stores**   | All training data (raw instances)  | Learns a generalized model (equation, tree, etc.) |
| **Prediction time**  | Slower (compares to all instances) | Faster (uses model to predict)                    |
| **Memory usage**     | High (stores all data)             | Low (stores only model parameters)                |
| **Examples**         | K-Nearest Neighbors (KNN)          | Linear Regression, Decision Trees, SVM            |
| **Flexibility**      | Adapts easily to new patterns      | Needs retraining if data changes                  |
| **Interpretability** | Low (no clear rules)               | Often high (e.g., coefficients, rules)            |

> 💡 **Linear Regression is Model-Based** — it learns `y = w₁x₁ + w₂x₂ + ... + b` and forgets the training data.

---

