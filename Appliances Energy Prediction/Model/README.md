# Appliances Energy Prediction
In this time of global uncertainty world needs energy and in increasing quantities to support economic and social progress and build a better quality of life, in particular in developing countries. But even in today’s time there are many places especially in developing world where there are outages. These outages are primary because of excess load consumed by appliances at home. Heating and cooling appliances takes most power in house. In this project we will be analysing the appliance usage in the house gathered via home sensors. All readings are taken at 10 mins intervals for 4.5 months . The goal is to predict energy consumption by appliances .

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-36/Appliances%20Energy%20Prediction/Images/app1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/sohommajumder21/appliances-energy-prediction-data-set.I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-36/Appliances%20Energy%20Prediction/Dataset) folder too, you can access that!

## Goal
The goal of this project is to make a prediction model which will predict the enery consumption by the appliances based on the given dataset.
**************************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-36/Appliances%20Energy%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Cleaning
4. Data Visualization
5. Data Pre-processing
6. Prediction Model Deployment
    - Linear regression
    - Random Forest regression
    - Lasso regression+
    - Ridge regression
    - Gradient Boosting regression
    - XGBoosting regression
    - MLP regression
    - Support vector regressor
    - Extra Tree Regressor
    - KNN Regression
7. Parameter Tuning
8. Feature Importance
9. Conclusion

***************************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. XgBoost

*********************************
## Data Visualization
1. **Histogram of all the features to understand the distribution**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-36/Appliances%20Energy%20Prediction/Images/app2.png)

2. **focussed displots for RH_6 , RH_out , Visibility , Windspeed due to irregular distribution**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-36/Appliances%20Energy%20Prediction/Images/app3.png)

3. **Distribution of values in Applainces column**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-36/Appliances%20Energy%20Prediction/Images/app4.png)
************************************
## Model Visualization
- **Different Accuracy checking parameters for different models**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-36/Appliances%20Energy%20Prediction/Images/app5.png)
*****************************************
## Conclusion
1. The best Algorithm to use for this dataset Extra Trees Regressor

2. The untuned model was able to explain 57% of variance on test set .

3. The tuned model was able to explain 63% of varaince on tese set which is improvement of 10%

4. The final model had 22 features

5. Feature reduction was not able to add to better R2 score

**************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
