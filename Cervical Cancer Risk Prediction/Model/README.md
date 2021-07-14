# Cervical Cancer Risk Prediction
Cervical cancer continues to be listed among the top gynaecologic cancers worldwide. According to current data of WHO, Cervical cancer is the second most frequent cancer in women with an estimated 570,000 new cases in 2018 representing 14.7% of all female cancers. Approximately 90% of deaths from cervical cancer occurred in low- and middle-income countries. The high mortality rate from cervical cancer globally could be reduced through a comprehensive approach that includes prevention, early diagnosis, effective screening and treatment programmes. There are currently vaccines that protect against common cancer-causing types of human papilloma virus and can significantly reduce the risk of cervical cancer.

Cervical cancer is the term used to describe tumours that can grow at the lower end of the womb. These tumours usually develop from abnormal cell changes at the entrance to the womb from the vagina (the opening of the cervix). Abnormal cell changes can be detected through screening and then removed. A vaccine against viruses that cause cancer (HPV vaccine) can reduce the risk of cervical cancer.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-39/Cervical%20Cancer%20Risk%20Prediction/Images/cer1.jpg)

## Goal
* Cervical cancer is the leading gynecological malignancy worldwide. 
* The business objective is to build a Machine Learning Prediction Model that predicts the result of Biopsy test and thereby confirming the presence/non-presence of cervical cancer in the patients.
* It is studied that there is more chance of survival if the cancer is detected during its early stages.
* Therefore, the ML model should be helpful in predicting the cancer and thus it can be a huge assest to the medical industry.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset :  https://www.kaggle.com/loveall/cervical-cancer-risk-classification. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-39/Cervical%20Cancer%20Risk%20Prediction/Dataset) folder too, you can access that!

**********************************************
## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-39/Cervical%20Cancer%20Risk%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Cleaning
4. Exploratory Data Analysis
    - Univariate Analysis
    - Multivariate Analysis
5. Feature Engineering
6. Base Line models
    - KNN Classifier
    - Logistic Regression
    - Random Forest Classifier
    - Decision Tree Classifier
    - Gaussian Naive Bayes Classifier
7. Final Model deployment
8. Ensembling
9. Hyper Parameter Tuning
10. Model Comparison
11. Conclusion
********************************************************

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. Tensorflow Backend

**********************************************************
## Exploratory Data Analysis
1. **Biopsy Percentage**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-39/Cervical%20Cancer%20Risk%20Prediction/Images/ce2.png)

2. **Age and Sexual Habits vs Biopsy**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-39/Cervical%20Cancer%20Risk%20Prediction/Images/ce3.png)

3. **Birth control attributes & Age vs Biopsy**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-39/Cervical%20Cancer%20Risk%20Prediction/Images/ce6.png)
**********************************************************
## Model Visualization
- **Feature Engineering**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-39/Cervical%20Cancer%20Risk%20Prediction/Images/ce11.png)

### For more visualizations, check out the [`Images`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-39/Cervical%20Cancer%20Risk%20Prediction/Images) folder!
**************************************************************
## Model Comparison
Mainly we have used three machine learning algortihms but after all those tuning and twaeking procedure, there are 9 models which are the variants of the three main machine learning models. Now let's compare all those models using AUROC value.

|Models|AUROC Value|
|-|-|
|Decision Tree After Sampling|0.910127|
|Random Forest After Sampling|0.883122|
|Decision Tree after Feature Selection|0.971861|
|Random Forest after Feature Selection|0.948052|
|Decision Tree after Hyperparameter Tuning|0.956710|
|Random Forest After Hyperparameter Tuning|0.937229|
|Bagged Decision Tree with Hyperparameter|0.937229|
|Decision Tree ADA Boost with Hyperparameter|0.974026|
|Gradient Boost|0.967532|

*******************************************************************
## Conclusion :
* The **Decision Tree Classification with Ada Boost with Hyperparameter tuning** is the best fitted model for this dataset.
* Along with the previous model, the **Gradient Boosting Model** is also providing good score in terms of model creation.
* We believe that the models we have chosen will assist the medical experts to predict the cancer more precisely than the traditional methods.
- Moreover, the faster diagnosis of early stages of the cancer can be done with the help of this  model. 
- This model will also be cost effective method for low and middle class community. 

********************************************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
