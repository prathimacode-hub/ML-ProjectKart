# Automated Essay Grading

## Goal
The goal of this project is to make a prediction model which will give scoring to student-written essays.

## DATASET
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/c/asap-aes/overview. I have uploaded the
same in [`Dataset`](https://github.com/prathimacode-hub/ML-ProjectKart/tree/main/Automated%20Essay%20Grading/Dataset) folder too, you can access that!

## LIBRARIES NEEDED

- Pandas
- Numpy
- Sklearn
- NLTK
- Keras

## WHAT I HAD DONE
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/prathimacode-hub/ML-ProjectKart/blob/main/Automated%20Essay%20Grading/Model/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Loading Test and Train from Dataset
4. Apply K Fold Cross Validation and extract sentences from essays from training data.
5. Apply Word2Vec Model to convert sentences into test and training word vectors.
6. Apply Different Models for prediction and calculate their different evaluation metrics mainly Cohen Kappa Score.
7. Prediction Models Used:
    - LSTM
    - Linear Regression Model
    - Gradient Boosting regressor
    - Logistic Regression
    - XgBoosting Classifer
    - Decision Tree Classifier
    - Random Forest Classifier
    - KNN
    - Support Vector Regression
9. Choose Best Model which has highest kappa score for final prediction for the scores on the test data.

## Model Comparison
We have deployed 9 machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the Kappa score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|LSTM|0.87|
|Linear Regression Model|0.86|
|Gradient Boosting regressor|0.95|
|Logistic Regression|0.46|
|XgBoosting Classifer|0.89|
|Decision Tree Classifier|0.85|
|Random Forest Classifier|0.94|
|KNN|0.92|
|Support Vector Regression|0.60|

*****************************************

## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Gradient Boosting regressor Algorithm gives highest cohen kappa score(0.95) and will provide best prediction for scores for our essay data.**

Code Contributed by Akash Jain **(@Akash20x)**
