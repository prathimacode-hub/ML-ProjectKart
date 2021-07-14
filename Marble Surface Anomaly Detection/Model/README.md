# Marble Surface Anomaly Detection
Anomaly detection is any process that finds the outliers of a dataset; those items that don’t belong. These anomalies might point to unusual network traffic, uncover a sensor on the fritz, or simply identify data for cleaning, before analysis.

In today’s world of distributed systems, managing and monitoring the system’s performance is a chore—albeit a necessary chore. With hundreds or thousands of items to watch, anomaly detection can help point out where an error is occurring, enhancing root cause analysis and quickly getting tech support on the issue. Anomaly detection helps the monitoring cause of chaos engineering by detecting outliers, and informing the responsible parties to act.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-49/Marble%20Surface%20Anomaly%20Detection/Images/mar1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/wardaddy24/marble-surface-anomaly-detection-2.

## Goal
The goal of this project is to make a detection model which will detect which type of marble is present.
********************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-49/Marble%20Surface%20Anomaly%20Detection/requirements.txt).
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
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-49/Marble%20Surface%20Anomaly%20Detection/Images/mar2.png)
*************************************
## Model Visualization
- **Accuracy Score Checking**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-49/Marble%20Surface%20Anomaly%20Detection/Images/mar3.png)

- **Error Analysis**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-49/Marble%20Surface%20Anomaly%20Detection/Images/mar4.png)

- **Confusion Matrix**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-49/Marble%20Surface%20Anomaly%20Detection/Images/mar5.png)
**********************************
## Conclusion
* Images classification is one of the hot topics in today's world.
* Usage of Concolution Neural Network in this type of classification works makes the developer easier to develope models using the architectures.
* For this project we have used the ***EfficientNet B1 Architecture*** to develop the model.
* ***EfficientNet B1 Architecture*** is having the accuracy of 0.99, with macro average of 0.97 and weighted average of 0.99.
* Hence, from my side, this is the best model to be deployed using this dataset, to detect the anomaly in the marbles.
*****************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
