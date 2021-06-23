# Plant Seedlings Classification
Agriculture is very important to human continued existence and remains a key driver of many economies worldwide, especially in underdeveloped and developing economies. There is an increasing demand for food and cash crops, due to the increasing in world population and the challenges enforced by climate modifications, there is an urgent need to increase plant production while reducing costs. Preceding instrument vision methods established for selective weeding have confronted with major challenges for trustworthy and precise weed recognition. In this project, plant seedlings classification approach is presented with a dataset that contains approximately 5,000 images with 960 unique plants that belong to 12 species at a few developing phases. Convolutional Neural Network (CNN) algorithms, a deep learning technique extensively applied to image recognition was used, for this task. The results found that CNN-driven seedling classification applications when used in farming automation have the latent to enhance crop harvest and improve output and productivity when designed properly. The trained model achieved an accuracy of 99.48% on a held-out test set, demonstrating the feasibility of this approach.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-15/Plant%20Seedlings%20Classification/Images/plant1.jpg)

## Goal
The goal of this project is to build the classification model. The architectures that I have used are, ResNet, AlexNet, Vgg, Inception, MobileNet, SqueezeNet, DenseNet, to deploy the classification model.

## Dataset
The dataset which is used in this project, is collected from Kaggle. Here is the link of the dataset : https://www.kaggle.com/vbookshelf/v2-plant-seedlings-dataset

## What Have I done
1. Loading and importing all the libraries, check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-15/Plant%20Seedlings%20Classification/requirements.txt).
2. Importing the dataset in the Jupyter Notebook.
3. Then I prepared the Classification model using the Neural Networks.
4. These are following steps - 
    - Classification Algorithms using Neural Networks
        - Setting the model architecture
        - Evaluating the deployment of the architectures
        - Getting prediction on validation set
        - Creating Confusion Matrix
        - Plotting the Loss and Accuracy on the Training and Validation set
5. Conclusion

## Libraries used
|Numpy|Pandas|Matplotlib|Tensorflow|Keras|copy|date|time|shutils|torch|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

## Model Accuracy Visualization

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-15/Plant%20Seedlings%20Classification/Images/plant2.png)

## Model Comparison
I have deployed seven Convolution Neural Network architectures for this Plant Seedlings Classification project. The model is successfully deployed and the accuracy of the model is checked using the accuracy score. CNN is one of the finest neural networks and the architectures are grading up the model to the higher extent.

After evaluating the architectures, the accuracy score of the architectures are shown below -

|Name of the Architecture|Best Accuracy Score|
|:---:|:---:|
|ResNet|0.69|
|AlexNet|0.69|
|MobileNet|0.67|
|vgg|0.68|
|DenseNet|0.67|
|SqueezeNet|0.67|
|Inception|0.68|

## Conclusion
**Comparing all those scores scored by the deep learning algorithms, it is clear that ResNet and AlexNet architecture is having the upper hand in case of this dataset, than rest of the architectures of CNN.**

Best Fitted Models ranking - 
1. ResNet
2. AlexNet
3. Inception
4. VGG
5. MobileNet
6. DenseNet
7. SqueezeNet

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
