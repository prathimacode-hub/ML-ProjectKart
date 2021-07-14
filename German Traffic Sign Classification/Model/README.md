# German-Traffic-Sign-Classification
In this project, I used Python and TensorFlow to classify traffic signs.

Dataset used: German Traffic Sign Dataset. This dataset has more than 50,000 images of 43 classes. 

<a ="https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-signhttps://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign" </a>

<b>Libraries and requirements</b>

<a>https://github.com/Best-forever-003/ML-ProjectKart/blob/main/German%20Traffic%20Sign%20Classification/requirements.txt</a>

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

# Data Visualization

<b>Data to Tensors</b>

![](https://github.com/Best-forever-003/ML-ProjectKart/blob/main/German%20Traffic%20Sign%20Classification/Images/Data%20to%20Tensors.png)

<b>Training data</b>

![](https://github.com/Best-forever-003/ML-ProjectKart/blob/main/German%20Traffic%20Sign%20Classification/Images/training.png)

<b>Data Loss</b>

![](https://github.com/Best-forever-003/ML-ProjectKart/blob/main/German%20Traffic%20Sign%20Classification/Images/Data%20loss.png)

<b>Data Accuracy</b>

![](https://github.com/Best-forever-003/ML-ProjectKart/blob/main/German%20Traffic%20Sign%20Classification/Images/training.png)

<b>Conclusion</b>

I have made the training accuracy to 60%. It can be increased if we train our model more!

Faster RCNN can be used but as we are doing it in a classification based problem, we are avoiding that.

By having such a model, people will follow the rules.

Accidents and all kinds of indiscipline drib=ving can be reduced.

Compared with previous traffic sign benchmarks, images in this benchmark are more variable, and signs in these images are much smaller.

Data Augmentation has also been done for better generalization.

It contains more images than previous benchmarks, and the images have a higher resolution.

In future, we plan to seek out more traffic signs of the classes that rarely appear in this benchmark.


# Author

<b>Aamir P</b>

"https://github.com/Best-forever-003"
