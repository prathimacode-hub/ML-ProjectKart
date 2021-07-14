# Balls Image Classification
In recent years sport video research has gained a steady interest among the scientific community. The large amount of video data available from broadcast transmissions and from dedicated camera setups, and the need of extracting meaningful information from data, pose significant research challenges. Hence, computer vision and machine learning are essential for enabling automated or semi-automated processing of big data in sports. Although sports are diverse enough to present unique challenges on their own, most of them share the need to identify active entities such as ball or players. In this project, an innovative deep learning approach to the identification of the ball in tennis context is presented. The work exploits the potential of a convolutional neural network classifier to decide whether a ball is being observed in a single frame, overcoming the typical issues that can occur dealing with classical approaches on long video sequences (e.g. illumination changes and flickering issues). Experiments on real data confirm the validity of the proposed approach that achieves 95% accuracy and suggest its implementation and integration at a larger scale in more complex vision systems.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-47/Balls%20Image%20Classification/Images/ball1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/gpiosenka/balls-image-classification.

## Goal
The goal of this project is to make a deep learning model which will classify the images of different types of balls using the convoolution neural network, to be precise the MobileNet architecture.
******************************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-47/Balls%20Image%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Exploratory Data analysis and Data Visualization
4. Classification Model using Neural Networks
    * Define the model
    - Deploy the model
    - Classification report
5. Observation
6. Conclusion

**********************************************
## Libraries used
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Sklearn
- Tensorflow
- Keras
- glob

*******************************************
## Data Visualization
1. **Share the train, test and validation images**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-47/Balls%20Image%20Classification/Images/ball2.png)

2. **Plotting the types of balls v/s no. of the balls**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-47/Balls%20Image%20Classification/Images/ball3.png)

3. **Plotting different images**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-47/Balls%20Image%20Classification/Images/ball4.png)
***********************************************
## Model Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-47/Balls%20Image%20Classification/Images/ball5.png)
**********************************************

## Observation from the model
* The model deployed here is using the architecture called MobileNetV2.
* It is a neural network model architecture, mainly used for the images classification.
* The model shows a recall of 1.00
* The model shows f1 score of 1.00
* The model shows precision of 1.00
* Talking about the accuracy score, the model shows the accuracy of 0.95 or, 95%
* The model also shows the macro average of 0.95 and weighted average of 0.95.
*************************************
## Conclusion
* Images classification is one of the trending models in the recent times.
* Using of Convolution Neural Network for classifying the images, made the model to easlily deployable.
* The MobileNetV2 architecture has the special ability to classify the images from the dataset and predict the correct images.
* As the model provides an accuuracy score of 95%, for me it is the final model for this project
* Hence, **MobileNetV2 Architecture** is the best model for this dataset to deploy the classification model.
***********************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
