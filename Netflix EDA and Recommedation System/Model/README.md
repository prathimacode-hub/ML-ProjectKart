# Netflix EDA and Recommendation System

**GOAL**: The project aims to gain insights from detailed EDA and recommend which movie to watch next.

**DATASET** : The dataset used in this project can be downloaded from [here](https://www.kaggle.com/shivamb/netflix-shows)

**LIBRARIES NEEDED** : 

- Pandas
- Numpy
- Matplotlib
- Seaborn
- missingno
- sklearn


**WHAT I HAD DONE**:

--> EXPLORATORY DATA ANALYSIS
- I explored the dataset and handeled missing values in suitable manner.
- Cleaned and manipulated the data to perform Exploratory data analysis.
- Created data visualisations to understand the data in most simplified way.
- Computed Detailed analysis in different features of data and gained insights from it.
- Asked right questions and got answers to them which can be helpful in practical applications.

--> RECOMMENDATION SYSTEM
     I have used "Content based recommendation system" for this project purpose.

- Simple plot(description) based Recommendation System
  
  - It recommends the top contents based on TF-IDF matrix based cosine similarity score.
  - After calculating the weighted score for every movie, based on score it recommends the movies. This Simple Recommendation system gives good results but to improve the 
  recommendation we need to build something more better.
  
- Multiple metrics(Genre,cast,director) based Recommendation System
 
  - It will compute the cosine similarity scores for all movies based on the features in our dataset.
  - I cleaned the data first and used CountVectorizer() and computed cosine similarity score.
  - This improved Model gives better recommendations and can be considered.
  
  
**Conclusion** :
- Detailed Exploratory Data analysis helps to gain useful insights from the data.
- Insights can help to take better decisions for the organization profit.
- Analysis shows users watching patterns,content type,trends in durations over the time.
- Multiple metrics based Recommendation system works better for this dataset.
