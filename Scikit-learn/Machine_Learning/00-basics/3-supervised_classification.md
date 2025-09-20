# **Classification**

## 🎓 Problem Statement

> **Predict if a student will Pass or Fail** based on their study and play habits.

---

## 📊 Sample Dataset

| No. of Study Hours | No. of Play Hours | Result (Pass/Fail) |
| ------------------ | ----------------- | ------------------ |
| 7                  | 3                 | Pass               |
| 2                  | 6                 | Fail               |

---

## 🧩 Key Terms

### ➤ Independent Features (Input Variables / X)

- Variables used to **predict** the outcome.
- Also called **features** or **predictors**.
- Examples:
  - `No. of Study Hours`
  - `No. of Play Hours`

### ➤ Dependent Feature (Output Variable / y)

- The **target** we want to predict.
- Also called **label** or **class**.
- In this case: `Pass` or `Fail`

> 🎯 Model learns:  
> `Result = f(Study Hours, Play Hours)`

---

## 🏁 Classification Types

### ✅ Binary Classification

- When the output has **two possible classes**.
- Example: `Pass` vs `Fail`, `Spam` vs `Not Spam`, `Yes` vs `No`

> ⚠️ This example is **Binary Classification** because there are only two outcomes.

### 🌐 Multiclass Classification

- When the output has **more than two classes**.
- Example: `A`, `B`, `C`, `D`, `F` (grades), or `Cat`, `Dog`, `Bird`

> 💡 Note: If the result could be `Pass`, `Fail`, or `May Be`, then it becomes **Multiclass**.

---

## 💡 How It Works

1. Train the model on historical data (with known results).
2. Model learns patterns between study/play time and performance.
3. Use trained model to predict outcome for **new students**.

### Example Prediction:

- Input: Study = 5 hrs, Play = 4 hrs
- Output: Predicted Result = **Pass**

---

## 🌍 Real-World Applications

- Student performance prediction
- Email spam detection
- Medical diagnosis (e.g., disease or no disease)
- Customer churn prediction (will leave or stay?)

---

## ✅ Summary

| Concept                       | Description                                     |
| ----------------------------- | ----------------------------------------------- |
| **Supervised Learning**       | Learns from labeled input-output pairs          |
| **Classification**            | Predicts discrete class labels                  |
| **Features (X)**              | Input variables (e.g., study hours, play hours) |
| **Target (y)**                | Output class (e.g., Pass/Fail)                  |
| **Binary Classification**     | Two possible outcomes (e.g., Pass/Fail)         |
| **Multiclass Classification** | More than two outcomes (e.g., A/B/C/D/F)        |

---
