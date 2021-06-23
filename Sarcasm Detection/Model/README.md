# Sarcasm Detection
Sarcasm detection is a very narrow research field in NLP, a specific case of sentiment analysis where instead of detecting a sentiment in the whole spectrum, the focus is on sarcasm. Therefore the task of this field is to detect if a given text is sarcastic or not. This dataset is large compared to the other datasets, yet very small compared to the datasets used in DL models. It is imbalanced, meaning there are more non-sarcastic tweets than sarcastic, which is realistic since sarcasm is very rare in our daily interactions and datasets should represent reality as best as they can. And regarding the type of sarcasm, this dataset captures intended sarcasm, this tweet is labelled as sarcastic because the author wants it to be, it doesn’t consider people’s perception.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-11/Sarcasm%20Detection/Images/sar1.png)

## Goal
The Goal of this project is to, Detecting Sarcasm from news headlines data set using classification algorithms, and compare the algorithms to find out which one is better. Here I have used, Logistic regression , Random forest classifier and Convolution neural network (CNN) for deploying the model.

## Dataset
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection?select=Sarcasm_Headlines_Dataset.json.. I have also uploaded the same in the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-11/Sarcasm%20Detection/Dataset) folder. You can access from there too.

## What Have I Done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-11/Sarcasm%20Detection/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. Then I prepared the Classification Algorithms using the Neural Networks and also the traditional classifiers.
4. Three models are being prepared - 
    - Logistic Regression
    - Random Forest Classifier
    - Convolution Neural Network

5. Conclusion


## Model Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-11/Sarcasm%20Detection/Images/sar2.png)

## Model Comparison
We have deployed three machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.76|
|Random Forest Classifier|0.80|
|Convolution Neural Network|0.95|


## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Convolution Neural Network is having the upper hand in case of this dataset and after this, we can use Logistic Regression, Random Forest Classifier which are also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Convolution Neural Network (CNN)
2. Random Forest Classifier
3. Logistic Regression

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
