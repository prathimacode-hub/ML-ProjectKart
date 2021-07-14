# Dogecoin Price Prediction
Dogecoin (/ˈdoʊ(d)ʒkɔɪn/ DOHZH-koyn or DOHJ-koyn, code: DOGE, symbol: Ð) is a cryptocurrency created by software engineers Billy Markus and Jackson Palmer, who decided to create a payment system as a joke, making fun of the wild speculation in cryptocurrencies at the time. Despite its satirical nature, some consider it a legitimate investment prospect. Dogecoin features the face of the Shiba Inu dog from the "Doge" meme as its logo and namesake. It was introduced on December 6, 2013, and quickly developed its own online community, reaching a market capitalization of US$85,314,347,523 on May 5, 2021.

Originally formed as a joke, Dogecoin was created by IBM software engineer Billy Markus and Adobe software engineer Jackson Palmer. They wanted to create a peer-to-peer digital currency that could reach a broader demographic than Bitcoin. In addition, they wanted to distance it from the controversial history of other coins. Dogecoin was officially launched on December 6, 2013, and within the first 30 days, there were over a million visitors to Dogecoin.com.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge1.jpeg)

## Goal
The goal of this project is to make a Prediction model which will predict the price of the Dogecoin in the future times depending on the previous parameters.

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/dhruvildave/dogecoin-historical-data. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-24/Dogecoin%20Price%20Prediction/Dataset) folder too, you can access that!

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Visualization
    - Data v/s Volumn graph
    - Performance of Dogecoin in 2021
    - Opening price visualization for 2021
    - Maximum price visualization for 2021
    - Lowest price visualization for 2021
    - Closing price visualization for 2021
    - Adjustment price visualization for 2021
    - Correlation Heatmap
4. Prediction Models
    - Spliting the dataset into 70:30 ratio
    - Deploying the models
        - Linear Regression
        - Decision Tree Regression
        - Random Forest Regression
        - Lasso Regression
        - Ridge Regression
        - MLP Regression
        - XgBoost Regression
        - Gradient Boosting Regression
        - Support Vector Regression
5. Comparing the accuracy of the models
6. Conclusion


## Dogecoin Data Visualization
1. **Data v/s Volumn graph**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge2.png)

2. **Performance of Dogecoin in 2021**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge3.png)

3. **Opening price visualization for 2021**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge4.png)

4. **Maximum price visualization for 2021**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge5.png)

5. **Lowest price visualization for 2021**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge6.png)

6. **Closing price visualization for 2021**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge7.png)

7. **Adjustment price visualization for 2021**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-24/Dogecoin%20Price%20Prediction/Images/doge8.png)


*************************************************
## Model Comaparison
We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|98.79%|
|Decision Tree Regressor|97.50%|
|Random Forest Regressor|98.04%|
|Lasso Regression|57.15%|
|Ridge Regression|97.90%|
|XgBoost Regressor|98.65%|
|MLP Regressor|-104%|
|Gradient Boosting Regressor|98.14%|
|Support Vector Regressor|-8.85%|


## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Linear Regression is having the upper hand in case of this dataset and after this, we can use  XgBoosting Regressor, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Linear Regression
2. XgBoosting Regression
3. Gradient Boosting Regression
4. Random Forest Regression
5. Ridge Regression
6. Decision Tree Regressor
7. Lasso Regression
8. Support Vector Regressor
9. MLP Regressor


Hooray!! The models are deployed successfully!

*********************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
