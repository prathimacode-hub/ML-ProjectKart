# Coffee Production Prediction

## Goal
The goal of this project is to make a prediction model which will give total production of the coffee from year 1990-2018.

## DATASET
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/yamaerenay/ico-coffee-dataset-worldwide . I have uploaded the
same in [`Dataset`](https://github.com/prathimacode-hub/ML-ProjectKart/tree/main/Coffee%20Production%20Prediction/Dataset) folder too, you can access that!

## LIBRARIES NEEDED

- Pandas
- Numpy
- Sklearn
- Matplotlib

## WHAT I HAD DONE
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/prathimacode-hub/ML-ProjectKart/blob/main/Coffee%20Production%20Prediction/Model/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Loading different data files from a Dataset. 
4. Combine them to make a dataframe suitable for prediction. 
5. Split dataframe into train and test data along with scaling. 
6. Apply different regressor models to predict total production and calculate their evaluation metrics such as RMSE and R2 score. .
7. Choose best model for our prediction which has lowest RMSE and high R2 score. 

## Model Comparison
We have deployed 7 machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the efficiency of the models based on the rmse and r2 score of each of the models. Now let's take a look at model with their rmse and r2 score. 

|Name of the Model|RMSE |R2 Score |
|:---:|:---:|:---:|
|Linear Regression|587.702473|0.996282|
|Lasso Regression|562.750463|0.996591|
|Ridge Regression|202.901006|0.999557|
|Support Vector Regression|8643.103733|0.195790|
|Gradient Boosting Regressor|6140.180115|0.594125|
|Decision Tree Regression|6381.033368|0.561659|
|Random Forest Regression|7976.435049|0.315068|

*****************************************

## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Ridge regressor Algorithm gives low RMSE and high R2 score and will provide best prediction for total production of Coffee.**

Code Contributed by Akash Jain **(@Akash20x)**
