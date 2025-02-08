
## Next Word Prediction:


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.9](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-390/) 
# Movie Recommendation System
Recommendation systems are one of the most essential applications of Machine Learning in today's times. With the ability to recommend suggestions to the user based on past activity helps to retain the user's attention and helps increase user engagement. This project **recommends** movies to the user based on factors such as the **ratings** it has received, the **genre** of the movie, certain **tags** or **keywords** related to a movie, etc. It uses the K Nearest Neighbors algorithm to generate the recommendations.  


**Algorithm**- KNN Clustering

Clustering is one of the most common EDA techniques, which is used to get an idea about the structuring of the data. It is defined as the process of identifying subgroups or clusters in the data, such that data points in the same cluster show similarities to each other, while data points in different clusters are highly dissimilar. In essence, we try to find subgroups within the data so that data points in each cluster are as similar as possible according to a given similarity measure.


## KNN Algorithm
The KNN algorithm is a **non-parametric algorithm** (it does not make any assumptions about the underlying data) which **stores** all the available data and then classifies a new data point based on its **similarity** with the other points in the dataset. This means when new data appears then it can be easily classified into a well suite category by using KNN algorithm.
It is also called a **lazy learner** algorithm because it does not learn anything from the training set immediately. Instead, it stores the dataset. At the time of classification, it performs an action on the dataset.


### The way KNN algorithm works is as follows:
* Specify number of closest points K.
* Compute the cosine similarity between 2 non-zero vectors of an inner product space which measures the cosine of the angle between them
* Choose K highest similarities
* Find the majority category based on the k entries obtained above. 


### Prerequisites

What things you need to install the software and how to install them

```
re
SequenceMatcher from difflib
numpy
pandas
matplotlib.pyplot
csr_matrix from scipy.sparse
NearestNeighbors from sklearn.neighbors
```

## Getting Started
Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above. Run vid.py file to cartonify your webcamp feed. Uncomment the last 2 lines of cartoonize.py and run to cartoonify an image.

```
## Built With
* [python](https://www.python.org/) - The software used