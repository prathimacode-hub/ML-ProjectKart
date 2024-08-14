Amazon Sales Data Analysis
Overview
This project involves analyzing and modeling sales data from Amazon. The dataset used includes various features related to sales transactions, including order details, shipping information, and sales quantities. The goal is to clean, preprocess, and analyze the data to extract insights and build predictive models.

Project Structure
Data Cleaning and Preprocessing:

Removal of irrelevant columns (Order ID, ASIN, etc.).
Handling missing data by dropping rows with null values in critical columns (Date, Qty, Amount).
Conversion of Date to datetime format and extraction of time-based features like Year, Month, Day, and Weekday.
Encoding of categorical variables such as Category, Size, and promotion-ids using one-hot encoding.
Exploratory Data Analysis (EDA):

Visualization of sales trends over time.
Decomposition of the time series to analyze seasonal components.
Modeling:

Use of XGBoost for predictive modeling.
Evaluation of model performance using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared.
Requirements
To run the notebook, you will need the following Python libraries:

numpy
pandas
matplotlib
statsmodels
xgboost
scikit-learn
You can install these dependencies using pip:

bash
Copy code
pip install numpy pandas matplotlib statsmodels xgboost scikit-learn
How to Run
Clone the repository or download the notebook file.
Install the required dependencies.
Open the notebook using Jupyter and run the cells sequentially.
Data
The dataset used in this analysis is not included in this repository. Please ensure you have access to the Amazon_Sale_Report.csv file and place it in the appropriate directory.

Results
The analysis provides insights into sales patterns over time and allows for predictive modeling to forecast future sales trends.  
 for xgboost:
    Mean Squared Error: 0.0023453120571902807
    Mean Absolute Error: 0.004754900366465545
    R-squared: 0.941647067855254
    Accuracy (rounded predictions): 0.9978544314243274
 for hybrid-approach:
    Mean Squared Error: 0.0006714059939832862
    R^2 Score: 0.0
