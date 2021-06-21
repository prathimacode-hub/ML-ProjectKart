# Cryotherapy Analysis
Cryotherapy is a treatment where your healthcare provider applies extreme cold to freeze and destroy abnormal tissue. To create this severe cold, your provider will use a substance like liquid nitrogen or argon gas.

Cryotherapy can be used to treat a variety of skin conditions and some cancers, including prostate and liver cancer. This therapy can treat tissue externally (on the skin) and internally (inside the body).

This treatment can also be called cryoablation.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-7/Cryotherapy%20Analysis/Images/cr1.jpg)

## Goal
Here in this project we are going to analyze the cryotherapy dataset and will deploy several machine learning algorithm models, such as, Random Forest Classifier, Decision Tree Classifier, KNN Algorithm, Gausian NB, Logistic Regression, Support Vector Machine, Gradient Boosting, Adaboost and ANN. After deploying all the models we will do a comparative analysis among them to determine the accurate model.

## Dataset
The dataset is available in the Kaggle website. Here's the link : https://www.kaggle.com/mmkvarma/cryotherapy-analysis. Also I have stored the dataset in the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-7/Cryotherapy%20Analysis/Dataset) folder, you can access from there too.

## What have I done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-7/Cryotherapy%20Analysis/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. After that I have a few data analysis and then created the models -
    - Classification Models
        - K-Nearest Neighbour Algorithm
        - Decision Tree Classifier
        - Random Forest Classifier
        - Gausian NB Algorithm
        - Logistic Regression
        - Support Vector Machine
        - Gradient Boosting Algorithm
        - AdaBoost Algorithm
        - Artificial Neural Network
    - Accuracy Score of the algorithms
    - ROC Curve of the algorithms
4. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. sklearn
5. seaborn

## Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-7/Cryotherapy%20Analysis/Images/cr2.png)

## Model Comparison
We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|83.33|
|Decision Tree Classifier|69.17|
|Random Forest Classifier|83.33|
|Naive Bayes Algorithm|86.67|
|KNN Algorithm|84.17|
|Support Vector Machine Algorithm|83.33|
|Gradient Boosting Algorithm|83.33|
|AdaBoosting Classifier|83.33|
|Artificial Neural Network|86.67|


## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Artificial Neural Network and Naive Bayes Algorithm are having the upper hand in case of this dataset and after this, we can use Logistic regression, Random Forest Classifier, SVM, Gradient Boosting, AdaBoosting algorithm, which are also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. ANN
2. Naive Bayes
3. Logistic Regression
4. Randm Forest classifier
5. SVM
6. Gradient Boosting
7. AdaBoosting
8. KNN
9. Decision Tree Classifier
 
 
********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
