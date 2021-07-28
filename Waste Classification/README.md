**PROJECT TITLE - Waste Classification**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Waste%20Classification/Images/project_viz.png" width = 800>


**GOAL** - The aim of this project is to recognize whether the image of the waste product is a Organic Waste or a Recyclable Waste


**WHAT HAVE I DONE**

 **Convolutional Neural Network(CNN)  approach**

- Import Libraries
- Loading datasets
- Data Visualization
- Building the CNN Model
- MODEL EVALUATION
- Applying the model on Test set
    - Test Cases:1 - ORGANIC
    - Test Case:2 - RECYCLE

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Waste%20Classification/Images/display.png">


**MODELS USED**

- **Convolutional Neural Network** - *A feed forward deep learning neural network designed for processing structured arrays of data such as images. Convolutional neural networks are very good at picking up on patterns in the input image, such as lines, gradients, circles, or even eyes and faces. It is this property that makes convolutional neural networks so powerful for computer vision. Unlike earlier computer vision algorithms, convolutional neural networks can operate directly on a raw image and do not need any preprocessing.*

***Training Accuracy achieved - 98.61%***

***Validation Accuracy achieved - 89.02%***

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Waste%20Classification/Images/accuracy.png" width = 500>

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Waste%20Classification/Images/loss.png" width = 500>



**LIBRARIES NEEDED**

- Tensorflow
- cv2
- mpimg
- matplotlib
- random
- pandas
- seaborn
- os
- numpy
- PIL
- scikit learn
- keras
- Ipython

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Waste%20Classification/Images/pie_chart.png" width = 500>

Pre Trained model is available at https://drive.google.com/drive/folders/1XK8VJWKIExVRbgzcIrj_IuZr3dSTxydJ?usp=sharing


**Conclusion**

In this project we have used Convolutional neural Network approach to train a model on the provided images of Organic and Recyclable waste products. This model gives a Training accuracy of 98.61% and a Validation accuracy of 89.02% and also categorizes all the images of the evaluation set with correct labels.

