**GOAL**

The goal is to predict if a student is placed or not according to his/her percentage and other factors.

Dataset can be downloaded from [here]( https://www.kaggle.com/benroshan/factors-affecting-campus-placement)

**WHAT I HAD DONE**
- Discussed some major columns on which placement depends.
- Handling outliers of diagnosis columns. As, it is very important because at last we're predicting placenment of a student.
- Then I used different Regression models present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**
-  Logistic Regression
-  Decission Tree Classifier
-  K Nearest Neighbour Classifier
-  Random Forest Classifier

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn

**CONCLUSION**

By using Logistic Regression I got 
 ```
    Accuracy of training data: 86.04651162790698
    Accuracy of testing data: 95.34883720930233
 ``` 

By using Decission Tree Classifier I got 
 ```
    Accuracy of training data: 100.0
    Accuracy of testing data: 86.04651162790698
 ``` 
 
 By using KNN Classifier I got 
 ```
    Accuracy of training data: 86.62790697674419
    Accuracy of testing data: 90.69767441860465
 ``` 

 By using Random Forest Classifier I got 
 ```
    Accuracy of training data: 89.53488372093024
    Accuracy of testing data: 88.37209302325581
 ``` 


As accuracy of **Logistic Regression** algorithm is more ie. **95.34%**

Hence this model is selected.


<img align="center" alt="acc"  src="https://github.com/Jagannath8/ML-ProjectKart/blob/campus/Campus%20Placement%20Prediction/Images/accuracy.png" />


<a href="https://github.com/Jagannath8">Jagannath Pal</a>
