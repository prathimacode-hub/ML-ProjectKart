# Hotel Rating Prediction
Hotel rating systems are used in almost all countries. The policy makers, managers, and researchers take this process seriously, and contribute in enhancing the system to reflect the needs of the modern traveler. Hotels also invest a lot for getting the desired star ratings. However, at the same time, apart from the guidelines and manuals of the star rating schemes, there is hardly any reliable source of information explaining the principles on which the star rating process is based. The available information can be confusing as different rating systems have different criteria for hotel evaluation. Considering this challenge, this book attempts to bring the star rating process to life through the principles of service quality management because hotel rating systems claim to raise standards of service. Such principles were identified through hundreds of research studies and existing hotel rating systems around the world. This book focusses on making the hotel rating process simple to understand for the benefit of students, managers, and policymakers.

Here to deploy the Hotel Rating Prediction model, I have used nine Machine learning algortihms. The models are fitted succesfully, and at the end all these models are going evaluated based on the accuracy scores.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-8/Hotel%20Rating%20Prediction/Images/hotel2.jpg)

## Goal
The goal of this project is to build the model for the Hotel Rating Prediction. For that I have used nine Machine Learning Models, The models are fitted succesfully, and at the end all these models are going evaluated based on the accuracy scores.

## Dataset
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/andrewmvd/trip-advisor-hotel-reviews. I have uploaded the same, you can access from the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-8/Hotel%20Rating%20Prediction/Dataset) folder too.

## What have I done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-8/Hotel%20Rating%20Prediction/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. After that I have divided the project into two halves -
    - Part A :: Exploratory Data Analysis
        - Most searched words using word-cloud
        - Positive Sentiment Distribution
        - Negative Sentiment Distrbution
        - Visualization using Pair Plot
        - Visualization using Joint Plot
        - Visualization using 3D Scatter Plot
        - Outlier Removal
    - Part B :: Prediction Models
        - K-Nearest Neighbour Algorithm
        - Decision Tree Classifier
        - Random Forest Classifier
        - Gausian NB Algorithm
        - Logistic Regression
        - Support Vector Machine
        - Gradient Boosting Algorithm
        - AdaBoost Algorithm
        - Artificial Neural Network
        - Truncated SVD
4. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. sklearn
5. seaborn

## Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-8/Hotel%20Rating%20Prediction/Images/newplot.png)

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-8/Hotel%20Rating%20Prediction/Images/newplot%20(1).png)

## Model Comparison
We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|49.51|
|Decision Tree Classifier|38.88|
|Random Forest Classifier|44.63|
|Naive Bayes Algorithm|49.22|
|KNN Algorithm|42.76|
|Support Vector Machine Algorithm|46.13|
|Gradient Boosting Algorithm|47.49|
|AdaBoosting Classifier|48.34|
|Artificial Neural Network|49.06|

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-8/Hotel%20Rating%20Prediction/Images/newplot%20(2).png)

## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Logistic Regression and Naive Bayes Algorithm are having the upper hand in case of this dataset and after this, we can use ANN, Random Forest Classifier, SVM, Gradient Boosting, AdaBoosting algorithm, which are also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Logistic Regression
2. Gausian Naive Bayes
3. Artificial Neural Network
4. AdaBoosting
5. Gradient Boosting
6. Support Vector Machine
7. Random Forest Classifier
8. K-Nearest Neighbours
9. Decision Tree Classifier


Hooray!! The models are deployed successfully!

 
********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
