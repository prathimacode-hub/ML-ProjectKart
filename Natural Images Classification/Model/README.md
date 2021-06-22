# Natural Images Classification
Image Classification is a fundamental task that attempts to comprehend an entire image as a whole. The goal is to classify the image by assigning it to a specific label. Typically, Image Classification refers to images in which only one object appears and is analyzed. In contrast, object detection involves both classification and localization tasks, and is used to analyze more realistic cases in which multiple objects may exist in an image. Deep learning is a vast field so we’ll narrow our focus a bit and take up the challenge of solving an Image Classification project. Additionally, we’ll be using a very simple deep learning architecture to achieve a pretty impressive accuracy score. For deploying and developing the Classification Model based on the Image Classification Dataset, I am going to use two Neural Network Algorithms. They are -
- Artificial Neural Network (ANN)
- Convolution Neural Network (CNN)

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-10/Natural%20Images%20Classification/Images/im1.gif)

## Goal
The goal of this project is to build the Classification Model using the Neural Networks and Deep Learning.

## Dataset
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/prasunroy/natural-images

## What Have I Done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-10/Natural%20Images%20Classification/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. Then I prepared the Classification Algorithms using the Neural Networks.
4. Two model are being prepared.
    - Artificial Neural Network.
        - Label Encoder applied.
        - Spliting the data at 70:30 ratio.
        - Fitting the model.
        - Checking the accuracy.
        - Confusion Matrix to recheck the low accuracy factor for ANN.
    - Convolution Neural Network (CNN).
        - Label Encoder applied.
        - Spliting the data at 70:30 ratio.
        - Fitting the model.
        - Checking the accuracy.
5. Model Comparison and Conclusion.

## Model Visualization
- Model developed using ANN :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-10/Natural%20Images%20Classification/Images/model1.png)

- Model developed using CNN :

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-10/Natural%20Images%20Classification/Images/model2.png)

## Model Comparison
We have deployed two neural network based deep learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Artificial Neural Network (ANN)|0.73|
|Convolution Neural Network (CNN)|0.85|


## Conclusion
**Comparing all those scores scored by the deep learning algorithms, it is clear that Convolution Neural Network (CNN) is having the upper hand in case of this dataset, than Artificial Neural Network (ANN).**

Best Fitted Models ranking - 
1. Convolution Neural Network (CNN)
2. Artificial Neural Network (ANN)

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
