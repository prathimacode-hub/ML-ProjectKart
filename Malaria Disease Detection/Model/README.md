**PROJECT TITLE - American Sign Language (ASL) Recognition**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Malaria%20Disease%20Detection/Images/project_viz.png">

>

**GOAL** - The aim of this project is to recognize whether the image of the human cell is infected with Malaria disease or not.

**DATASET - https://www.kaggle.com/miracle9to9/files1**


**WHAT HAVE I DONE**

 **Convolutional Neural Network(CNN)  approach**

- Loading datasets
- Finding out the total number of Uninfected and Parasitized images in the train and test sets
- Visualizing the Uninfected cell and Parasitized cell images
- Performing Image augmentation using ImageDataGenerator
- Setting up numeric labels for the binary image classes
- Defining a function to plot the train/test loss and train/test accuracy
- Building the CNN Model
- Saving the model
- Performing model evaluation
- Predicting the cell images
    - Loading paths of prediction images
    - Defining a function to display the images that are to be predicted
    - Defining a function that will process the image and use the trained CNN model to detect whether the cell is infected by Malaria or not
    - Predicting Image 1
    - Predicting Image 2
    - Predicting Image 3
    - Predicting Image 4
    - Predicting Image 5
    - Predicting Image 6


**MODELS USED**

- **Convolutional Neural Network** - *A feed forward deep learning neural network designed for processing structured arrays of data such as images. Convolutional neural networks are very good at picking up on patterns in the input image, such as lines, gradients, circles, or even eyes and faces. It is this property that makes convolutional neural networks so powerful for computer vision. Unlike earlier computer vision algorithms, convolutional neural networks can operate directly on a raw image and do not need any preprocessing.*

***Model Accuracy achieved - 94.89%***


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


**Conclusion**

In this project we have used Convolutional neural Network approach to train a model on the provided images of uninfected and parasitized human cell. This model gives a validation accuracy of 94.89% and also detects all the images of the evaluation set with correct labels.

