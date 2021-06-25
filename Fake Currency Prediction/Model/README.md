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



**Selection Of Model**

- we applied two models Logistic Regression and Random Forest Classifier.
- As we can see random forest classifier have higher accuracy therefore we dump this model to make (.pickle) file which will be used in flask to deploy the model.



**Deployment Of Model**

- Deployed Model using Flask.
- Created a Tensorflow environment in anaconda prompt.
- Created a app.py file which will comprise of all Backend stuff.
- Also created index.html for our front page which consist of placeholder for 4 features.
- When user will give features data and press (Predict) button it will render to (/predict) page.
- Predict page will give us the result about whether the note is fake or not. 

 




