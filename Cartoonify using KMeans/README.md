
## Cartoonify using KMeans Algo :


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 
# Cartoonify_reality

Even the basics of image processing if done properly can be handy which otherwise would require a machine learning model.This project is one of such inspiration which **cartoonizes** images and videos using only core **opencv filters** and functions.It also uses K-means clustering algorithm to compress the image. This clustering gives it the basic cartoonish tinge it requires.

**Algorithm**- K_Means Clustering

Clustering is one of the most common exploratory data analysis technique used to get an intuition about the structure of the data. It can be defined as the task of identifying subgroups in the data such that data points in the same subgroup (cluster) are very similar while data points in different clusters are very different. In other words, we try to find homogeneous subgroups within the data such that data points in each cluster are as similar as possible according to a similarity measure such as euclidean-based distance or correlation-based distance. The decision of which similarity measure to use is application-specific.



## Kmeans Algorithm
Kmeans algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups (clusters) where each data point belongs to only one group. It tries to make the intra-cluster data points as similar as possible while also keeping the clusters as different (far) as possible. It assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s centroid (arithmetic mean of all the data points that belong to that cluster) is at the minimum. The less variation we have within clusters, the more homogeneous (similar) the data points are within the same cluster.


### The way kmeans algorithm works is as follows:
* Specify number of clusters K.
* Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.
* Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.
* Compute the sum of the squared distance between data points and all centroids.
* Assign each data point to the closest cluster (centroid).
* Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster.


**Filters**-Bialateral Filter, Contours, erode, Canny(edge detection)


### Prerequisites

What things you need to install the software and how to install them

```
scipy 
numpy 
cv2
```

## Getting Started
Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above. Run vid.py file to cartonify your webcamp feed. Uncomment the last 2 lines of cartoonize.py and run to cartoonify an image.

```
$vid.py     
                    
$cartoonize.py
```
## Original Image
![original2](https://user-images.githubusercontent.com/65017645/135580833-34790f46-6f76-4da0-a7be-a8dd9bc19215.jpg)


## Cartoon Output
![cartoon](https://user-images.githubusercontent.com/65017645/135580847-9688a647-711f-4e67-aa95-50aa7d528868.jpg)


## Built With
* [python](https://www.python.org/) - The software used

## Documentation
The entire documentation and explanation of code as well as concepts can be found in this article: https://iot4beginners.com/cartoonize-reality-with-opencv-and-raspberry-pi/
