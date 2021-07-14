# CAPTCHA Decoding
A CAPTCHA (acronym for "Completely Automated Public Turing test to tell Computers
and Humans Apart") is a type of challenge-response test used to determine whether or not a
user providing the response is human. In this project, we used a deep neural network
framework for CAPTCHA recognition. The core idea of the project is to learn a model that
breaks image-based CAPTCHAs. We used convolutional neural networks and recurrent neural
networks instead of the conventional methods of CAPTCHA breaking based on segmenting and
recognizing a CAPTCHA. Our models consist of two convolutional layers to learn image
features and a recurrent layer to output character sequence. We tried different configurations,
including wide and narrow layers and deep and shallow networks. We synthetically generated a
CAPTCHA dataset of varying complexity and used different libraries to avoid overfitting on one
library. We trained on both fixed-and variable-length CAPTCHAs and were able to get accuracy
levels of 99.8% and 80%, respectively. 
 
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/fournierp/captcha-version-2-images. The dataset contains CAPTCHA images. The images are **5 letter** words, and have noise applied (blur and a line). They are of size **200 x 50**. The file name is same as the image letters.

## Goal
The goal of this project is to create a deep learning model which will recognize the captcha letters.

## Approach
My approach is to train a **CNN** model for every letter that occurs in the **CAPTCHA** and use this model for evaluation. We will remove all noises (ie. smooth out the images and remove that lines) and then separate out each of the 5 letters in the image and feed each one to the model independently.
**************************************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Processing
4. Data Wrangling
5. Model Creation using CNN
6. Checking accuracy
7. Predictions
8. Error Analysis
9. Conclusion

***********************************************
## Libraries used
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Sklearn
- Tensorflow
- Keras
- glob
***********************************************
## Data Visualization
- **Plotting some CAPTCHAs**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap2.png)

- **Label Distribution in CAPTCHAs**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap3..png)

- **Label distribution in test set**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap4.png)
********************************************
## Model Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap5.png)
******************************************
## Recognitions 
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap6.png) ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap7.png)
*******************************************
## Error Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap8.png) ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-51/CAPTCHA%20Decoding/Images/cap9.png)
*******************************************
## Conclusion
* Convolution Neural Network provides the luxury of detecting the images in a single model frame work.
* Here we have deployed the CNN model successfully, and it is working perfectly, recognizing the CAPTCHAs correctly.
* The model is having the accuracy of 0.88, macro average of 0.89 and weighted average of 0.88.
* Using the Convolution Neural Network along with the SMOTE and ReduceLROnPlateau makes the model more accurate than the baseline model.
* For me, it would be the best model to identify the CAPTCHA images and recognize them easily!
* ***Convolution Neural Network with SMOTE and ReduceLROnPlateau*** is the best model to be fitted.
**************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
