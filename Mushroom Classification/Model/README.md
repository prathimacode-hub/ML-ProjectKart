# Mushroom Classification Model
Mushroom is one of the fungi types food that has the most potent nutrients on the plant. Mushrooms have major medical advantages such as killing cancer cells. This study aims to find the most appropriate technique for mushroom classification, and mushroom will be classified into two categories, poisonous and nonpoisonous. The proposed approach will implement a different techniques and algorithms like Logistic Regression, Support Vector Machines (SVM), Random Forest, Naive Bayes and k Nearest Neighbors (KNN), on dataset of mushroom classification where the dataset contains types of the mushrooms.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-6/Mushroom%20Classification/Images/266024.jpg)

## Goal
This project is all about deploying classification algorithms and comparing the models.

## Dataset
The dataset is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/uciml/mushroom-classification. Or, you can access the dataset from the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-6/Mushroom%20Classification/Dataset) folder itself, I have uploaded the same.

## What have I done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-6/Mushroom%20Classification/requirements.txt).
2. Importing the dataset in the Jupyter Notebook
3. Then I have divided my project into two halves.
    - **Part A :: Exploratory Data Analysis**
        - Information about the dataset
        - Datatypes used in the dataset
        - Description
        - Label Encoding
        - Visualization
            - Classes
            - Insight 1
            - Insight 2
            - Insight 3
            - Insight 4
    - **Part B :: Classification Algorithms**
        - Spliting the data
        - Logistic Regression
        - K-Nearest Neighbour Algorithm
        - Support Vector Machine Algorithm
        - Naive Bayes Algorithm
        - Decision Tree Classifier
        - Random Forest Classifier
        - Confusion Matrix
4. Conclusion and Comparison

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. sklearn
5. seaborn

## Visualzation
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-6/Mushroom%20Classification/Images/mush1.png)
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-6/Mushroom%20Classification/Images/mush2.png)

## Model Comparison
We have deployed six machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|95.08|
|Decision Tree Classifier|100.0|
|Random Forest Classifier|100.0|
|Naive Bayes Algorithm|92.66|
|KNN Algorithm|100.0|
|Support Vector Machine Algorithm|100.0|

## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Logistic Regression is having the upper hand in case of this dataset and after this, we can use Gausian NB algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Decision Tree Classifier
1. Random Forest Classifier
1. KNN Algorithm
1. Support Vector Machine Classifier
2. Logistic Regression
3. Naive Bayes Algorithm

Hooray!! The models are deployed successfully!

**Through the use of Confusion matrix, we can clearly see that our train and test datas are balanced, so our model is predicting well and also most classification methods scored 100%**

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
