**Problem Statement:**
Churn rate is a marketing metric that describes the number of customers who leave a business over a specific time period. . Every user is assigned a prediction value that estimates their state of churn at any given time. This value is based on:

- User demographic information
- Browsing behavior
- Historical purchase data among other information
It factors in our unique and proprietary predictions of how long a user will remain a customer. This score is updated every day for all users who have a minimum of one conversion. The values assigned are between 1 and 5.

**PROJECT TITLE:** 
Churn Risk Score Prediction 

**GOAL:** 
Goal is to predict the churn score for a website based on the features provided in the dataset.

**DATASET link:**  
train data - https://www.kaggle.com/imsparsh/churn-risk-rate-hackerearth-ml?select=train.csv
test data - https://www.kaggle.com/imsparsh/churn-risk-rate-hackerearth-ml?select=test.csv

**MODELS USED:**
I have used the Gradient Boosting Classifier algorithm for model building. 

**WHAT I HAD DONE:**
I have done the following operations on the given dataset.
- Data Exploration
- Data Cleaning
- Data Visualization
- Correlation
- Model Building
- Prediction.

**LIBRARIES NEEDED:**
- Pandas 
- Matplotlib
- Seaborn
- Numpy
- Sklearn

**Accuracy:**

Gradient Boosting Classifier
0.6363882496277243

Random Forrest
0.6011736834980371

**CONCLUSION:**
Hence the model built successfully and is ready to predict the churn score.