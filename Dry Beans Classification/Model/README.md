**GOAL**

The goal is to predict Dry Beans.

Dataset can be downloaded from [here](https://www.kaggle.com/josegarban/beans-classification)

**WHAT I HAD DONE**
- Discussed some major columns on which dry beans depends.
- Handling outliers of diagnosis columns. As, it is very important because at last we're predicting dry beans.
- Then I used different classification models present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**
-  Logistic Regression
-  Decission Tree
-  K Nearest Neighbour
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
    Accuracy of training data: 28.655400440852315
    Accuracy of testing data: 27.889324191968655
 ``` 


 By using Decission Tree I got 
 ```
    Accuracy of training data: 100.0
    Accuracy of testing data: 89.49559255631733
 ``` 

 By using K Nearest Neighbour I got 
 ```
    Accuracy of training data: 86.82691298415031
    Accuracy of testing data: 78.20763956904995
 ``` 


 By using Random Forest Classifier I got 
 ```
    Accuracy of training data: 100.0
    Accuracy of testing data: 92.85014691478942
 ``` 


As accuracy of **Random Forest Classifier** algorithm is more ie. **92.85%** ~ **93%**

Hence this model is selected.


<img align="center" alt="acc"  src="https://github.com/Jagannath8/ML-ProjectKart/blob/beans/Dry%20Beans%20Classification/Images/accuracy.png" />

<a href="https://github.com/Jagannath8">Jagannath Pal</a>
