**GOAL**

The goal is to predict percentage of body fat of a person.

Dataset can be downloaded from [here](https://www.kaggle.com/fedesoriano/body-fat-prediction-dataset)

**WHAT I HAD DONE**
- Discussed some major columns on which body fat depends.
- Handling outliers of diagnosis columns. As, it is very important because at last we're predicting body fat of a person.
- Then I used different Regression models present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**
-  Linear Regression
-  Decission Tree Regressor
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
    Accuracy of training data: 99.34389985772462
    Accuracy of testing data: 88.02065759522881
 ``` 

By using Decission Tree Regressor I got 
 ```
    Accuracy of training data: 96.7030531456007
    Accuracy of testing data: 89.27056053767987
 ``` 

 By using Random Forest Regressor I got 
 ```
    Accuracy of training data: 98.38209292469364
    Accuracy of testing data: 91.72551266711207
 ``` 


As accuracy of **Random Forest Regressor** algorithm is more ie. **91.72%** ~ **92%**

Hence this model is selected.


<img align="center" alt="acc"  src="https://github.com/Jagannath8/ML-ProjectKart/blob/bodyfat/Body%20Fat%20Prediction/Images/output.png" />


<a href="https://github.com/Jagannath8">Jagannath Pal</a>
