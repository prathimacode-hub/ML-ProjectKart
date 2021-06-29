# Dandelion Recognition
These are images of dandelions and not-dandelions. Basically grass or other. Goal of this project/images is a very simple binary image classification model for me to do some "real world learning": - Dandelions - Anything NOT dandelions :) Initial thoughts and findings: Need lots and lots more images. While the training results in decent accuracy, the validation loss is substantial. My initial 1,200+ images (50% dandelion/50% not) seems woefully small. May need upwards of 10,000+ of each….maybe. Initially the focus was not on dandelions that have already flowered, but more on just the leaves being the more prominent feature. Next spring/summer, I'll need to diversify the dandelions. I had initially started with 'Square' images to keep it uniform. However, with help from the 'kids,' in the neighborhood I ended up allowing all sizes and shapes. Seems that to get well over 10,000 of each, that's a restriction I'll have to work through.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/Images/dand7.jpg)

## Goal
The goal of this project is to create classification model which will identify the dandelion from the images given to the model. It's basically going to be a recognition model.

## Dataset
The dataset is collected from the Kaggle website. Here is the link for the website : https://www.kaggle.com/coloradokb/dandelionimages

## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Visualization
4. Implementing CNN
5. Checking the accuracy
6. Predictions on the images
7. Confusion Matrix
8. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Seaborn
5. Sklearn
6. Tensorflow
7. Keras
8. os
9. date

## Data Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/Images/dand1.png)

### Various Images from the dataset
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/Images/dand2.png)
******************************************************

## Model Accuracy
1. **Checking the accuracy of the model**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/Images/dand3.png)

2. **Confusion Matrix**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/Images/dand4.png)

3. **Predicting to the Images**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-30/Dandelion%20Recognition/Images/dand5.png)

## Conclusion
Here I have used Tensorflow backend and CNN for creating the model and the model is well fitted and well trained also the model is providing correct predictions as it recognises the images correctly during the testing of the model. The model is having the higher accuracy of 82.68% and the validation loss is under 0.50 which shows that the model is really well trained and well fitted.

|Model|Accuracy Score|
|:---:|:---:|
|Convolution Neural Network|82.68|

For this Dandelion Recognition the Convolution Neural Network is the best fitted model from my classification techniques, also the model can be trained with RNN, but in the case of RNN, it will be overfitted, means the model will be well trained on the training set but will not be predicted accurately on the testing set. So, to overcome that situation CNN is the best model for this dataset.

*******************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
