# News Articles Classification
In this project we will be working with a dataset containing headlines of various news articles and their categories along with publication site and other necessary details. We will try to create a model that will classify the news articles to different cateories based on their headlines.

## GOAL - 
     Classify the news articles 

## WHAT I HAVE DONE - 
  Cleared up the data used, removed punctuations and transformed all the letters to lowercase to help maintain uniformity.
  Vectorized the cleared up data.
  Used the resultant with multiple models and compared their acuracy.
   
## MODELS USED-
  Naive Bayes 
  DecisionTree
  Stochastic Gradient Descent Classifier
  XGBClassifier
  Light Gradient Boosting Classifier

  

## LIBRARIES NEEDED

    numpy
    pandas
    seaborn
    matplotlib
    scikit-learn
    lightgbm
    xgboost

## CONCLUSION 
   
### MultinomialNB
```
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     42174
         1.0       0.92      0.91      0.91     11599
         2.0       0.97      0.97      0.97     15575
         3.0       0.92      0.93      0.93      4278
         4.0       0.91      0.92      0.91     10858

    accuracy                           0.97     84484
   macro avg       0.94      0.94      0.94     84484
weighted avg       0.97      0.97      0.97     84484
```
### DecisionTree
```
               precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     42174
         1.0       0.89      0.89      0.89     11599
         2.0       0.93      0.95      0.94     15575
         3.0       0.89      0.85      0.87      4278
         4.0       0.91      0.89      0.90     10858

    accuracy                           0.95     84484
   macro avg       0.92      0.92      0.92     84484
weighted avg       0.95      0.95      0.95     84484
```

### XGBoost
```
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     42174
         1.0       0.91      0.81      0.86     11599
         2.0       0.81      0.98      0.89     15575
         3.0       0.95      0.78      0.86      4278
         4.0       0.94      0.83      0.88     10858

    accuracy                           0.94     84484
   macro avg       0.92      0.88      0.90     84484
weighted avg       0.94      0.94      0.94     84484
```
### SGD
```
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     42174
         1.0       0.93      0.92      0.92     11599
         2.0       0.96      0.98      0.97     15575
         3.0       0.96      0.91      0.94      4278
         4.0       0.93      0.93      0.93     10858

    accuracy                           0.97     84484
   macro avg       0.96      0.95      0.95     84484
weighted avg       0.97      0.97      0.97     84484
```
### LGBM
```
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     42174
         1.0       0.91      0.87      0.89     11599
         2.0       0.89      0.97      0.93     15575
         3.0       0.95      0.86      0.90      4278
         4.0       0.92      0.88      0.90     10858

    accuracy                           0.95     84484
   macro avg       0.93      0.92      0.92     84484
weighted avg       0.95      0.95      0.95     84484
```
