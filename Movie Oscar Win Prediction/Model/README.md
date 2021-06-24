# Movie Oscar Win Prediction
### Abstract
The Academy Awards, popularly known as the Oscars, are awards for artistic and technical merit in the film industry. They are regarded as one of the most significant and prestigious awards in the entertainment industry. Given annually by the Academy of Motion Picture Arts and Sciences (AMPAS), the awards are an international recognition of excellence in cinematic achievements, as assessed by the Academy's voting membership. The various category winners are awarded a copy of a golden statuette as a trophy, officially called the "Academy Award of Merit", although more commonly referred to by its nickname, the "Oscar". The statuette depicts a knight rendered in the Art Deco style.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-18/Movie%20Oscar%20Win%20Prediction/Images/oscar1.jpg)


## Goal
The goal of this project is to make a prediction model, which will predict the chances of winning the Oscar award.


## Dataset
The dataset is collected from the kaggle website. Here is the link for the website : https://www.kaggle.com/balakrishcodes/others?select=Movie_classification.csv.
*The same dataset is uploaded in the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-18/Movie%20Oscar%20Win%20Prediction/Dataset) folder, you can access that too!*

## What Have I done
1. Imported all the required libraries. check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-18/Movie%20Oscar%20Win%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Finding out the correlation between the attributes
4. Spliting the data
5. Prediction Model creation
    - Logistic Regression
    - Decision Tree Classifier
    - Random forest classifier
    - Gaussian NB
    - K-Nearest Neighbouring
    - Support Vector Machine (SVM)
    * Gradient Boosting
    - MLP Classifier
    - Stochastic Gradient Descent (SGD)
    - Linear Discriminant Analysis (LDA)
6. Model Comparison
7. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Seaborn
5. Sklearn

## Model Comparison
We have deployed ten machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.60|
|Decision Tree Classifier|0.47|
|Random Forest Classifier|0.51|
|Gausian NB Algorithm|0.50|
|KNN Algorithm|0.61|
|Support Vector Machine Algorithm|0.50|
|Gradient Boosting|0.64|
|MLP Classifier|0.64|
|Stochastic Gradient Descent|0.64|
|Linear Discriminant Analysis|0.51|


## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Gradient Boosting, MLP and SDG are having the upper hand in case of this dataset and after this, we can use KNN algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Gradient Boosting
2. MLP
3. SGD
4. KNN
5. Logistic Regression
6. Random Forest Classifer
7. LDA
8. SVM
9. Gaussian Naive Bayes
10. Decision Tree Classifier

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
