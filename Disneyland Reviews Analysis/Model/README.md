**PROJECT TITLE - Disneyland Reviews Analysis**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/project_viz.png" width="400">

**GOAL** - The aim of this project is to analyse the reviews given by visitors from different countries of the world using NLP to understand the sentiment of the reviews and classify using Sentiment Analysis metrics like Sentiment Polarity and VADER Polarity. This processed data is then feeded to different classifier models to get trained and predict the sentiment of the test reviews.

**WHAT HAVE I DONE**

- Loading datasets
- Dealing with Null Values
- Preprocessing the 'Review_ID ' column
- Removing duplicate labels
- Preperocessing the 'Year_Month' column
- Visualization of the 'Year' column
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/year_plot1.png" width="300">

- Visualization of the 'Month' column
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/month_plot1.png" width="300">

- Preprocessing the 'Reviewer_Location' column
- Visualization on the 'Reviewer_Location' column
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/country_visitors.png" width="300">

- Preprocessing 'Review_Text' column and extracting the useful words
- Preprocessing the 'Branch' column
- Visualization of the labels in the 'Branch' column
- <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/branch_piechart.png" width="300">

- Performing One Hot Encoding on the 'Branches' column
- Visualization and data analysis of the 'Rating' column
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/ratings_piechart.png" width="300">

- Creating WordCloud of Rating = 1
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_rating1.png" width="300">

- Creating WordCloud of Rating = 2
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_rating2.png" width="300">

- Creating WordCloud of Rating = 3
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_rating3.png" width="300">

- Creating WordCloud of Rating = 4
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_rating4.png" width="300">

- Creating WordCloud of Rating = 5
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_rating5.png" width="300">

- Visualization of Rating with respect to different Branches of Disneyland
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/branch_locations_piechart.png" width="300">

- Creating WordCloud of 'California' Branch
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_california.png" width="300">

- Creating WordCloud of 'HongKong' Branch
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_hongkong.png" width="300">


- Creating WordCloud of 'Paris' Branch
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_paris.png" width="300">

- Visualization of the Correlation between different Branches and Reviewers Location
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/correlations.png" width="300">

- Creating WordCloud of Positive Sentiments
 <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_positive.png" width="300">
 
 - Creating WordCloud of Nagetive Sentiments
 <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_nagetive.png" width="300">
 
 - Creating WordCloud of Neutral Sentiments
 <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/wordcloud_intermediate.png" width="300">
 
 - Finding the Sentiment Polarity of the reviews
 <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/Spolarity_piechart.png" width="300">
 
 - Performing Lexicon based approach of Sentiment Analysis using the VADER Polarity
 <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Disneyland%20Reviews%20Analysis/Images/Vpolarity_piechart.png" width="300">

- Performing Label Encoding on 'Reviewer Location' , 'Year', 'S_Polarity' and 'V_Polarity' columns
- Converting the data of 'Month' column into numeric type
- Review Analysis on the basis of Sentiment Polarity
- Splitting the data
- Using Tf-IDF Vectorizer
- Using Decision Tree classifier
- Using Random Forest classifier
- Using XGBoost classifier
- Performing all these Analyis steps again with VADER Polarity



**MODELS USED**


- XGBoost - *Extreme Gradient Boost alsorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*



**LIBRARIES NEEDED**

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- nltk
- wordcloud
- PIL
- string
- re
- scikit learn
- xgboost


**Conclusion**

After performing the comparative analysis of different classfier models(Decision Tree,Random Forest, XGBoost), we can conclude that :-

-  VADER Polarity is a better metric than Sentiment Polarity to analyse the sentiment of the extracted review texts
-  XGBoost perfroms better than the other 2 models both when Sentiment Polarity and VADER Polarity is feeded. However it gives a better Train Accuracy(100%) and Test Accuracy(93%) when trained with VADER polarity  
