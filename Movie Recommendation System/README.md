# Movie Recommendation System

This model will recommend movies with the help of movies_metadata dataset from kaggle.

**About Dataset**

movies_metadata.csv: The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset. 
Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.

*DataColumns in Dataset*

- adult	
- belongs_to_collection	
- budget	
- genres	
- homepage	
- id	
- imdb_id	
- original_language	
- original_title	
- overview	...	
- release_date	
- revenue	
- runtime	
- spoken_languages	
- status	
- tagline	
- title	
- video	
- vote_average	
- vote_count


**Techniques Used**

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
  
  
With the help of TFIDF and cosine similarity we get better recommendations.
  
  
