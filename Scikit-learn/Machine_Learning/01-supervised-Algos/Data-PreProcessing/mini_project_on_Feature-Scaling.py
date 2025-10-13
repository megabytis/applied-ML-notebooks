import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Loading the DataSet
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# Separating features and Target
# Now we have to scale the features only, not the Target, so hav to drop target and add all features elsewhere.
X = df.drop("target", axis=1)

# Applying StandardScaler
std_scaler = StandardScaler()
X_std = std_scaler.fit_transform(X)
df_std = pd.DataFrame(X_std, columns=X.columns)

# Applying MinMaxScaler
mm_scaler = MinMaxScaler()
X_mm = mm_scaler.fit_transform(X)
df_mm = pd.DataFrame(X_mm, columns=X.columns)

print("Original Data:")
print(X.describe())
print("\nAfter Standardization:")
print(df_std.describe())
print("\nAfter Normalization:")
print(df_mm.describe())

# Now Visualization : using BoxPlots
plt.figure(figsize=(15, 5))

# Original Data
plt.subplot(1, 3, 1)
plt.title("Before Scaling")
plt.boxplot(X.values)
plt.xticks(ticks=range(1, len(X.columns) + 1), labels=X.columns, rotation=45)

# After Standardization
plt.subplot(1, 3, 2)
plt.title("Afetr Standardization")
plt.boxplot(df_std)
plt.xticks(ticks=range(1, len(df_std.columns) + 1), labels=df_std.columns, rotation=45)

# After Normalization
plt.subplot(1, 3, 3)
plt.title("After Normalization")
plt.boxplot(df_mm)
plt.xticks(ticks=range(1, len(df_mm.columns) + 1), labels=df_mm.columns, rotation=45)

plt.show()
