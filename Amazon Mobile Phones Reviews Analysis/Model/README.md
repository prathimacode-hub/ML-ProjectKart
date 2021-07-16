## Amazon Mobile Phones Reviews Analysis

This model analyze and classify sentiments from reviews.

## Goal

This is one of the major techniques used to analyze customers reviews on different products and find necessary insights fron reviews. The major idea is to classify reviews and find out satisfaction of customers regarding the product.

## Dataset 
You can have dataset from Dataset folder which contains about 3,00,000 data points.

it is availbale on kaggle at https://www.kaggle.com/magdawjcicka/amazon-reviews-2018-electronics


## What Have I Done
I have load necessary libraries, preprossed data, annoted ratings form 3-5 as positive and 1-2 as negative, applied nlp algorithms like stemming, lemmatize and others to remove stopword, punctuations and othersand after visualization I have build logistic regression model.

## Model Used
-  Logistic Regression
-  Random Forest Classifier
-  Decission Tree
-  Support vector machine
-  Voting Classifier(hard voting)
-  Voting Classifier(soft voting)


## Libraries Needed
pandas
numpy
sklearn
pickle
matplotlib
warnings
nltk
tqdm 
sklearn

## Conclusion
- By using Logistic Regression model 
 ```python
    Accuracy achieved :  0.86
 ``` 
 - By using Decission Tree Classifier 
 ```python
    Accuracy achieved :  0.81
 ``` 
 - By using Random Forest Classifier
 ```python
    Accuracy achieved :  0.86
 ``` 
 - By using Support Vector Machine 
 ```python
    Accuracy achieved : 0.874
 ``` 
 - By using Voting Classifier (hard voting) 
 ```python
    Accuracy achieved :  0.86
 ``` 
 - By using Voting Classifier (soft voting) 
 ```python
    Accuracy achieved :  0.871
 ``` 
Random forest classifier gives the highest accuracy which is almost similar to voting classifer(soft voting).

Here, we will consider random forest classifier to be most efficient.
And here model is deployed....

## By:
Drashti Patel
