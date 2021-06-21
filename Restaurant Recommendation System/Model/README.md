# Restaurant Recommendation System ---- using the Yelp User Reviews Dataset
I wanted to build something that would be meaningful for people in their everyday lives. This ultimately led me to build a recommendation system model that could recommend people restaurants near their location based on restaurant reviews from other people, drawing on sentiment analysis that could potentially improve the recommendation suggestions that you see on common food delivery apps like Deliveroo, GrabFood, and FoodPanda.

![ScreenShot](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-4/Restaurant%20Recommendation%20System/Images/front.jpeg)

## Goal
The goal of this project is to make a Recommendation System which will recommend the users the best restaurant that they are looking for.

## Dataset
The dataset which is being used here is easily accesible at Kaggle. The link is given here, https://www.kaggle.com/yelp-dataset/yelp-dataset

## What Have I done
1. Loading the required libraries, check the `requirements.txt` folder for the libraries.
2. Processing and cleaning the data using the dummies from the attributes.
3. Classifying the data using K-Nearest Neighbouring.
4. Model Filtering using Collaborative model filtering
  - Firstly, impose the SVD or, Simple Value Decomposition
    - Building the Utility Matrix
    - Transposing the matrix
    - Decomposing the matrix
    - Generating the co-relation matrix
    - Isolating most popular restaurants from the matrix
    - recommend the highly correlated restaurants
5. Neural Networks
  - Here, I have chosen to use the Keras 
    - Prediction
    - Cosine similarity
    - Recommendation

## Algorithms and Models used
1. For the filtering procedure I have used the K-Nearest Neighbouring algorithm.
2. Then for collaborative filtering, Singular Value Decomposition or, SVD.
3. For final prediction, Keras.
4. Prediction accuracy metrices, Cosine similarity.

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Keras
5. KNN
6. sklearn
7. Tensorflow

## Model output
![ScreenShot](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-4/Restaurant%20Recommendation%20System/Images/rating.png)

## Conclusion
Using the user reviews dataset this recommendation model is built and being successfully deployed using the proper libraries. The accuracy has been checked using the Cosine accuracy score and it turned out to be well enough to be a recommendation system. Hence, from all those factors we can conclude that the model is deployed successfully.

*****************************************************************************

### Author 
Code contributed by, Abhishek Sharma, 2021, @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
