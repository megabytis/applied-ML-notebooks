# **Regression**

## 🏠 Problem Statement:

> **Predict the price of a house** based on its features like size and number of rooms.

---

## 📊 Sample Dataset

| Size of House (sq ft) | # of Rooms | Price |
| --------------------- | ---------- | ----- |
| 5000                  | 5          | 450K  |
| 6000                  | 6          | 500K  |

---

## 🧩 Key Terms

### ➤ Independent Features (Input Variables / X)

- Variables used to **predict** the output.
- Also called **features** or **predictors**.
- Examples:
  - `Size of House`
  - `Number of Rooms`

### ➤ Dependent Feature (Output Variable / y)

- The **target** we want to predict.
- Also called **label** or **response variable**.
- In this case: `Price`

> 🎯 Model learns:  
> `Price = f(Size of House, # of Rooms)`

---

## 💡 How It Works

1. Train the model on historical data (with known prices).
2. Model finds patterns/relationships between features and price.
3. Use trained model to predict price for **new houses**.

### Example Prediction:

- Input: Size = 5500 sq ft, Rooms = 5.5
- Output: Predicted Price = ~475K

---

## 🌍 Real-World Applications

- Real estate price estimation
- Stock price forecasting
- Sales prediction
- Medical cost estimation

---

## ✅ Summary

| Concept                 | Description                                      |
| ----------------------- | ------------------------------------------------ |
| **Supervised Learning** | Learns from labeled input-output pairs           |
| **Regression**          | Predicts continuous numerical output             |
| **Features (X)**        | Input variables (e.g., size, rooms)              |
| **Target (y)**          | Output to predict (e.g., price)                  |
| **Goal**                | Build a model to accurately predict `y` from `X` |

---
