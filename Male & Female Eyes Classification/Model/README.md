# Male & Female Eyes Classification
Studies have revealed superior face recognition skills in females, partially due to their different eye movement strategies when encoding faces. In the current project, we utilized these slight but important differences and proposed a model that estimates the gender of the viewers and classifies them into two subgroups, males and females. An eye tracker recorded participant’s eye movements while they viewed images of faces. Regions of interest (ROIs) were defined for each face. Results showed that the gender dissimilarity in eye movements was not due to differences in frequency of fixations in the ROI s per se. Instead, it was caused by dissimilarity in saccade paths between the ROIs. The difference enhanced when saccades were towards the eyes. Females showed significant increase in transitions from other ROI s to the eyes. Consequently, the extraction of temporal transient information of saccade paths through a transition probability matrix, similar to a first order Markov chain model, significantly improved the accuracy of the gender classification results.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/pavelbiz/eyes-rtte.

## Goal
The goal of this project is to create a classification model which will classify the genders based on the eyes images as per given in the dataset. For this we are going to use different architectures of Convolution Neural Network.
********************************

## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Organising Training and testing data
4. Data Distribution
5. Plotting various images
6. Label encoder
7. Neural Network models
    - ConvNet
    - Inception
    - Xception
    - MobileNet
8. Model Comparison
9. Predictions
10. Conclusion

********************************************
## Libraries used
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Sklearn
- Tensorflow
- Keras
- glob

***********************************
## Data Distribution
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye2.png)

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye3.png)
************************************
## Model Visualization [ConvNetV2 Architecture]
1. **Accuracy and Loss**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye4.png) ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye5.png)

2. **Confusion Matrix**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye6.png)
**************************************
## Model Comaprison
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye7.png) ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye8.png)

Here we have deployed four architectures of Convolution Neural Network, now let's find out the accuracy checking metrices and their respective scores.

|Model|	Test accuracy (%)|	Recall (%)|	Precision (%)|	F1 (%)|	AUC|
|-|-|-|-|-|-|
|ConvNet	|0.925399	|0.973651	|0.899710	|0.935221|	0.919667|
|Inception|	0.855309	|0.874529	|0.865301|	0.869891|	0.853026|
|Xception|	0.868494|	0.942911|	0.839196|	0.888035|	0.859654|
|MobileNet|	0.860167|	0.896487|	0.857229|	0.876418|	0.855852|
***************************************
## Predictions
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-48/Male%20%26%20Female%20Eyes%20Classification/Images/eye9.png)
**************************************
## Conclusion
* Images classification is one of the hot topics in today's world.
* Usage of Concolution Neural Network in this type of classification works makes the developer easier to develope models using the architectures.
* Here we have used four different types of architecture, such as, MobileNet, ConvNet, Inception and Xception.
* Among all these deployed models, **ConvNet Architecture** is having the upper hand over all of the rest of the models.
* ***ConvNet Architecture*** is having the accuracy of 0.93, with a F1-score of 0.94 and AUROC value of 0.92, which shows how much the architecture is capable of building the model.
* Hence, **ConvNet is the best fitted Convolution Neural Network architecture used here and deployed successfully!**
***************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
