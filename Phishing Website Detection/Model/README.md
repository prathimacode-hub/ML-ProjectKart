# Phishing Website Detection
Phishing attack is a simplest way to obtain sensitive information from innocent users. Aim of the phishers is to acquire critical information like username, password and bank account details. Cyber security persons are now looking for trustworthy and steady detection techniques for phishing websites detection. This paper deals with machine learning technology for detection of phishing URLs by extracting and analyzing various features of legitimate and phishing URLs. Decision Tree, random forest and Support vector machine algorithms are used to detect phishing websites. Aim of the paper is to detect phishing URLs as well as narrow down to best machine learning algorithm by comparing accuracy rate, false positive and false negative rate of each algorithm.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-25/Phishing%20Website%20Detection/Images/web1.jpg)

## Goal
The goal of this project is to make a detection model which will detect the phishing websites depending on various factors, using machine learning algorithms.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/eswarchandt/phishing-website-detector. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-25/Phishing%20Website%20Detection/Dataset) folder too, you can access that!

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-25/Phishing%20Website%20Detection/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. After that I have extracted the features and deployed the ML algorithms.
4. Classification Models -
    - Logistic Regression
    - Decision Tree Classifier
    - Random forest classifier
    - K-Nearest Neighbouring
    - Support Vector Machine (SVM)
    * Gradient Boosting
    - AdaBoost Classifier
    - XgBoost Classifier
5. Finding out something more about Logistic Regression
6. Model Comparison
7. Conclusion


## Model Visualization
1. Random Forest Classifier Confusion Matrix
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-25/Phishing%20Website%20Detection/Images/web2.png)

2. Decision Tree Classifier Confusion Matrix
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-25/Phishing%20Website%20Detection/Images/web3.png)

3. XgBoost Classifier Confusion Matrix
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-25/Phishing%20Website%20Detection/Images/web4.png)

## Model Comparison
We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|92.76|
|Decision Tree Classifier|94.72|
|Random Forest Classifier|97.05|
|KNN Algorithm|63.52|
|Support Vector Machine Algorithm|56.04|
|Gradient Boosting|84.11|
|AdaBoost Classifier|91.04|
|XgBoost Classifier|94.72|
|Logistic Regression on two features|84.11|


## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest and Decision Tree Classifier are having the upper hand in case of this dataset and after this, we can use XgBoost Classifier algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Random forest classifier
2. Decision tree classifier
3. XgBoost Classifier
4. Logistic Regression
5. AdaBoost classifier
6. Gradient Boosting
7. KNN
8. SVM

Hooray!! The models are deployed successfully!

***********************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
