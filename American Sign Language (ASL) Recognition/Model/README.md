**PROJECT TITLE - American Sign Language (ASL) Recognition**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/American%20Sign%20Language%20(ASL)%20Recognition/Images/project_viz.png"  width="800">

>

**GOAL** - he aim of this project is to recognize what the person is trying to convey using different hand gestures. The dataset contains 29 classes which comprises of A to Z alphabets, nothing, space and delete hand gestures.



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
- Generating X data and y data using Image augmentation approac
- Visualizing the X data --> sign language image and the y data --> label of the sign language
- Data Processing
- Performing One Hot Encoding on the categorical features of the training data
- Verifying the dimensions of all variables before they are feeded to the models
- Building the CNN model
- Plotting the accuracy and validation accuracy
- Plotting the loss and validation loss
- Saving the CNN model
- Performing multiclass predictions
- Comparing the Actual label vs the Predicted label of the Sign Language image
- Confusion Matrix
- Classification report of the CNN model

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/American%20Sign%20Language%20(ASL)%20Recognition/Images/cnn_matrix.png"  width="300">


**MODELS USED**

- **Multi Layer Perceptron** - *A multilayer perceptron (MLP) is a feedforward artificial neural network that generates a set of outputs from a set of inputs. An MLP is characterized by several layers of input nodes connected as a directed graph between the input and output layers. MLP uses backpropogation for training the network.* 
- **Convolutional Neural Network** - *A feed forward deep learning neural network designed for processing structured arrays of data such as images. Convolutional neural networks are very good at picking up on patterns in the input image, such as lines, gradients, circles, or even eyes and faces. It is this property that makes convolutional neural networks so powerful for computer vision. Unlike earlier computer vision algorithms, convolutional neural networks can operate directly on a raw image and do not need any preprocessing.*


**CNN model results**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/American%20Sign%20Language%20(ASL)%20Recognition/Images/cnn_results.png">

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

    -  *After training and testing the MLP model we can conclude that it reaches a training accuracy of 91.99% and validation accuracy of 68.28%.*
    -  Inference -  Since the validation accuracy is much less than the training accuracy we can say that the model has been overfitted on the training set. 
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/American%20Sign%20Language%20(ASL)%20Recognition/Images/MLP_plot.png" width = "400">
    
### Multi layer perceptron network is not considered to be very efficient over image data. Convolutional neural networks are considered to be more efficient since they also take into consideration, the pixels with their spatial structure and hence perform better than MLP networks. Therefore now we will try this project with CNN approach.

-  **Convolutional Neural network**

    - *After training and testing the CNN model we can conclude that it reaches a training accuracy of 99.43% and validation accuracy of 99.78% which shows that the CNN model has gained a very high precision.*

     
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/American%20Sign%20Language%20(ASL)%20Recognition/Images/cnn_plot.png" width = "400">
    
### Therefore we can conclude that the CNN model has served our purpose well and successfully recognizes the American Sign Language images with their proper labels.


**Conclusion**

In this project we have used a couple of Deep Learning frameworks to recognize the American Sign Language. The MLP model performs fairly but gets overfitted. However, CNN approach is used to train the dataset which perfroms well and gives a validation accuracy of 99.78% .

