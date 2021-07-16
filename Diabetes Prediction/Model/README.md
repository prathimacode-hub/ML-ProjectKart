**GOAL**

The goal is to predict if a person is having Diabetes or not using the diabetes dataset which is present inside the dataset folder. This dataset contains features as Pregnencies, Glucose, BloodPressure, SkinThickness, BMI, Insulin, DiabetesPedegreeFunction and Age. On the basis of these feature we have to predict the outcome i.e whether a peron has diabetes or not.

Dataset can be downloaded from [here](https://www.kaggle.com/mathchi/diabetes-data-set)

**WHAT I HAD DONE**
- I used some scientific librarires like scikit learn , pandas.

- By using this libraries I read that dataset and then go through all the features.Check thier description i.e mean , min of them, max of them and few other things.
 
- After going throught the dataset I found that some of the features such as BloodPressure, BMI, Skinthickness having value 0 in some rows,which is practically not possible.
  So I used some preprocessing techniques to handle those things.In this tehnique I replace that 0 with median of that particular feature.
  
- I Used Correlation coefficients to measure how strong a relationship is between two variables and to detect multicollinearity in between the variables.I haven't found           multicollinearity in between them.

- After that I found that the all the features are in the diffrent range, then I used Standardization to convert those in such a way that thier mean=0 and Std.Deviation = 1.

- After standardizarion I splitted these dataset into four parts i.e Training data , its respective outcome and Test data , also its respective outcome.

- Then I used some Classification models which is Logistic Regression ,Decision Trees, SVM, Random Forest on the training data.

- Then I calculate accuracy of every model on the test and training data and reviewed thier respective confusion matrix.

- After training and predicting values ,I saved the respective model using pickle and os library.
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
- Pickle
- OS

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
 
 Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest Classifier and Logistic Regression Algorithm are having the upper hand in case of this dataset and after this, we can also SVM algorithm, which is also having good score as compared to the Decision Tree Classifier.
 
 Best Fitted Model as per ranking(Accuracy):
 
 1. Random Forest Classifier
 2. Logistic Regression
 3. Decision Tree Classifier
 4. Support Vector Machine(SVM)
 
 Finally!!! The models are deployed successfully!
 
 
 
 Arihant Rode @arihantrode89
 
