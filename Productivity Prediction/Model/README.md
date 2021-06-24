# Productivity Prediction Model
The Garment Industry is one of the key examples of the industrial globalization of this modern era. It is a highly labour-intensive industry with lots of manual processes. Satisfying the huge global demand for garment products is mostly dependent on the production and delivery performance of the employees in the garment manufacturing companies. So, it is highly desirable among the decision makers in the garments industry to track, analyse and predict the productivity performance of the working teams in their factories.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-16/Productivity%20Prediction/Images/pro2.jpg)

## Goal
It is highly desirable among the decision makers in the garments industry to track, analyse and predict the productivity performance of the working teams in their factories.

## Dataset
The dataset which is used here, collected from kaggle website. Here is the link : https://www.kaggle.com/ishadss/productivity-prediction-of-garment-employees. You can find out the same from the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-16/Productivity%20Prediction/Dataset) folder too.

## What Have I done
1. Firstly, install the required libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-16/Productivity%20Prediction/requirements.txt).
2. Open the Jupyter Notebook file in the Anaconda Navigator.
3. Import the dataset.
4. Then I have divided the project into two halves - 
    - Part A : Exploratory Data Analysis
        - Categorial Features
        - Numeric Features
        - Actual v/s Predicted Productivity
        - Heatmap
        - One Hot Encoding
        - Label Encoding
        - Target Label Productivity
        - Balancing Data
        - Spliting the Dataset
    - Part B :: Prediction Models
        - Machine Learning Classifiers to train the model
        - Tuning Random Forest Classifier
5. Conclusion and Comparison of the algorithms

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn

## Visualization of various features
- Targeted Productivity v/s Actual Productivity

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-16/Productivity%20Prediction/Images/pro3.png)

- HeatMap Creation

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-16/Productivity%20Prediction/Images/pro4.png)

- Features Visualization

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-16/Productivity%20Prediction/Images/pro5.png)

## Model Comparison
We have deployed seven machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the F-measure accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.66|
|Decision Tree Classifier|0.79|
|Random Forest Classifier|0.84|
|Gausian NB Algorithm|0.54|
|KNN Algorithm|0.79|
|Support Vector Machine Algorithm|0.65|
|Linear Discriminant Analysis (LDA)|0.83|
|Tuned Random Forest Classifier|0.86|


### Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest Classifier is having the upper hand in case of this dataset and after this, we can use Linear Discriminant Analysis algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Tuned Random Forest Classifier
2. Linear Discriminant Analysis
3. Decision tree classifier
4. KNN algorithms
5. Logistic Regression
6. SVM
7. Gaussian Naive Bayes classifier

Hooray!! The models are deployed successfully!
********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
