**PROJECT TITLE - Prediction of Subject based on Question (NLP)**
        
<img src = https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/project_viz.png width = '300'>


**GOAL** - The aim of this project is to predict whether the subject is Physics, Chemistry, Biology or Maths by analysis of the questions coloumn using Natural Language Processing techniques.

**WHAT HAVE I DONE**
- Loading datasets
- Checking distinct values of the dataset
- Data Visualizations
- Data Cleaning
    - Removing the numeric values
    - Removing the spaces
    - Setting all words to Lower Case
    - Performing stemming
    - Tokenizing the text
    - Removing the stopwords¶
    - Performing lemmatization
- Frequency Distribution Plot
- Displaying Most common words
- WordCloud Vizualizations
- Saving the dataframe with Preprocessed Text to build the classification model
- Constructing Features using Vectorizers
- Comparative Model Analysis
- Logistic Regression
- K-Nearest Neighbour Algorithm
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost classifier
- Gausian Naive Bayes Classifier Algorithm
- Saving the Random Forest model
- Saving the predictions in a dataframe 



### WordCloud Visualizations

- **WordCloud of most common 100 words**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/Wordcloud100.png" width = "500">

- **WordCloud of most common 100 words**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/Wordcloud200.png" width = "500">

- **WordCloud of most common words used in Chemistry questions**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/Wordcloud_chemistry.png" width = "500">

- **WordCloud of most common words used in Physics questions**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/Wordcloud_physics.png" width = "500">

- **WordCloud of most common words used in Maths questions**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/Wordcloud_maths.png" width = "500">

- **WordCloud of most common words used in Biology questions**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/Wordcloud_biology.png" width = "500">


**MODELS USED**

- Logistic Regression
- K-Nearest Neighbour Algorithm
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost classifier
- Gausian Naive Bayes Classifier Algorithm

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/rf_classif.png" width = "300">

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- scipy
- seaborn
- scikit-learn
- pickle
- tensorflow


**Comparing the models**

- **Logistic Regressor model**
    - *Accuracy of Logistic regression on training set: 88%*
    - *Accuracy of Logistic regression on test set:  88%*

- **KNN Classifier model**
    - *Accuracy of KNeighbors Classifier on training set: 87%*
    - *Accuracy of KNeighbors Classifier on test set: 0.80%*

- **Decision Tree Classifier model**
    - *Accuracy of Decision Tree Classifier on training set: 98%*
    - *Accuracy of Decision Tree Classifier on test set: 81%* 

- **Random Forest Classifier model**
    - *Accuracy of Decision Tree Classifier on training set: 98%*
    - *Accuracy of Decision Tree Classifier on test set: 87%* 

- **XGBoost classifier model**
    - *Accuracy of Decision Tree Classifier on training set: 88%*
    - *Accuracy of Decision Tree Classifier on test set: 87%* 

- **Gausian Naive Bayes Classifier model**
    - *Accuracy of Decision Tree Classifier on training set: 77%*
    - *Accuracy of Decision Tree Classifier on test set: 76%* 






### From the model comparison it is evident that the Random Forest Classifier performs better than other models with a Training Accuracy of 98% and a testing accuracy of 87%.


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Prediction%20of%20Subject%20based%20on%20Question%20(NLP)/Images/predictions_count.png" width = "500">



**Conclusion**

In this project we have first processed the text data using the NLP techniques and then tried to visualize the most relavent words using various WordClouds. Once the preprocessing and the visualization is done we saved the processed text data, converted it into feature vectors to perform a comparative model analysis using different classifier models. After doing the result is that the Random Forest Classifier performs better than other models with a Training Accuracy of 98% and a testing accuracy of 87%. So we have saved this model and its predictions also.
