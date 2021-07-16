
## Intro to face Recognition

A facial recognition system is a technology capable of matching a human face from a digital image or a video frame against a database of faces, typically employed to authenticate users through ID verification services, works by pinpointing and measuring facial features from a given image.



Faces recognition example using eigenfaces and SVMs
Our discussion of PCA spent a lot of time on theoretical issues, so in this mini-project we’ll ask you to play around with some sklearn code. The eigenfaces code is interesting and rich enough to serve as the testbed for this entire mini-project.

## Models used 
Principal Component Analysis, or PCA, is a dimensionality-reduction method that is often used to reduce the dimensionality of large data sets, by transforming a large set of variables into a smaller one that still contains most of the information in the large set.






### Install

This project requires **Python 3.6** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

### Run

In a terminal or command window, navigate to the top-level project directory (that contains this README) and run one of the following commands:

```bash
Model.ipynb
```

### Dataset

The dataset used in this example is a preprocessed excerpt of the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/)

## Principal component analysis (PCA)

Principal component analysis (PCA) is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables (entities each of which takes on various numerical values) into a set of values of linearly uncorrelated variables called principal components. If there are n observations withp variables, then the number of distinct principal components is min ( n − 1 , p ).

PCA is many advantages when applied to ML algorihtms:

* Dimensionality reduction
* Feature transformation
* Data visualisation
* Speeds up the machine learning algorithms

### How does PCA work?

PCA transforms the data into a new coordinate system such that the greatest variance by some projection of the data comes to lie on the first coordinate(called the principal component), the second greatest varaince on the second coordinate, and so on.

<img src="https://github.com/shashank136/Face-detection-using-PCA/blob/master/pca.png" width="350" title="hover text">

The idea is to increase the variance and decrease the total sum of distance of each points from the PC. In above figure the PC1 has maximum variance and minimum total distance sum compared to PC2.

#### Results for face recognition

![png](https://github.com/shashank136/Face-detection-using-PCA/blob/master/result.png)
