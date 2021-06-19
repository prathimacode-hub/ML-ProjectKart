#  FLIGHT DELAY PREDICTION 

**GOAL** 
- The main purpose of this project is to predict future delays in flights.

**DATASET**
- The data used in this project can be downloaded from [here](https://www.kaggle.com/usdot/flight-delays?select=flights.csv)

**WHAT I HAD DONE**
- Performed Exploratory Data Analysis.
- Created data visualisations to understand the data in a better way.
- Found strong relationships between independent features and dependent feature using correlation.
- Handled missing values using strong correlations,dropping unnecessary ones and filling important features with mean values.
- Used ensemble Modeling approach for building Classification Model to predict if flight will be delayed or not.
- Compared various models and used best performance model to make predictions.

**MODELS USED**
| Model | Accuracy Score |
| :--------: | :----------: |
| Logistic Regression | 0.99800 |
| Naive Bayes | 0.95586 |
| KNN | 0.96753 |
| Support Vector Machine | 0.99146 |


**LIBRARIES NEEDED**
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn


**CONCLUSION**
- Ensemble Modeling approach is best possible way to get higher performing model.
- Delays in departure of flights affects mostly to delay in flights.
- Here, Logistic Regression model can predict 99.8% accurate results of flight delays which is highest model performance in comparison with other Models.
