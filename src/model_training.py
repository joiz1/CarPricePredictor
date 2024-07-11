import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the preprocessed data
df = pd.read_csv('/Users/jose/PycharmProjects/MotorCyclePricePredictor/data/preprocessed_bike_data.csv')

# Features and target variable
features = ['year', 'km_driven', 'ex_showroom_price', 'log_kms_driven']
target = 'selling_price'

X = df[features]
y = df[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate mean squared error
mse = np.mean((y_test - y_pred) ** 2)
print(f"Mean Squared Error: {mse}")

# Save the model
joblib.dump(model, '/Users/jose/PycharmProjects/MotorCyclePricePredictor/models/linear_regression_model.pkl')

print("Model saved to /Users/jose/PycharmProjects/MotorCyclePricePredictor/models/linear_regression_model.pkl")
