# Crop Recommendation System
Data mining is the practice of examining and deriving purposeful information from the data. Data mining finds its application in various fields like finance, retail, medicine, agriculture etc. Data mining in agriculture is used for analyzing the various biotic and abiotic factors. Agriculture in India plays a predominant role in economy and employment. The common problem existing among the Indian farmers are they don't choose the right crop based on their soil requirements. Due to this they face a serious setback in productivity. This problem of the farmers has been addressed through precision agriculture. Precision agriculture is a modern farming technique that uses research data of soil characteristics, soil types, crop yield data collection and suggests the farmers the right crop based on their site-specific parameters. This reduces the wrong choice on a crop and increase in productivity. In this paper, this problem is solved by proposing a recommendation system through an ensemble model with majority voting technique using Random tree, CHAID, K-Nearest Neighbor and Naive Bayes as learners to recommend a crop for the site specific parameters with high accuracy and efficiency.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-12/Crop%20Recommendation%20System/Images/crop1.jpg)

## Goal
The Goal of this project is to build the recommendation model using the crop recommendation dataset.

## Dataset
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/atharvaingle/crop-recommendation-dataset. Also, I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-12/Crop%20Recommendation%20System/Dataset) folder, you can access the dataset from there.

## What have I done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-12/Crop%20Recommendation%20System/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. After that I have divided the project in two halves -
	- Part A :: Exploratory Data Analysis
		- Visualizing the Ratio of Nitrogen and Phosphorous in the soil
		- Visualizing the Ratio of Potassium and Temperature in the soil
		- Visualizing the Humidity and pH in the soil
		- Visualizing the Rainfall
		- Introducing Label Encoder
	- Part B :: Prediction Models
		- Training and Testing Dataset Spliting using the train_test_split
		- K-Nearest Neighbour Algorithm
   		- Decision Tree Classifier
		- Random Forest Classifier
		- Gausian NB Algorithm
		- Logistic Regression
		- Support Vector Machine
		- Artificial Neural Network
4. Conclusion


## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. sklearn
5. seaborn

## Visualization
- Visualizing the Ratio of Nitrogen and Phosphorous in the soil
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-12/Crop%20Recommendation%20System/Images/crop2.png)

- Visualizing the Ratio of Potassium and Temperature in the soil
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-12/Crop%20Recommendation%20System/Images/crop3.png)


- Visualizing the Humidity and pH in the soil
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-12/Crop%20Recommendation%20System/Images/crop4.png)

- Visualizing the Rainfall

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-12/Crop%20Recommendation%20System/Images/crop5.png)

## Model Comparison
We have deployed seven machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|97.5|
|Decision Tree Classifier|98.6|
|Random Forest Classifier|99.3|
|Naive Bayes Algorithm|99.5|
|KNN Algorithm|97.0|
|Support Vector Machine Algorithm|96.1|
|Artificial Neural Network|95.2|

## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Naive Bayes Algorithm is having the upper hand in case of this dataset and after this, we can use Logistic Regression, Random Forest Classifier, SVM, which are also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Gausian Naive Bayes
2. Random Forest Classifier
3. Decision Tree Classifier
4. Logistic Regression
5. K-Nearest Neighbours
6. Support Vector Machine
7. Artificial Neural Network


Hooray!! The models are deployed successfully!
 
********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
