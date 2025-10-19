import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, recall_score
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "loan_approval_data.csv")

df = pd.read_csv(file_path)
X = df.drop("Approved", axis=1)
y = df["Approved"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


pipeline = Pipeline(
    steps=[("scaler", StandardScaler()), ("model", LogisticRegression())]
)

pipeline.fit(X_train, y_train)
y_prob = pipeline.predict_proba(X_test)[:, 1]
y_pred = (y_prob >= 0.5).astype(int)


print(f"Real:\n{y_test}\nPrediction:\n{y_pred}\n")


cm = confusion_matrix(y_test, y_pred)
acc_score = accuracy_score(y_test, y_pred)
rs = recall_score(y_test, y_pred)
fs = f1_score(y_test, y_pred)

print(
    f"confusion-Matrix: \n{cm} \n\nAccuracy-Score: {acc_score} \nRecall-Score: {rs} \nF1-Score: {fs} \n"
)


# plt.figure(figsize=(12, 4))

# plt.subplot(1, 2, 1)
# plt.scatter(y_test, y_pred, alpha=0.6)
# plt.xlabel("Actual Approval")
# plt.ylabel("Predicted Approval")
# plt.title("Loan Approval: Actual vs Predicted")
# plt.xticks([0, 1])
# plt.yticks([0, 1])
# plt.grid(True, alpha=0.3)

# plt.subplot(1, 2, 2)
# plt.scatter(range(len(y_test)), y_prob, c=y_test, cmap="viridis", alpha=0.7)
# plt.axhline(y=0.5, color="red", linestyle="--", label="Decision Threshold (0.5)")
# plt.xlabel("Sample Index")
# plt.ylabel("Predicted Probability of Approval")
# plt.title("Predicted Probabilities by Sample")
# plt.legend()
# plt.colorbar(label="Actual Approval (0=No, 1=Yes)")

# plt.tight_layout()
# plt.show()


plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Denied", "Approved"],
    yticklabels=["Denied", "Approved"],
)
plt.title("Confusion Matrix - Loan Approval")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()
