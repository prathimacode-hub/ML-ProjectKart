
# Xbox Game Prediction Using Search Query Data

This project involves predicting user behavior based on search queries related to Xbox games. The dataset contains search queries, categories, and timestamps that were analyzed and processed to build predictive models. The goal was to predict a specific target outcome based on the given features.

## Table of Contents

1. [Data Collection](#data-collection)
2. [Data Preprocessing](#data-preprocessing)
3. [Model Building](#model-building)
4. [Results & Analysis](#results--analysis)
5. [Conclusion](#conclusion)

### 1. Data Collection

The dataset used in this project is `xbox.csv`, which contains the following key features:
- `sku`: Unique identifier for the product.
- `category`: The category of the game.
- `query`: The search query entered by the user.
- `click_time`: The timestamp when the user clicked on the game.
- `query_time`: The timestamp when the search query was entered.
- `query_length`: The length of the search query.

### 2. Data Preprocessing

**Conversion of Timestamps:**
- Both `click_time` and `query_time` were originally in string format. These were converted to `datetime` format to facilitate time-based feature extraction.

**Feature Engineering:**
- From the converted `click_time` and `query_time`, various features were extracted such as the hour, minute, and second. Additionally, the time difference between `click_time` and `query_time` was calculated to capture user interaction time.

**Label Encoding:**
- The `query` and `category` columns, being categorical, were label encoded to transform them into a numerical format suitable for modeling.

### 3. Model Building

| Model               | Accuracy    |
|---------------------|-------------|
| Logistic Regression | 79.25%      |
| Random Forest       | 95.80%      |

**Logistic Regression:**
- Logistic Regression was applied to the dataset to predict the target variable. The model achieved an accuracy of **79.25%**.

**Random Forest Classifier:**
- A Random Forest Classifier was also implemented, significantly improving the prediction accuracy to **95.80%**.

### 4. Results & Analysis

- **Logistic Regression:** The model provided a decent baseline with an accuracy of 79.25%. It performed well in scenarios with linear relationships between the features and the target.
  
- **Random Forest:** This model outperformed Logistic Regression with an accuracy of 95.80%, demonstrating its strength in handling complex data patterns and interactions between features.

### 5. Conclusion

This project demonstrated the power of feature engineering and the effectiveness of different machine learning models on the Xbox game search query dataset. The Random Forest model proved to be the most successful in predicting user behavior, making it a valuable tool for understanding and anticipating user preferences in the gaming industry.
