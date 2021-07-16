**PROJECT TITLE - English Alphabet Classification**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/project_viz.png"  width="500">


**GOAL** - The aim of this project is to recognize the computerised generated images of the English apphabets. The dataset contains 26 classes which comprises of a to z alphabets, each class containing 100 images.


**WHAT HAVE I DONE**

 **Multi Layer Perceptron(MLP) approach**

- Loading datasets
- Defining a function to display sample images from the dataset when their corresponding labels are given as input
- Performing Data Augmentation using ImageDataGenerator to import training images and augment more images
- Building the Multi Layer Perceptron model
- Defining a function to determine the learning_rate decay based on epoch schedule.
- Plotting the accuracy and loss curves


**Convolutional Neural Network(CNN) approach**

- Loading datasets
- Labelling the images before giving it as input to the CNN model
- Converting the images and labels into numpy arrays
- Performing Data Augmentation using ImageDataGenerator to import training images and augment more images
- Verifying the dimensions of all variables before they are feeded to the models
- Building the CNN model
- Plotting the accuracy and validation accuracy
- Plotting the loss and validation loss
- Saving the CNN model

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/viz1.png"  width="600">


**MODELS USED**

- **Multi Layer Perceptron** - *A multilayer perceptron (MLP) is a feedforward artificial neural network that generates a set of outputs from a set of inputs. An MLP is characterized by several layers of input nodes connected as a directed graph between the input and output layers. MLP uses backpropogation for training the network.* 
- **Convolutional Neural Network** - *A feed forward deep learning neural network designed for processing structured arrays of data such as images. Convolutional neural networks are very good at picking up on patterns in the input image, such as lines, gradients, circles, or even eyes and faces. It is this property that makes convolutional neural networks so powerful for computer vision. Unlike earlier computer vision algorithms, convolutional neural networks can operate directly on a raw image and do not need any preprocessing.*


**CNN model results**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/viz2.png">

**LIBRARIES NEEDED**

- Tensorflow
- cv2
- glob
- matplotlib
- random
- math
- os
- numpy
- PIL
- scikit learn
- keras
- skimage

**Comparing the models**

- **Multi Layer Perceptron**

    -  *After training and testing the MLP model we can conclude that it reaches a training accuracy of 57.15% and validation accuracy of 47.69%.*
    -  Inference -  Since the validation accuracy and the training accuracy is my much less, we can say that the MLP model is not the right choice for this type of multiclass classification.
 
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/mlp_acc.png" width = "400">
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/mlp_loss.png" width = "400">
    
    
### Multi layer perceptron network is not considered to be very efficient over image data. Convolutional neural networks are considered to be more efficient since they also take into consideration, the pixels with their spatial structure and hence perform better than MLP networks. Therefore now we will try this project with CNN approach.

-  **Convolutional Neural network**

    - *After training the CNN model we get a training accuracy of 98.80% and a validation accuracy of 92.69% after 50 epochs*

     
     <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/cnn_acc.png" width = "400">
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/English%20Alphabet%20Classification/Images/cnn_loss.png" width = "400">
    
    
### Therefore we can conclude that the CNN model has served our purpose well and successfully recognizes the English alphabet images with their proper labels.


**Conclusion**

In this project we have used a couple of Deep Learning frameworks to classify the computerised images of English alphabets. The MLP model is trained and its results are quite unsatisfactory. However, CNN approach is used to train the dataset which perfroms well and gives a validation accuracy of 92.69% .

