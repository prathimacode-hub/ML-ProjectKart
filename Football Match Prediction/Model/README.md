# Football Match Prediction ---- Using the Spanish Super League Dataset
Sports Analysis and Betting have been on the rise lately with the ever increasing ease of Internet accessibility and popularity of Machine Learning. This is an interesting area of research for football, as football is regarded as much more complex and dynamic when compared to a few other sports. It is also the world's most popular sport, played in over 200 countries. Several methodologies and approaches are being taken to develop prediction systems. In this paper, we predict the match outcomes of the Spanish Super League, by performing a detailed study of past football matches and observing the most important attributes that are likely to decide the conclusion. We use algorithms such as Random forest classifer, Decision Tree classifier, KNN classifier, logistic regression, SDG classfier, Gausian NB and then select the best one to give us the target label.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-5/Football%20Match%20Prediction/Images/ft3.jpg)

## Goal
The goal of this project is to predict the match winner according to the prediction model

## Dataset
The dataset is available in the Kaggle website. Here's the link : https://www.kaggle.com/ricardomoya/football-matches-of-spanish-league. Also I have stored the dataset in the `Dataset` folder, you can access from there too.

## What have I done
1. Loading and importing all the libraries, check `requirements.txt`.
2. Importing the dataset in the Jupyter Notebook
3. Then I have divided my project into two halves.

    - **Part A :: Exploratory Data Analysis**
        1. Information about the dataset
        2. Description of the dataset
        3. Analysis of various factors
        4. Most wins by a team
        5. Graphical Visualization
    - **Part B :: Prediction Models**
        1. Spliting the dataset
        2. Logistic Regression
        3. Decision Tree Classification
        4. Random Forest Classifier
        5. K-Nearest Neighbour Algorithm
        6. Gausian NB Algorithm
        7. Support Vector Machine
4. Conclusion and Comparison of the algorithms

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. sklearn
5. seaborn

## Visualzation
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-5/Football%20Match%20Prediction/Images/ft1.png)
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-5/Football%20Match%20Prediction/Images/ft2.png)

## Model Comparison
We have deployed six machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.4072678331090175|
|Decision Tree Classifier|0.40511440107671604|
|Random Forest Classifier|0.40511440107671604|
|Gausian NB Algorithm|0.40659488559892326|
|KNN Algorithm|0.39596231493943473|
|Support Vector Machine Algorithm|0.40511440107671604|

## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Logistic Regression is having the upper hand in case of this dataset and after this, we can use Gausian NB algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Logistic Regression
2. Gausian NB Algorithm
3. Decision Tree Classifier
4. Random Forest Classifier
5. Support Vector Machine
6. KNN Algorithm

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
