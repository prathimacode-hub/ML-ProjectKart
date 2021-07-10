## PROJECT TITLE - Honey Bee Pollen Detection
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Honey%20Bee%20Pollen%20Detection/Images/project_viz.png"  width="500">


**GOAL** - The aim of this project is to classify the images of the bees to detect whether they are carrying pollen grains or not.


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Honey%20Bee%20Pollen%20Detection/Images/train.png">


**WHAT HAVE I DONE**

- Importing libraries
- Importing dataset
- Data Visualizations
   - Distribution plot
   - Correlations Matrix
   - Scatter/Density plot
- Loading the images
- Image Preprocessing
- Image Augmentation using ImageDataGenerator
- Visualizations of the training images
- Greyscale visualization of the training images
- Visualizations of the validation images
- Greyscale visualization of the validation images
- Visualizations of the testing images
- Greyscale visualization of the testing images
- Building the CNN model
- Classification report
- Making predictions on the testing Images

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Honey%20Bee%20Pollen%20Detection/Images/corr.png"  width="300">


**MODELS USED**

- **Convolutional Neural Network** - *A feed forward deep learning neural network designed for processing structured arrays of data such as images. Convolutional neural networks are very good at picking up on patterns in the input image, such as lines, gradients, circles, or even eyes and faces. It is this property that makes convolutional neural networks so powerful for computer vision. Unlike earlier computer vision algorithms, convolutional neural networks can operate directly on a raw image and do not need any preprocessing.*


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Honey%20Bee%20Pollen%20Detection/Images/train_greyscale.png">


**LIBRARIES NEEDED**

- Tensorflow
- cv2
- glob
- matplotlib
- glob
- os
- Path
- numpy
- PIL
- scikit learn
- keras
- skimage


**CNN model results**


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Honey%20Bee%20Pollen%20Detection/Images/classif.png"  width="300">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Honey%20Bee%20Pollen%20Detection/Images/predictions.png">



**Conclusion**

In this project we have first made visualizations of the Bee images dataset using different techniques to understand the correlation, density and other insights of the data.Then we have splitted tbhe whole image set into Training, Validations and Testing set. These sets has been visualized individually in their Original and Greyscale form. Finally,  a CNN bianry classification model ahs been build which gives a validation accuracy of 86%. This trained has then been used to predict whether the bee images in the test set are carrying pollen or not.  
