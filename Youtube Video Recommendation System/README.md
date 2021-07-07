# Youtube Video Recommendation System

**GOAL**: This model will recommend the video titles on proving the search query by user.

**DATASET** : https://github.com/prathimacode-hub/ML-ProjectKart/tree/main/Youtube%20Video%20Recommendation%20System/Dataset

**LIBRARIES NEEDED** : 

- Pandas
- Numpy
- Sklearn
- NLTK

**WHAT I HAD DONE**:

I have used two techniques to recommend video titles

- Simple Recommendation System(K-nearest neighbours)
  
  It will recommend the top videos using concept of K-nearest neighbours. Simple Recommendation system gives good results but to improve the 
  recommendation we need to build something more better.
  
- Content Based Recommendation System(Tf-idf Vectorizer)
 
  It will compute the cosine similarity scores for all videos titles words based on the titles and descriptions in our dataset.
  Here, We will compute Term Frequency-Inverse Document Frequency (TF-IDF) vectors for each text(titles + description). 
  This will give us a matrix where each column represents a word from the text and each row represents a title.
  It will also recommend top 10 matching video titles based on user query.
  
  
**Conclusion** : TFIDF Vectorizer gives better recommendations than KNN.
  
  
