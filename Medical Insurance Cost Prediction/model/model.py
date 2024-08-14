import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv("dataset/insurance.csv")

# Separate features and target
X = data.drop('charges', axis=1)
y = data['charges']

# Preprocessing: Encode categorical features and scale numerical features
numeric_features = ['age', 'bmi', 'children']
categorical_features = ['sex', 'smoker', 'region']

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Define multiple models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor()
}

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Results dictionary to store metrics for each model
results = {}

# Train and evaluate each model
for name, model in models.items():
    # Create pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])
    # Train the model
    pipeline.fit(X_train, y_train)
    # Predict on the test set
    y_pred = pipeline.predict(X_test)
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    # Store the results
    results[name] = {"mse": mse, "mae": mae, "r2_score": r2}

# Print the results
for name, metrics in results.items():
    print(f"{name}:\n\tMean Squared Error: {metrics['mse']}\n\tMean Absolute Error: {metrics['mae']}\n\tR-squared: {metrics['r2_score']}\n")

# Ensemble Learning (Optional): Combining predictions
from sklearn.ensemble import VotingRegressor

ensemble = VotingRegressor(estimators=[
    ('lr', LinearRegression()),
    ('dt', DecisionTreeRegressor()),
    ('rf', RandomForestRegressor()),
    ('gb', GradientBoostingRegressor())
])

ensemble_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('ensemble', ensemble)
])

ensemble_pipeline.fit(X_train, y_train)
ensemble_pred = ensemble_pipeline.predict(X_test)

# Evaluate the ensemble model
ensemble_mae = mean_absolute_error(y_test, ensemble_pred)
ensemble_mse = mean_squared_error(y_test, ensemble_pred)
ensemble_r2 = r2_score(y_test, ensemble_pred)

print(f"Ensemble Model:\n\tMean Absolute Error: {ensemble_mae}\n\tMean Squared Error: {ensemble_mse}\n\tR-squared: {ensemble_r2}\n")
