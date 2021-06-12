**GOAL**
The goal is to predict the price of house(dependent variable) located in the
cities of US, with the help of other essential features (independent variable) available in
our dataset.


**WHAT I HAD DONE**
- Discussed some major columns on which price depends.
- Handling outliers of price columns. As, it is very important because at last we're predicting price and disturbance in its distribution might   hit hard to our predictions.
- Then I used different classification models present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**
-  Linear Regression
-  K-Nearest Neighbors
-  Random Forest Regressor
-  Decision Tree Regressor

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn
- One hot encoding

**CONCLUSION**
By using Linear Regression I got 
 ```python
    Train set Accuracy: 68.77134166176889
    Test set Accuracy:   0.7861937862204528
 ``` 

 By using K-nearest neighbors I got 
 ```python
    Train set Accuracy:  55.48869876436817
    Test set Accuracy:   49.0835860505657
 ``` 
By using Random Forest Regressor I got 
 ```python
    Train set Accuracy: 94.98233899753667
    Test set Accuracy:   72.07665288364437
 ``` 
By using Decision Tree Regressor I got 
 ```python
    Train set Accuracy: 99.91921367119716
    Test set Accuracy:   37.59405452806801
 ``` 

