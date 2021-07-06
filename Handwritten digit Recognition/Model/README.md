#  HANDWRITTEN DIGIT RECOGNITION

**GOAL** 
- The main purpose of this project is to recognize handwritten digits by humans.

**DATASET**
- The data used in this project can be downloaded from [here](https://www.kaggle.com/c/mnist-handwritten-digit-recognition/data)
- Data containes images of handwritten digits between 0 to 9 in csv format.

**WHAT I HAD DONE**
- Preprocessed the images before model training.
- Build Convolution Neural network Architecture and trained the model.
- Evaluated the model using Accuracy score.
- Visualized Model's performance using seaborn and matplotlib libraries..


## CONVOLUTIONAL NEURAL NETWORK
 
 ***Network Architecture***
 - Input Dense Layer | Activation Function : Relu
 - Three Conv2D Layers, maxPooling2D | Activation Function : Relu
 - Output layer | Activation Function : Softmax
 - loss : categorical_cross_entropy
 - metrics : accuracy_score
 - optimizer : Adam
 
 **RESULTS**
 - Train Accuracy : 97.8%
 - Test Accuracy : 98.7%
