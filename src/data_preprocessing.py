import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('/Users/jose/PycharmProjects/MotorCyclePricePredictor/data/BIKE DETAILS.csv')

# Preprocess the data
df['year'] = df['year'].apply(lambda x: 2024 - x)
df['seller_type'] = df['seller_type'].apply(lambda x: 1 if x == 'Individual' else 0)
df['owner'] = df['owner'].apply(lambda x: int(x.split()[0]) if x.split()[0].isdigit() else 0)
df['log_kms_driven'] = np.log1p(df['km_driven'])

# Fill missing values with the mean
df['ex_showroom_price'].fillna(df['ex_showroom_price'].mean(), inplace=True)

# Save the preprocessed data
df.to_csv('/Users/jose/PycharmProjects/MotorCyclePricePredictor/data/preprocessed_bike_data.csv', index=False)

print("Preprocessed data saved to /Users/jose/PycharmProjects/MotorCyclePricePredictor/data/preprocessed_bike_data.csv")
