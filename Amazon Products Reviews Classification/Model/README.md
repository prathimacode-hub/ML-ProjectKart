# Amazon Products Reviews Classification
Amazon.com, Inc. (/ˈæməzɒn/ AM-ə-zon) is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as "one of the most influential economic and cultural forces in the world", as well as the world's most valuable brand.

Jeff Bezos founded Amazon from his garage in Bellevue, Washington,on July 5, 1994. It started as an online marketplace for books but expanded to sell electronics, software, video games, apparel, furniture, food, toys, and jewelry. In 2015, Amazon surpassed Walmart as the most valuable retailer in the United States by market capitalization. In 2017, Amazon acquired Whole Foods Market for US$13.4 billion, which substantially increased its footprint as a physical retailer. In 2018, its two-day delivery service, Amazon Prime, surpassed 100 million subscribers worldwide.

Sentiment analysis is a NLP task which aims to classify a text based on the sentiment it conveys, aka its *polarity* (whether it is positive, neutral or negative). A typical business-oriented application is to analyze product reviews and customer feedbacks.

The dataset which we investigate contains tens of thousands of Amazon reviews, which have been labeled as positive or negative by looking at the score given by users. We show different approaches to the problem of sorting them in the correct class based on the content of the review, both using text-feature extraction and deep learning. 

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/ama1.jpg)

## Dataset
The dataset is collected from the Kaggle website. Here is the link : https://www.kaggle.com/kritanjalijain/amazon-reviews?select=train.csv.

## Goal
The goal of this project is to make a classifiation model which will classify the products review enlisted in the Amazon Inc website, so that it can help the company for their betterment, and also they can rectify their faults depending on the users' experience.
***************************************************
## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Preparation
    - Packages
    - Loading Dataset
4. Text Features
    - CountVectorizer + MultinomialNB
    - TfidfVectorizer + MultinomialNB
    - CountVectorizer + MultinomialNB w/o stopwords
    - TfidfVectorizer + MultinomialNB w/o stopwords
    - CountVectorizer + MultinomialNB lemmatized
    - Model Comparison
5. Deep Learning
    - LSTM
    - RoBERTa
    - Model Comparison
6. Overall Comparison
7. Conclusion

***************************************************
## Libraries used
|Numpy|Pandas|Matplotlib|Seaborn|Sklearn|collections|nltk|spacy|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|langid|plotly|cufflinks|fastbook|fastai|transformers|fsspec|os|

*************************************************************
## Model Visualization
1. **Most frequent n-grams**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/newplot.png)

2. **Most frequent n-grams w/o stopwords**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/newplot%20(1).png)

3. **Most frequent 2/3-grams w/o stopwords - Positive reviews**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/newplot%20(2).png)

4. **Most frequent 2/3-grams w/o stopwords - Negative reviews**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/newplot%20(3).png)

5. **RoBERTa Model Learning rate**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/ama2.png)      ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-40/Amazon%20Products%20Reviews%20Classification/Images/ama3.png)
***********************************************************
## Overall Model Comparison
We have developed five text vectorization models and two deep learning models, all total we have deployed seven machine learning + deep learning models. Now let's find out which one is the best among all these!

|Models|Accuracy Score|
|:-:|:-:|
|CountVectorizer + MultinomialNB|89.06|
|TfidfVectorizer + MultinomialNB|89.08|
|CountVectorizer + MultinomialNB w/o stopwords|87.63|
|TfidfVectorizer + MultinomialNB w/o stopwords|87.59|
|CountVectorizer + MultinomialNB lemmatized|88.48|
|LSTM Reccurent Neural Network|91.00|
|RoBERTa Model|96.50|

*********************************************

## Conclusion
* From all the deployed models it is clear that the **deep learning methods are having the upper hand over the Text Vectorization models in this case.**
* Text vectorization models have achieved the best score of **89.08**, which is scored by, **TfidfVectorizer + MultinomialNB** model.
* Deep learning models are having the higher accuracy than the vectorizations, as **RoBERTa architecture** is the best among them with **96.50** accuracy score.
* **RoBERTa is the best model for this classification model for the Amazon Products Reviews Classification.**

**************************************************
## Author
Code Contributed by, **Abhishek Sharma, 2021** `@abhisheks008` *#LGMSOC21*
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
