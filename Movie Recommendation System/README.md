# Movie Recommendation System

**GOAL**: This model will recommend the movies , provided the movies name.

**DATASET** : https://www.kaggle.com/rounakbanik/the-movies-dataset/code

**LIBRARIES NEEDED** : 

- Pandas
- Numpy
- Seaborn
- sklearn

**WHAT I HAD DONE**:

I have used two techniques to recommend movies

- Simple Recommendation System
  
  It will recommend the top items based on a certain metric score.
  
  After calculating the weighted score for every movie , we can sort the movies based on the score. Simple Recommendation system gives good results but to improve the 
  recommendation we need to build something more better.
  
- Content Based Movies Recommendation System
 
  It will compute the cosine similarity scores for all movies based on the overview feature in our metadata dataset.
  Here, We will compute Term Frequency-Inverse Document Frequency (TF-IDF) vectors for each document(overview rows). 
  This will give us a matrix where each column represents a word in the overview vocabulary (all the words that appear in at least one document), 
  and each row represents a movie.
  
  
**Conclusion** : With the help of TFIDF and cosine similarity we get better recommendations.
  
  
