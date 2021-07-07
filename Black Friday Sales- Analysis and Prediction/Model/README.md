**Black Friday Sales- Analysis and Prediction**

Black Friday is a colloquial term for the Friday following Thanksgiving Day in the United States. Many stores offer highly promoted sales on Black Friday and open very early, or some time on Thanksgiving Day. Black Friday has routinely been the busiest shopping day of the year in the United States since at least 2005.

**GOAL**

The goal of this project is to analyse and predict purchases in the black friday sales from features as age group, gender, occupation, product category etc.

**DATASET**

Dataset can be downloaded from [here](https://www.kaggle.com/sdolezel/black-friday?select=train.csv).

**WHAT I HAD DONE**
- Step 1: Data Exploration
- Step 2: Data Cleaning
- Step 3: Data Visualization
- Step 4: Data Preparation & Training
- Step 5: Model Creation
- Step 6: Performance Evaluation


**MODELS USED**
-  Linear Regression
-  Lasso Regression
-  Ridge Regression
-  Decision Tree Regressor
-  Random Forest Regressor



**LIBRARIES NEEDED**
- pandas
- numpy
- matplotlib
- seaborn
- sklearn (For data traning, importing models and performance check)

**INSIGHTS DRAWN**
* **Males** showed more interest in the black friday sales than as compared to that of females.
*  **Age group 26-35** were more active than other age groups.
* People from **20 different occupations** showed their interest in the black friday sales.
* People from **city B** were more as compared to city A & C.
* Maximum people are staying in their respective city from **1 year**.
* **59.09%** people were unmarried  and 40.91 % were married among total participation.
* There are 18 subcategories of products in category 1.
* There are 17 subcategories of products in category 2.
* There are 15 subcategories of products in category 3.


**Accuracy of different models used**
- By using Linear Regression model 
 ```python
    Accuracy achieved :  10.92
 ``` 
 - By using Lasso Regression model 
 ```python
    Accuracy achieved :  10.92
 ``` 
  - By using Ridge Regression model 
 ```python
    Accuracy achieved :  10.92
 ```
 - By using Decision Tree Regressor model 
 ```python
    Accuracy achieved :  74.62
 ``` 
  - By using Random Forest Regressor model 
 ```python
    Accuracy achieved :  73.80
 ```



**CONCLUSION**

Performance of Decision tree regressor is better in terms of accuracy as compared to linear regression, lasso regression, ridge regression and random forest regressor.


**Author** 

[Ayushi Shrivastava](https://github.com/ayushi424)
