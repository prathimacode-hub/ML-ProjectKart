# Resume Categorizing
Companies often receive thousands of resumes for each job posting and employ dedicated screening officers to screen qualified candidates. Hiring the right talent is a challenge for all businesses. This challenge is magnified by the high volume of applicants if the business is labour-intensive, growing, and facing high attrition rates. IT departments are short of growing markets. In a typical service organization, professionals with a variety of technical skills and business domain expertise are hired and assigned to projects to resolve customer issues. This task of selecting the best talent among many others is known as Resume Screening. Typically, large companies do not have enough time to open each CV, so they use machine learning algorithms for the Resume Screening task.

Here I am going to use several machine learning algorithms for the categorization procedure of the resumes, and finally the models are going to be checked based on the accuracy score.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-9/Resume%20Categorizing/Images/resume4.jpg)

## Goal
The goal of this project is to build the model for the Resume Categorizing. For that I have used eight Machine Learning Models, The models are fitted succesfully, and at the end all these models are going evaluated based on the accuracy scores.

## Dataset
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/andrewmvd/trip-advisor-hotel-reviews. I have uploaded the same, you can access from the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-9/Resume%20Categorizing/Dataset) folder too.

## What have I done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-9/Resume%20Categorizing/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. After that I have divided the project into two halves -
    - **Part A :: Exploratory Data Analysis**
        - Distinct Values of the dataset
        - Graphical representation of job categories
        - Category-wise Distribution
        - Data Cleaning
        - Label Encoder
    - **Part B :: Classification Algorithms**
        - K-Nearest Neighbour Algorithm
        - Decision Tree Classifier
        - Random Forest Classifier
        - Gausian NB Algorithm
        - Logistic Regression
        - Support Vector Machine
        - AdaBoost Algorithm
        - Artificial Neural Network
4. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. sklearn
5. seaborn

## Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-9/Resume%20Categorizing/Images/resume2.png)

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-9/Resume%20Categorizing/Images/resume5.png)

## Model Comparison
We have deployed eight machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Test Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.99|
|Decision Tree Classifier|0.99|
|Random Forest Classifier|0.99|
|Naive Bayes Algorithm|0.99|
|KNN Algorithm|0.98|
|Support Vector Machine Algorithm|0.99|
|AdaBoosting Classifier|0.23|
|Artificial Neural Network|0.99|


## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Logistic Regression, Decision tree Classifier, Random Forest Classifier, Naive Bayes Algorithm, Support Vector Machine, Artificial Neural Network Algorithm are having the upper hand in case of this dataset and after this, we can use K-Nearest Neighbours algorithm which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Logistic Regression
2. Decision tree Classifier
3. Random Forest Classifier
4. Naive Bayes Algorithm
5. Support Vector Machine
6. Artificial Neural Network
7. K-Nearest Neighbours
8. AdaBoosting Classifier


Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
