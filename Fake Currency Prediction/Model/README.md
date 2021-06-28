# About the dataset
Dataset can be downloaded from [here](https://www.kaggle.com/dsabhis04/bank-note-data-set)

## Attributes in the dataset
**1) Target (0 = Given note is not a fake note, 1 = Given Note is a fake note)  


Four real-valued features:

**a) variance (variance of Wavelet Transformed image)**

**b) skewness (skewness of Wavelet Transformed image)**

**e) curtosis (curtosis of Wavelet Transformed image)**

**f) entropy (entropy of image)**



# About the model

**GOAL**

The goal is to predict whether a given note is fake or not.


**WHAT I HAD DONE**
- Data cleaning
- Data exploration
- Data Processing
- Data Modelling and evaluation 


**MODELS USED**
-  Logistic Regression
-  Random Forest Classifier
-  Decision Tree Classifier



**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn
- tensorflow
- flask





**Accuracy**
By using Logistic Regression I got 
 ```
    Accuracy : 0.9733009708737864
 ``` 
By using Random Forest Classifier I got 
 ```
    Accuracy : 0.9878640776699029
 ``` 
By using Decision tree Classifier I got 
 ```
    Accuracy : 0.9854368932038835
 ``` 



**Selection Of Model**

- We applied three models Logistic Regression, Random Forest Classifier and Decision tree Classifier.
- As we can see random forest classifier have higher accuracy therefore we dump this model to make (.pickle) file which will be used in flask to deploy the model.



**Deployment Of Model**

- Deployed Model using Flask.
- Created a Tensorflow environment in anaconda prompt.
- Created a app.py file which will comprise of all Backend stuff.
- Also created index.html for our front page which consist of placeholder for 4 features.
- When user will give features data and press (Predict) button it will render to (/predict) page.
- Predict page will give us the result about whether the note is fake or not. 





**Description**

- Fake Currency Detection is a task of binary classification in machine learning because bank notes can be either real or fake.
- If we have enough data on real and fake banknotes, we can use that data to train a model that can classify the new banknotes as real or fake.
- After training the model if we want to deploy it for real life purpose we can use FLASK.




**Conclusion**

- Fake Currency Detection is a real problem for both individuals and businesses.
- So by training this script in machine learning will help many individuals.
- Users will have a webpage content related to model in which they have to give value to the features required.
- After giving value to the features they can get to know the results that whether the given note is real or fake.

 

# Author :
- ### Medhir Manoj
 

















