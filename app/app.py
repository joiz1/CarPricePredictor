from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model using the absolute path
model = joblib.load('/Users/jose/PycharmProjects/MotorCyclePricePredictor/models/linear_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = pd.DataFrame([request.form])

    input_data['year'] = int(input_data['year'].iloc[0])
    input_data['km_driven'] = int(input_data['km_driven'].iloc[0])
    input_data['ex_showroom_price'] = float(input_data['ex_showroom_price'].iloc[0])
    input_data['seller_type'] = 1 if input_data['seller_type'].iloc[0] == 'Individual' else 0
    input_data['owner'] = int(input_data['owner'].iloc[0].split()[0]) if input_data['owner'].iloc[0].split()[0].isdigit() else 0
    input_data['log_kms_driven'] = np.log1p(input_data['km_driven'])

    features = ['year', 'km_driven', 'ex_showroom_price', 'log_kms_driven']
    prediction = model.predict(input_data[features])

    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
