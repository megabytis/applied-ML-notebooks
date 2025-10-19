import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "house_price_prediction_data.csv")

df = pd.read_csv(file_path)

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline(steps=[("scaler", StandardScaler()), ("model", LinearRegression())])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2s = r2_score(y_test, y_pred)

print(f"MSE:{mse} \nRMSE:{rmse} \nR2_Score:{r2s}")

# Percentage error
mean_price = y_test.mean()
percentage_error = (rmse / mean_price) * 100
print(f"RMSE as % of mean price: {percentage_error:.2f}%")

# Plotting
plt.scatter(y_test, y_pred, alpha=0.4)
plt.plot(
    [y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linewidth=2
)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("House-Price: Actual vs Predicted")
plt.show()
