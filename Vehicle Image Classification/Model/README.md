**PROJECT TITLE - Vehicle Image Classification**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Vehicle%20Image%20Classification/Images/project_viz.png"  width="400">


**GOAL** - The aim of this project is to classify a vehicle image which type of vehicle it is.First we will try to visualize the training images to understand how to perform this multiclass image classification. Then we will use Neural Network approaches: MLP and CNN, to train the model and finally compare the validation accuracy of both the models.The dataset contain 7 classes of vehicles.


**WHAT HAVE I DONE**

- Loading the paths of the training images set
- Multiclass classification classes
- Since this is a supervised learning approach to train the model we will have to label the images before giving it as input to the CNN and MLP model
- Converting the images and labels into numpy arrays
- Visualizing the vehicle images with their true labels
- Performing Data Augmentation using ImageDataGenerator to import training images and augment more images
- Defining a function to display sample images from the dataset when their corresponding labels are given as input
- **Building the Multi Layer Perceptron model**
   - Defining a function to determine the learning_rate decay based on epoch schedule.
   - Plotting the accuracy and validation accuracy
   - Plotting the loss and validation loss
   - Saving the MLP model

- **Building the CNN model**
   - Plotting the accuracy and validation accuracy
   - Plotting the loss and validation loss
   - Saving the CNN model  



<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Vehicle%20Image%20Classification/Images/disp.png" >


**MODELS USED**

- **Multi Layer Perceptron** - *A multilayer perceptron (MLP) is a feedforward artificial neural network that generates a set of outputs from a set of inputs. An MLP is characterized by several layers of input nodes connected as a directed graph between the input and output layers. MLP uses backpropogation for training the network.* 
- **Convolutional Neural Network** - *A feed forward deep learning neural network designed for processing structured arrays of data such as images. Convolutional neural networks are very good at picking up on patterns in the input image, such as lines, gradients, circles, or even eyes and faces. It is this property that makes convolutional neural networks so powerful for computer vision. Unlike earlier computer vision algorithms, convolutional neural networks can operate directly on a raw image and do not need any preprocessing.*


**LIBRARIES NEEDED**

- Tensorflow
- cv2
- glob
- matplotlib
- random
- math
- os
- numpy
- pandas
- PIL
- scikit learn
- keras
- skimage

**Comparing the models**

- ### **Multi Layer Perceptron**

    -  *After training the MLP model we get a Training Accuracy of 87.71% and a Validation Accuracy of 74.29%*
    -  Inference -  Since the validation accuracy is a bit more less with respect the training accuracy than normal cases, we can say that the model might have been a little overfitted on the training set.. 
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Vehicle%20Image%20Classification/Images/mlp_acc.png" width = "400">
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Vehicle%20Image%20Classification/Images/mlp_loss.png" width = "400">
    
    
#### Multi layer perceptron network is not considered to be very efficient over image data. Convolutional neural networks are considered to be more efficient since they also take into consideration, the pixels with their spatial structure and hence perform better than MLP networks. Therefore now we will try this project with CNN approach.

- ### **Convolutional Neural network**

    - *After training the CNN model we get a Training Accuracy of 95.00% and a Validation Accuracy of 87.12%, which shows that the CNN model has gained a much higher precision both in training and validation cases than the MLP model.*

     <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Vehicle%20Image%20Classification/Images/cnn_acc.png" width = "400">
    
     <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Vehicle%20Image%20Classification/Images/cnn_loss.png" width = "400">
    


**Conclusion**

In this project we have used a couple of Deep Learning frameworks to recognize the type of vehicle that is given in the images. The MLP model performs fairly but gets slightly overfitted. However, CNN approach is then used to train the dataset which performs well and gives a validation accuracy of 87.12% .

