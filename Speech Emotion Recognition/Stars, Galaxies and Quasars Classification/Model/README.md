# Stars, Galaxies and Quasars Classification
The Sloan Digital Sky Survey is a project which offers public data of space observations. Observations have been made since 1998 and have been made accessible to everyone who is interested. 
For this purpose a special 2.5 m diameter telescope was built at the Apache Point Observatory in New Mexico, USA. The telescope uses a camera of 30 CCD-Chips with 2048x2048 image points each. The chips are ordered in 5 rows with 6 chips in each row. Each row observes the space through different optical filters (u, g, r, i, z) at wavelengths of approximately 354, 476, 628, 769, 925 nm.
The telescope covers around one quarter of the earth's sky - therefore focuses on the northern part of the sky.

**For more information about this awesome project - please visit their website:** http://www.sdss.org/

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/Images/star4.jpg)

## Goal
The goal of this project is to make a perfect classification model according to the data collected by the survey work.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/dmvreddy91/usahousing. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/Dataset) folder too, you can access that!

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Feature Description
4. Data Exploration
5. Univariate Analysis
6. Multivariate Analysis
7. Feature Engineering
8. classification Models -
    1. KNN Classifier
    2. Random forest classifier
    3. XgBoost classifier
    4. Support Vector Machine
    5. Naive Bayes classifier
    6. model comparison
9. K Fold Cv deployment
10. Hyperparameters Tuning
11. Evaluation
12. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. XgBoost

## Model Visualization
1. Univariate Analysis [using RedShift]

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/Images/star1.png)

2. Univariate Analysis [using dec]

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/Images/star2.png)

3. Multivariate Analysis

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/Images/star3.png)

4. Feature Importance

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-23/Stars%2C%20Galaxies%20and%20Quasars%20Classification/Images/star4.png)

## Model Comparison
We have deployed five machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|XgBoosting Classifier|99.51%|
|Random Forest Classifier|99.28%|
|Naive Bayes|97.79%|
|Support Vector Machine|95.45%|
|K-Nearest Neighbouring|93.33%|

After these models, I have used K-fold CV on the top two algorithms.
|Name of the Model|Accuracy Score|
|:---:|:---:|
|XgBoosting Classifier on 10-fold CV|99.36%|
|Random Forest Classifier on 10-fold CV|99.07%|

Now applying the Hyper parameters tuning on the XgBoost Classifier on 10-fold CV, accuracy score shows, 99.36%

## Conclusion
After so much of comparison between the models deployed using the dataset, it is clear that **XgBoost Classifier with 10-fold CV on Hyperparameters tuning** is the best model with the accuracy score of 99.36, that's awesome!

After this model we can also use the Random Forest Classifier model, which is also having a good score above 99%.

Hence, the Best Model for this dataset is - **XgBoost Classifier with 10-fold CV on Hyperparameters tuning**

**********************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

