# Shoulder X-ray Classification
Total Shoulder Arthroplasty (TSA) is a type of surgery in which the damaged ball of the shoulder is replaced with a prosthesis. Many years later, this prosthesis may be in need of servicing or replacement. In some situations, such as when the patient has changed his country of residence, the model and the manufacturer of the prosthesis may be unknown to the patient and primary doctor. Correct identification of the implant’s model prior to surgery is required for selecting the correct equipment and procedure. We present a novel way to automatically classify shoulder implants in X-ray images. We employ deep learning models and compare their performance to alternative classifiers, such as random forests and gradient boosting. We find that deep convolutional neural networks outperform other classifiers significantly if and only if out-of-domain data such as ImageNet is used to pre-train the models. In a data set containing X-ray images of shoulder implants from 4 manufacturers and 16 different models, deep learning is able to identify the correct manufacturer with an accuracy of approximately 80% in 10-fold cross validation, while other classifiers achieve an accuracy of 56% or less. We believe that this approach will be a useful tool in clinical practice, and is likely applicable to other kinds of prostheses.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-52/Shoulder%20X-ray%20Classification/Images/xray1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/dryari5/shoulder-xray-classification.

## Goal
The goal of this project is to create a classification model which will classify different images of shoulder x-ray and predict or, detect the type of the image!
************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-52/Shoulder%20X-ray%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Visualization
4. Data Cleaning
5. EfficientNet Model Deployment
6. Evaluate the model
7. Make Predictions
8. Conclusion
*****************************
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
## Data Visualization
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-52/Shoulder%20X-ray%20Classification/Images/xray2.png)
*************************************
## Model Visualization
- **Accuracy Score Checking**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-52/Shoulder%20X-ray%20Classification/Images/xray3.png)

- **Error Analysis**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-52/Shoulder%20X-ray%20Classification/Images/xray4.png)

- **Confusion Matrix**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-52/Shoulder%20X-ray%20Classification/Images/xray5.png)
**********************************
## Conclusion
* Images classification is one of the hot topics in today's world.
* Usage of Concolution Neural Network in this type of classification works makes the developer easier to develope models using the architectures.
* For this project we have used the ***EfficientNet B1 Architecture*** to develop the model.
* ***EfficientNet B1 Architecture*** is having the accuracy of 0.88, with macro average of 0.78 and weighted average of 0.88.
* Hence, from my side, this is the best model to be deployed using this dataset, to detect the images from the shoulder x-ray dataset.
*****************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
