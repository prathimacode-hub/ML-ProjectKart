**PROJECT TITLE - Fake News Detection**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/project_viz1.png" width="400">

**GOAL** - The aim of the project is to detect whether the news is Real or Fake using different text extraction NLP techniques to understand the data, use different classifiers approaches and RNN framework on this training data to train various models and use them to make detections.   

**WHAT HAVE I DONE**
- Loading datasets
- Handling null values
- Concatinating all the text for more generalisation of the model and increases reliability
- Using NLP approaches like Count Vectorizer and Tf-IDF Vectorizer to do proper data extraction
- Training a Logistic Regression model using Count Vectorizer
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/LG_countvec.png" width="300">

- Training a Logistic Regression model using Tf-IDF Vectorizer
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/LG_tfidf_vec.png" width="300">

- Training a Multinomial Naive Bayes model using Count Vectorizer
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/multinomialNB_countvec.png" width="300">

- Training a Multinomial Naive Bayes model using Tf-IDF Vectorizer
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/multinomialNB_tfidf_vec.png" width="300">

- Training a Passive Agressive Classifier model using count Vectorizer
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/PAclassifier_countvec.png" width="300">

- Training a Passive Agressive Classifier model using Tf-IDF Vectorizer
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/PAclassifier_tfidf_vec.png" width="300">

- Training a LTSM Network model
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/ltsm_traintest_loss.png" width="300">

- Performing the data preprocessing steps again to apply the RNN approach
- Making visualizations of differnent columns and dropping the noisy data
- Applying NLP to create Wordcloud of teh most used words in Real and Fake news
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/real_news_wordcloud.png" width="300">
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/fake_news_wordcloud.png" width="300">


- Splitting data and creating the model layers
- Making predictions on test data and saving the detections in a specific dataframe


**MODELS USED**
- Logistic Regression
- Multinomial Naive Bayes
- Passive Agressive Classifier
- LTSM Networks
- RNN framework

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- seaborn
- nltk
- re
- wordcloud
- tensorflow
- keras
- scikit Learn
- itertools
- tqdm

**Data Visualizations**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Fake%20News%20Detection/Images/news_outliers.png" width="300">

**Conclusion**

In this project we have performed a comparative analysis of different classifiers and neural network models merged with various text extraction approches of NLP to read and understand the degree of realness in the news and then classify them into binary classes: real and fake.
The RNN model gives 99% accuracy and proves to be the most effective among all of the trained models.

