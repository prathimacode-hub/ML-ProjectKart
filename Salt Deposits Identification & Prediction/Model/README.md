# Salt Deposits Identification & Prediction
Several areas of Earth with large accumulations of oil and gas also have huge deposits of salt below the surface.But unfortunately, knowing where large salt deposits are precisely is very difficult. Professional seismic imaging still requires expert human interpretation of salt bodies. This leads to very subjective, highly variable renderings. More alarmingly, it leads to potentially dangerous situations for oil and gas company drillers.


![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/20180124081226334imageedit_1_4880614023_main.jpg)

## Goal
The goal of this project is to make an identification model which will predict whether the input image is of salt or, not!

## Dataset
The dataset is collected from Kaggle website. Here is the link for the website : https://www.kaggle.com/c/tgs-salt-identification-challenge
***************************
## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Processing
4. Data Cleaning
5. Model Architectures
    - U-Net Architecture
    - ResNet 34 Architecture
6. Accuracy Checking
7. Inference
8. Predictions
9. Conclusion and Discussion

*******************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. Tensorflow Backend
7. Keras
8. six

*********************************
## Data Visualization and Optimization
**1. Some Example images**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/__results___16_1.png)

**2. Augmentation of the images**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/__results___33_1.png)

*************************************
## Model Visualization
**Training and Testing Loss**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/salt1.png)

**Prediction on Training Set**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/salt2.png)

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/salt3.png)

**Prediction on Test Set**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/salt4.png)

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-56/Salt%20Deposits%20Identification%20%26%20Prediction/Images/salt5.png)

*************************************
## Conclusion and Discussion
Here we have deployed two CNN architectures for predicting the Salt images and also the identification of the images and lastly, we have combined both the architectures U-Net and ResNet 34 to produce the final model. After thresolding procedure the model looks better than the previously deployed ones and providing the accuracy scores of more than 90% while identifying the images and more than 97% while predicting the images whether they are salt images or, not!

The identification model or, frame work provides the accuracy of 90%

The Prediction model provides the accuracy of 97%

From my side CNN is the best way to identify this kind of images and creating this kind of image classification models!
************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #DCP21

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
