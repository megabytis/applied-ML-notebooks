import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    f1_score,
    accuracy_score,
    recall_score,
    precision_score,
    precision_recall_curve,
    average_precision_score,
    auc,
)
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = pd.read_csv(file_path)
print(df.columns)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

X = df.drop("Churn", axis=1).drop("customerID", axis=1)
y = df["Churn"].map({"Yes": 1, "No": 0})  # converting yes/no to 1/0 also here


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Separating numerical and categorical columns
numerical_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

# Removing Target column from eatures if it is present in the list
if "Churn" in numerical_features:
    numerical_features.remove("Churn")
if "Churn" in categorical_features:
    categorical_features.remove("Churn")

if "customerID" in numerical_features:
    numerical_features.remove("customerID")
if "customerID" in categorical_features:
    categorical_features.remove("customerID")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_features),
        (
            "cat",
            OneHotEncoder(drop="first", handle_unknown="ignore"),
            categorical_features,
        ),
    ]
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(class_weight="balanced")),
    ]
)


pipeline.fit(X_train, y_train)
y_prob = pipeline.predict_proba(X_test)[:, 1]
y_pred = (y_prob >= 0.4).astype(int)

print(f"\nReal:\n{y_test} \nPredict:\n{y_pred}")


cm = confusion_matrix(y_test, y_pred)
f1s = f1_score(y_test, y_pred)
rs = recall_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)


print(
    f"\nConfusion-Matrix:\n{cm} \nF1-Score:{f1s} \nRecall-Score:{rs} \nAccuracy-Score:{accuracy} \nPrecission-Score:{precision}\n"
)


plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No", "Yes"],
    yticklabels=["No", "Yes"],
)
plt.title("Confusion Matrix - Customer-Churn")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()

# pr_auc = auc(recalls, precisions)

# plt.figure(figsize=(6, 5))
# plt.plot(recalls, precisions, color="blue", lw=2, label=f"PR AUC = {pr_auc:.3f}")
# plt.title("Precision-Recall Curve - Customer Churn")
# plt.xlabel("Recall")
# plt.ylabel("Precision")
# plt.legend(loc="lower left")
# plt.grid(alpha=0.3)
# plt.show()


pickle.dump(pipeline, open("churn_pipeline.pkl", "wb"))
print("Model saved as 'churn_pipeline.pkl'")
