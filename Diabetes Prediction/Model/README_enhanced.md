**GOAL**

The goal is to predict if a person is having Diabetes or not.

Dataset can be downloaded from [here](https://www.kaggle.com/mathchi/diabetes-data-set)

**WHAT I HAD DONE**
- Discussed some major columns on which diabetes are depend.
- I found some zeros values in dataset that can't be zero.
- Use Correlation coefficients to measure how strong a relationship is between two variables and to detect multicollinearity.
- Preprocess data and solve that zero values problem
- Standarized the data.
- Then I used some Classification models present in sklearn to train the model.
- Also I have used SVM models present in sklearn to train the model.
.

**MODELS USED**
-  Logistic Regression
-  Decision Tree Classifier 
-  Support Vector Machine (SVM)
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
    Accuracy of training data: 0.7687296416938111
    Accuracy of testing data: 0.8181818181818182
 ``` 
 
By using Decision Tree Classifier I got 
 ```
    Accuracy of training data: 1.00
    Accuracy of testing data: 0.7597402597402597
 ``` 
By using SVM I got 
 ```
    Accuracy of training data: 0.8143322475570033
    Accuracy of testing data: 0.7727272727272727
 ``` 

By using Random Forest Classifier I got 
 ```
    Accuracy of training data: 1.00
    Accuracy of testing data:  0.8181818181818182
 ``` 
 
