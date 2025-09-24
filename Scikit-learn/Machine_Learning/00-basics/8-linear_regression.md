# 📈 NOW: Linear Regression — The First Supervised Algorithm

---

## 🔢 What is Linear Regression?

- **Type**: Supervised Learning → Regression (predicts continuous number)
- **Goal**: Find the best-fit line (or hyperplane) that minimizes error between predicted and actual values.
- **Assumption**: Relationship between features and target is approximately linear.

---

## 🧠 Mathematical Form

For `n` features: ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

Or in vector form: ŷ = wᵀx + b

    - `ŷ` = predicted value
    - `w` = weights (learned from data)
    - `b` = bias / intercept
    - `x` = input features

> 📌 This is the same as the **hyperplane equation** — but here, we’re not separating classes, we’re predicting values.

---

## 📉 How It Learns: Cost Function & Optimization

- **Cost Function**: Mean Squared Error (MSE)
  MSE = (1/m) \* Σ(ŷᵢ - yᵢ)²

- **Optimization**: Gradient Descent (or Normal Equation) → finds `w` and `b` that minimize MSE.

---

## ✅ When to Use Linear Regression

- Predicting house prices, sales, temperature, salary
- Baseline model for any regression problem
- Interpretable — you can see how each feature affects output

---

## ⚠️ Limitations

- Assumes linear relationship
- Sensitive to outliers
- Can underfit if data is complex

> 💡 Fix with: Polynomial features, regularization (Ridge/Lasso), or upgrade to Random Forest / XGBoost.

---

📌 **Summary Flow**:
Equation of Line → Plane → Hyperplane
↓
Distance from Plane → Used in SVM
↓
Instance vs Model Based → Linear Regression is Model-Based
↓
ŷ = wᵀx + b → Learned via minimizing MSE
