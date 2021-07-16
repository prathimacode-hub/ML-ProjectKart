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

## Data Visualization and Approach
* Visualised the dataset by using **histogram distribution** and used **normalisation fit** to all the features to check for **skewness** present in each feature in the dataset.
* **Line plot** was plotted for each of the feature to visualise its trend in the changing years.
* All the features were **correlated** using **heatmap** and **pair plot** was plotted to find the relation between each pairs of features. 
* **Box plot** was plotted to check for the **outliers** in the dataset, the features containing outliers was removed for the easeness of training dataset.
* Features were scaled before applying ML model to it. 

## Models
* **Random Forest Regressor**: A random forest is a supervised machine learning algorithm that can be used for both classification and regression tasks. Here, random forest is used for regression task. 
Random Forest Regression is a supervised learning algorithm that uses ensemble learning method for regression. The model works by sampling the training dataset, building multiple decision trees, and outputting the mean/mode of prediction of the individual trees.

* **Logistic Regression**: Logistic regression is a fundamental classification technique, but can also be used for regression tasks. It is an algorithm that measures the probability of a binary response as the value of response variable based on the mathematical equation relating it with the predictor variables. It uses sigmoid function for the feature modelling.

* **XGBoost Regressor**: XGBoost is a powerful approach for building supervised regression models. It is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.

* **Kernel Ridge**: Kernel ridge regression (KRR) combines ridge regression (linear least squares with l2-norm regularization) with the kernel trick. It thus learns a linear function in the space induced by the respective kernel and the data. For non-linear kernels, this corresponds to a non-linear function in the original space.

* **Linear Regression**: Linear regression is a linear model that assumes a linear relationship between the input variables matrix (x) and the single output variable (y).

## Libraries Needed
* sklearn==0.0
* seaborn==0.10.1
* numpy==1.18.5
* pandas==1.0.5
* matplotlib==3.2.2
* scipy==1.5.0
* xgboost==1.4.2

## Accuracy Score of each model
#### R2 score:
* Linear Regression:0.9990599862236123
* Logistic Regression:0.9717703193951238
* Kernel Ridge:0.9944767667649214
* XGBoost Regressor:0.9968942494250208
* Random Forest Regressor:0.9967004821427558
#### Mean absolute error:
* Linear Regression:33803393.75958949
* Logistic Regression:202904558.3809524
* Kernel Ridge:92449024.91959827
* XGBoost Regressor:73621005.14285715
* Random Forest Regressor:54836079.01761898
#### Mean squared error:
* Linear Regression:1896014273658965.2
* Logistic Regression:5.69394605825428e+16
* Kernel Ridge:1.1140399548928138e+16
* XGBoost Regressor:6264320341360499.0
* Random Forest Regressor:6655150286804994.0

For concluding a perfect model, I used all the three errors and score to calculate a new score by introducing a new measure to the model,
* **Final score**=(R2 score * 100)/(Mean absolute error + Mean squared error)
#### Final score:
* Linear Regression:5.2692639622575544e-14
* Logistic Regression:1.7066728521663304e-15
* Kernel Ridge:8.926760248988567e-15
* XGBoost Regressor:1.591384513220121e-14
* Random Forest Regressor:1.497637815792727e-14

## Conclusion
Since, final score of Linear regression is highest among all the rest of the models, so, Linear regression model works best for the current world population prediction model.

## My Name
* Palak Singh
* https://www.linkedin.com/in/palak-singh-9066271a4/
