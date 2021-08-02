
#  IMDB Sentiment Analysis
![](https://cfml.se/img/blog/sentiment_classification/top_img.png)

**GOAL** 
- The main purpose of this project is to predict the sentiment of movie reviews on IMDB.

**DATASET**
- The data used in this project can be downloaded from [here](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

**WHAT I HAD DONE**
- Performed Exploratory Data Analysis on text data.
- Generated various wordclouds to know data better.
- Performed Text cleaning on the reviews text data.
- Removed stopwords, HTML strips and tags and noise from data.
- Built multiple models like LSTM, BERT, LinearSVC and compared them to get best results.


**MODELS USED**


| Model | Train Score | Test Score |
| :---: | :---: | :---: |
| LSTM | 0.9319 | 0.8766 |
| BERT | 0.9750 | 0.9045 |
| LinearSVC | 0.9884 | 0.8952 |

## Wordclouds from movie reviews :

### Positive Reviews
![](https://github.com/shivani6320/ML-ProjectKart/blob/sentiment_analysis/IMDB%20Sentiment%20Analysis/Images/positive.png?raw=true)

### Negative Reviews
![](https://github.com/shivani6320/ML-ProjectKart/blob/sentiment_analysis/IMDB%20Sentiment%20Analysis/Images/negative.png?raw=true)


**LIBRARIES NEEDED**
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- Tensorflow
- Keras
- re
- NLTK

**CONCLUSION**
- Text cleaning performs major role in improvinh model performance to get better results.
- After comparing multiple models, **BERT** Model gives the best performance with 90% test accuracy.


