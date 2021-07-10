# German-Traffic-Sign-Classification
In this project, I used Python and TensorFlow to classify traffic signs.

Dataset used: German Traffic Sign Dataset. This dataset has more than 50,000 images of 43 classes. 

<b>Pipeline architecture:</b>
Load The Data.
Dataset Summary & Exploration
turning data into tensors
Getting images and their labels
turning images into tensors
Data Preprocessing.
Normalization
resize
Design a Model Architecture. -CNN Model
Model Training and Evaluation.
Testing the Model Using the Test Set.

<b>Environement:</b>
Python 3.7
TensorFlow 2.4.1 (GPU support)

So, the above was just a summary! Let us dive in to our project!

<b>Introduction</b>
Traffic sign detection is a high relevance computer vision problem and is the basis for a lot of applications in industry such as Automotive etc. Traffic signs can provide a wide range of variations between classes in terms of color, shape, and the presence of pictograms or text.
In this challenge, we will develop a deep learning algorithm that will train on German traffic sign images and then classify the unlabeled traffic signs. The deep learning model will be built using Keras (high level API for tensorflow) and we will also understand various ways to preprocess images using OpenCV and also use a cloud GPU service provider.

<b>Data Understanding</b>
The Image dataset consists of 43 classes (Unique traffic sign images).
Training Set has 34799 Images , Test set has 12630 images and the validation set has 4410 images.

<b>Our Algorithm:</b>

1.Understand the data
2.Preprocess the data
3.Build the architecture of the model
4.Test the model
5.Iterate the same process until you achieve the optimal results

#Data Visualization
<b>Data to Tensors</b>
![image](https://user-images.githubusercontent.com/79377502/125165054-e063d780-e1b2-11eb-8c05-119563fff272.png)

<b>Training data</b>
![image](https://user-images.githubusercontent.com/79377502/125165211-a8a95f80-e1b3-11eb-8337-913a9208b6be.png)

<b>Data Loss</b>
![image](https://user-images.githubusercontent.com/79377502/125165235-c1197a00-e1b3-11eb-8290-1c0e2c77dffb.png)

<b>Data Accuracy</b>
![image](https://user-images.githubusercontent.com/79377502/125165246-d098c300-e1b3-11eb-9646-a9266abbc928.png)

<b>Conclusion</b>
I have made the training accuracy to 60%. It can be increased if we train our model more!

#Author
Aamir P
<a ="https://github.com/Best-forever-003 </a>
