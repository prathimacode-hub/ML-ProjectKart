# Emoji Classification using OpenCV
The data consists of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centred and occupies about the same amount of space in each image.

The task is to categorize each face based on the emotion shown in the facial expression into one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). The training set consists of 28,709 examples and the public test set consists of 3,589 examples.

## Goal
The Goal of this project is to make a model which will predict the emotion shown using the input image. And also it will classify the particular emotion shown in the given image.

## Algorithms and Libraries used
Various algoriehms are being used here to develope this project.
Major things are used here like,
- Tensorflow
- Keras
- OpenCV
- Numpy
- Pandas
- Matplotlib

using these libraries the whole project is developed and deployed successfully.

## Dataset
The dataset is being directly used from the Kaggle website, as given in the raised issue : https://www.kaggle.com/msambare/fer2013

## Procedure
The procedures of this project are discussed as the following -
- Import the libraries from the requirments.txt file.
- Open the Anaconda Navigator and upload the Jupyter Notebook file.
- Run all the cells one by one.
- Project deployed successfully!

## Output 
<img src = "Images/emoji.png">

## Accuracy of the model
The accuracy of the model is checked using the accuracy score and the cross validation score.
|Accuracy Metric|Score|
|:---:|:---:|
|Accuracy Score|71.73|
|CV Score|65.22|

## Conclusion
The accuracy score shows the deployment of the model is successfully done and is working properly!

### Author
Code contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
