**Classification of Images Using MNIST and CIFAR10**

**GOAL**

Classifying and predictinhg images with accuracy

**DATASET**<br>

Already prresent in keras.datasets library <br>
https://keras.io/api/datasets/ <br>
or you can download it as csv file from here <br>
https://www.kaggle.com/c/digit-recognizer/data <br>
https://www.kaggle.com/valentynsichkar/cifar10-preprocessed <br>

**DESCRIPTION**<br>
Classifies Images in the mnist and cifar10 dataset and predicts the test set image labels with accuracy.<br>
mnist contains images of digits 0-9 in grey scale and cifar10 contains coloured images of different objects.


**WHAT I HAD DONE** <br>
Internal splitting the training dataset for validation purposes <br>
Separating images according to labels <br>
Scaling down the images and convert the labels into classes (categorical) and one hot vector.<br>
Internal splitting the training dataset for validation purposes<br>
Creating the model <br>
Training this Neural Network <br>
Performing Predictions with accuracy for both datasets.<br>

**MODELS USED**

2 Sequential models created manually having conv2D, Maxpooling, dense and flatttened layers.

**LIBRARIES NEEDED**

keras<br>
matplotlib<br>
tensorflow<br>
sklearn-learn

**ACCURACIES**

98 and 79 percent test accuracy for 2 models. Sequential model is used for both. with convulusional , max pool, dense and flattening layers.


**CONCLUSION** <br>
Convolution neural network is trained for mnist dataset using 1 convolutional layer and 2 fully connected layers. 
It is observed that training accuracy is 99.1% and testing accuracy is 98.7% for batch size 128 and epochs 5. And for cifar10 79 tsting set accuracy for batch size 100 and epochs 7.
Accuracy can be improved with more epochs and tuning hyper parameters. 

## Data Visualization Images
<br>

<img width = 385 height = 300 src="../Images/MNISTImage1.png">

<br>
<img width = 400 height = 400 src="../Images/CIFAR10Image1.png">

<br>
<img width = 385 height = 300 src="../Images/CIFAR10Image2.png">

**YOUR NAME**

Ritika chand
