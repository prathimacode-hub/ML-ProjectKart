# Stack Overflow Questions Quality Rating Prediction
Community Question Answering websites (CQA) have a growing popularity as a way of providing and searching of information. CQA attract users as they provide a direct and rapid way to find the desired information. As recognizing good questions can improve the CQA services and the user’s experience, the current study focuses on question quality instead. Specifically, we predict question quality and investigate the features which influence it. The influence of the question tags, length of the question title and body, presence of a code snippet, the user reputation and terms used to formulate the question are tested. For each set of dependent variables, Ridge regression models are estimated. The results indicate that the inclusion of terms in the models improves their predictive power. Additionally, we investigate which lexical terms determine high and low quality questions. The terms with the highest and lowest coefficients are semantically analyzed. The analysis shows that terms predicting high quality are terms expressing, among others, excitement, negative experience or terms regarding exceptions. Terms predicting low quality questions are terms containing spelling errors or indicating off-topic questions and interjections.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-37/Stack%20Overflow%20Questions%20Quality%20Rating%20Prediction/Images/stack3.png)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/imoore/60k-stack-overflow-questions-with-quality-rate.

## Goal
The gaol of this project is to make a prediction model which will predict the quality of the questions from the Stack Overflow website depending on the various factors.
*****************
## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-37/Stack%20Overflow%20Questions%20Quality%20Rating%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Cleaning
4. Data Visualization or, EDA
5. Prediction Models
    - Logistic Regression
    - Random forest Classifier
    - Decision Tree Classifier
    - KNN Classifier
    - Naive Bayes Classifier
    - XgBoosting Classifier
6. Model Comparison
7. Conclusion
***********************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. XgBoost

************************************
## Model Visualization using Confusion Matrix
1. **Logistic Regression** 

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-37/Stack%20Overflow%20Questions%20Quality%20Rating%20Prediction/Images/stack1.png)

2. **XgBoosting Classifier**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-37/Stack%20Overflow%20Questions%20Quality%20Rating%20Prediction/Images/stack2.png)
****************************************
## Comparing the models based on the accuracy scores
We have deployed six machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|87.79%|
|Decision Tree Classifier|79.72%|
|Random Forest Classifier|82.96%|
|Naive Bayes Algorithm|77.94%|
|KNN Algorithm|56.51%|
|XgBoost Classifier|87.86%|

*************************************
## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Logistic Regression and XgBoost Classifier are having the upper hand in case of this dataset and after this, we can use Decision Tree Classifier, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Logistic Regression
2. XgBoosting Classifier
3. Random Forest Classifier
4. Decision Tree Calsssifier
5. Multinomial Naive Bayes Classifier
6. KNN Classifier

Hooray!! The models are deployed successfully!
********************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
