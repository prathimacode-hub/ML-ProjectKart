# Olympic Medal Prediction

## Goal
The goal of this project is to make a prediction model which will predict whether an athlete will win medal or not. 

## DATASET
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results. I have uploaded the
same in [`Dataset`](https://github.com/prathimacode-hub/ML-ProjectKart/tree/main/Olympic%20Medal%20Prediction/Dataset) folder too, you can access that!

## LIBRARIES NEEDED

- Pandas
- Numpy
- Sklearn
- Matplotlib 

## WHAT I HAD DONE
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/prathimacode-hub/ML-ProjectKart/blob/main/Olympic%20Medal%20Prediction/Model/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Loading and Cleaning the dataset. 
4. Encoding textual columns. 
5. Select best 10 features and make a new dataframe using them
6. Split dataframe into train and test data along with scaling. 
7. Apply different classification models and calculate their accuracy.
8. Choose best model for our prediction which has highest accuracy. 
9. Make the final prediction using best model. 

## Model Comparison
We have deployed 6 machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the efficiency of the models based on the accuracy of each of the models. Now let's take a look at model with their accuracy. 

|Name of the Model|Accuracy|
|:---:|:---:|
|Logistic Regression|85.357825|
|MultinomialNB|85.367968|
|Decision Tree|84.095457|
|Random Forest|88.779773|
|Gradient Boosting|88.514205|
|Neural Network|87.904691|

*****************************************

## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest Classifier Model gives highest accuracy and will provide best prediction.**

Code Contributed by Akash Jain **(@Akash20x)**
