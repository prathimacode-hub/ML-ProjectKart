Medical Insurance Cost Prediction using Machine Learning

This repository contains a Python script (issue.py) that demonstrates the prediction of medical insurance costs using various machine learning regression models. The script analyzes the "insurance.csv" dataset (available on Kaggle), which includes information about individuals and their associated medical insurance charges.

Goal:

The goal of this project is to build and evaluate machine learning models capable of accurately predicting the cost of medical insurance based on various factors like age, BMI, smoking habits, and region.

Dataset:

The dataset used for this project can be found on Kaggle:https://www.kaggle.com/datasets/mirichoi0218/insurance

Methodology:

The script implements the following steps:

Data Loading and Preprocessing:

Loads the "insurance.csv" dataset using Pandas.

Separates the features (independent variables) from the target variable (medical insurance charges).

Preprocesses the data by:

One-hot encoding categorical features (sex, smoker, region).

Scaling numerical features (age, bmi, children) using StandardScaler.

Model Building and Evaluation:

Defines multiple regression models:

Linear Regression

Decision Tree Regression

Random Forest Regression

Gradient Boosting Regression

Splits the data into training and testing sets.

Creates pipelines for each model, combining preprocessing and model training.

Trains each model on the training data and predicts on the testing data.

Evaluates the models using the following metrics:

Mean Squared Error (MSE)

Mean Absolute Error (MAE)

R-squared score

Ensemble Learning (Optional):

Implements a VotingRegressor ensemble model to combine predictions from the individual models.

Evaluates the ensemble model using the same metrics.

Results:

The script provides the following results:

Model	MSE,MAE,R-squared
Linear Regression	33596915.85	4181.19	0.7836
Decision Tree	47547224.40	3352.59	0.6937
Random Forest	21898087.07	2569.67	0.8589
Gradient Boosting	18790018.23	2410.57	0.8790
Ensemble Model	21434214.97	2703.98	0.8619

Conclusion:

The Gradient Boosting Regressor model achieved the highest R-squared score (0.8790), indicating the best predictive performance among the individual models. The Ensemble Model also showed strong performance, with an R-squared score of 0.8619. These results suggest that the models were able to effectively learn the relationships between the input features and insurance costs, providing reasonable predictions on unseen data.


Libraries:

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

To run the script:

Install the required libraries using pip install pandas numpy matplotlib seaborn scikit-learn

Download the "insurance.csv" dataset from Kaggle.

Run the script: python issue.py

This README.md file provides a comprehensive overview of the script's functionality, results, and potential improvements. Feel free to modify and experiment with the code to explore different aspects of medical insurance cost prediction.