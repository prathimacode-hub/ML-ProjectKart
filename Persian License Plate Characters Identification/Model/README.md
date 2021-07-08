# Persian License Plate Characters Identification
In this project a license plate detection and recognition system for Iranian private cars is implemented. The proposed license plate localization algorithm is based on region elements analysis which works properly independent of distance (how far a vehicle is), rotation (angle between camera and vehicle), and contrast (being dirty, reflected, or deformed). In addition, more than one car may exist in the image. The proposed method extracts edges and then determines the candidate regions by applying window movement. The region elements analysis includes binarization, character analysis, character continuity analysis and character parallelism analysis. After detecting license plates, we estimate the rotation angle and try to compensate it. In order to identify a detected plate, every character should be recognized. For this purpose, we present 25 features and use them as the input to an artificial neural network classifier. The experimental results show that our proposed method achieves appropriate performance for both detection and recognition of the Iranian license plates.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-50/Persian%20License%20Plate%20Characters%20Identification/Images/per1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/amirebrahimi66/large-dataset-of-persian-license-plate-characters.

## Goal
The goal of this project is to make a detection model which will detect different characters from the Persian Number plate.
*****************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-50/Persian%20License%20Plate%20Characters%20Identification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Visualization
4. Data Cleaning
5. EfficientNet Model Deployment
6. Evaluate the model
7. Make Predictions
8. Conclusion

*********************************
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
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-50/Persian%20License%20Plate%20Characters%20Identification/Images/per2.png)
*************************************
## Model Visualization
- **Accuracy Score Checking**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-50/Persian%20License%20Plate%20Characters%20Identification/Images/per3.png)

- **Confusion Matrix**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-50/Persian%20License%20Plate%20Characters%20Identification/Images/per4.png)
**********************************
## Conclusion
* Images classification is one of the hot topics in today's world.
* Usage of Concolution Neural Network in this type of classification works makes the developer easier to develope models using the architectures.
* For this project we have used the ***EfficientNet B1 Architecture*** to develop the model.
* ***EfficientNet B1 Architecture*** is having the accuracy of 1.00, with macro average of 1.00 and weighted average of 1.00.
* Hence, from my side, this is the best model to be deployed using this dataset, to detect the characters in the license plate.
*****************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
