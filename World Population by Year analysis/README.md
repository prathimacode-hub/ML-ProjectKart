# World Population By Year Analysis
## Aim
To visualise and analyse the trend in the change in total world population for past 70 years and model future world population predicter. 

## Dataset
https://www.kaggle.com/sansuthi/world-population-by-year

#### Description of features in the dataset:
1. Year: 1951 to 2020
2. Population: World Population
3. ChangePerc: Yearly Change in total population in Percentage
4. NetChange: Yearly Change in total population
5. Density: Density in P/Km²
6. Urban: Urban Population
7. UrbanPerc: Urban Population Percentage

## Data Visualization
* Visualisation of the dataset was done by using histogram distribution and used normalisation fit to all the features to check for skewness in the dataset.
* Line plot was plotted for each of the feature to visualise its trend in the changing years.
* All the features were correlated using heatmap and pair plot was plotted to find the relation between each pairs of features.
* Box plot was plotted to check for the outliers in the dataset, the features containing outliers was removed for the easeness of training dataset.

## Models
* Random Forest Regressor: A random forest is a supervised machine learning algorithm that can be used for both classification and regression tasks. The model works by sampling the training dataset, building multiple decision trees, and then having the output of the decision trees determine a prediction.

* Logistic Regression: Logistic regression is a fundamental classification technique. It is an algorithm that measures the probability of a binary response as the value of response variable based on the mathematical equation relating it with the predictor variables.

* XGBoost Regressor: XGBoost is a powerful approach for building supervised regression models. It is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.

* Kernel Ridge:

* Linear Regression:

## Libraries Needed
* sklearn==0.0
* seaborn==0.10.1
* numpy==1.18.5
* pandas==1.0.5
* matplotlib==3.2.2
* scipy==1.5.0
* xgboost==1.4.2

## Accuracy Score of each model
* Linear Regression:
* Logistic Regression:
* Kernel Ridge:
* XGBoost Regressor:
* Random Forest Regressor:

## Conclusion

## My Name
* Palak Singh
* https://www.linkedin.com/in/palak-singh-9066271a4/
