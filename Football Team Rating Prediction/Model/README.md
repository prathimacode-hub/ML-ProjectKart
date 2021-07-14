**GOAL**

The goal is to predict rating of Football Team.

Dataset can be downloaded from [here](https://www.kaggle.com/varpit94/football-teams-rankings-stats)

**WHAT I HAD DONE**
- Discussed some major columns on which rating of Team.
- Handling outliers of diagnosis columns. As, it is very important because at last we're predicting ratings.
- Then I used different Regression models present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**
-  Linear Regression
-  KNN Regressor
-  Random Forest Regressor

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn

**CONCLUSION**

By using Linear Regression I got 
 ```
    Accuracy of training data: 85.93715635518097
    Accuracy of testing data: 85.50910152456676
 ``` 

By using KNN Regressor I got 
 ```
    Accuracy of training data: 84.2542613795557
    Accuracy of testing data: 89.04882333939983
 ``` 

 By using Random Forest Regressor I got 
 ```
    Accuracy of training data: 90.01102458451159
    Accuracy of testing data: 80.80577386297048
 ``` 


As accuracy of **KNN Regressor** algorithm is more ie. **89.04%**

Hence this model is selected.


<img align="center" alt="acc"  src="https://github.com/Jagannath8/ML-ProjectKart/blob/football/Football%20Team%20Rating%20Prediction/Images/acc.png" />


<a href="https://github.com/Jagannath8">Jagannath Pal</a>
