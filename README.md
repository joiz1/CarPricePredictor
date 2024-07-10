# Motorcycle Price Prediction

👨‍💻 Getting Started 😃😃

## Introduction 😃😃

### Problem Statement
A global motorcycle manufacturing company aims to expand its market presence in Europe by setting up new manufacturing units and producing motorcycles locally. They have contracted a market research firm to understand the factors influencing motorcycle pricing. Specifically, they want to analyze the variables affecting the pricing of motorcycles in the European market, as these factors may differ significantly from other regions. The company seeks to determine:

- Which variables are significant in predicting the price of a motorcycle 😃😃😃😃
- How well those variables describe the price of a motorcycle 😃😃😃😃

Based on extensive market research, the consulting firm has gathered a large dataset of various types of motorcycles across the European market. So, put on your helmet and get ready for an exciting journey. We're about to explore the world of motorcycles, solve pricing puzzles, and have a good laugh along the way! 🏍️😃😃😄😃😄

## Learn About Data

- **BikeID**: Identification Number for Each Motorcycle
- **SafetyRating**: Motorcycle's Safety Rating
- **BikeName**: Name of the Motorcycle Model
- **FuelType**: Type of Fuel Used (Gasoline, Electric, etc.)
- **NumGears**: Number of Gears on the Motorcycle
- **BodyStyle**: Style of the Motorcycle's Body (Sport, Cruiser, Touring, etc.)
- **DriveType**: Type of Drive (Chain, Belt, Shaft)
- **EngineLocation**: Location of the Motorcycle's Engine (Front, Rear)
- **Wheelbase**: Length of the Motorcycle's Wheelbase
- **BikeLength**: Overall Length of the Motorcycle
- **BikeWidth**: Width of the Motorcycle
- **BikeHeight**: Height of the Motorcycle
- **CurbWeight**: Weight of the Motorcycle without Passengers or Cargo
- **EngineType**: Type of Engine (Gas, Electric, etc.)
- **NumCylinders**: Number of Cylinders in the Engine
- **EngineSize**: Size of the Motorcycle's Engine
- **FuelSystem**: Type of Fuel Delivery System
- **BoreRatio**: Bore-to-Stroke Ratio of the Engine
- **Stroke**: Stroke Length of the Engine
- **CompressionRatio**: Compression Ratio of the Engine
- **Horsepower**: Motorcycle's Engine Horsepower
- **PeakRPM**: Engine's Peak RPM (Revolutions Per Minute)
- **CityMPG**: Miles Per Gallon (MPG) in City Riding
- **HighwayMPG**: MPG on the Highway
- **BikePrice**: Price of the Motorcycle

## Life Cycle of Machine Learning Project

1. Understanding the Problem Statement
2. Data Checks to Perform
3. Exploratory Data Analysis
4. Data Pre-Processing
5. Model Training
6. Choose Best Model

### 1. Problem Statement

Predicting the price of motorcycles based on a wide range of attributes and features. Using a dataset containing motorcycle details such as safety ratings, dimensions, engine specifications, and more, we aim to develop a machine learning model that accurately estimates the price of different motorcycle models.

### 2. Data Checks to Perform

- Check Missing values
- Check Duplicates
- Check data type
- Check the number of unique values of each column
- Check statistics of the dataset
- Check various categories present in the different categorical columns

### 3. Exploratory Data Analysis

- Distribution of Numerical Features
- Price Analysis
- Categorical Feature vs. Price
- Correlation Analysis

### 4. Data Pre-Processing

- Extract brand and model from BikeName
- Encoding categorical variables
- Feature engineering
- Feature scaling

### 5. Train the Model

- Splitting the dataset
- Model training
- Predictions
- Evaluate the model

### 6. Model Evaluation

- Calculate Mean Squared Error
- Calculate R-squared

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MotorcyclePricePrediction.git
   cd MotorcyclePricePrediction
