Cats Vs Dogs Classification

GOAL 
The goal of this project is to classify whether the image is of a dog or a cat.

DATASET Dataset can be downloaded from dataset of ENHANCEMENT folder.

WHAT I HAD DONE

I have reshaped the image and then the colored image has been taken for model creation.
Then I used Covolutional Neural Network(CNN) from keras API of tensorflow to train on the dataset.

cat_preprocessed

MODELS USED

CNN
LIBRARIES NEEDED

numpy
os
opencv(cv2)
tensorflow

CONCLUSION 
The models can be good in predicting dog or cat or both but atleast one of them. So in this I have used 4 different models and take the average result of the model if it is 0 then 
it is cat if not zero then we predict it as dog. So we can only comment on the 
accuracy:0.92 above
all the models are mostly good in prediction of cat and above average in prediction of dog. 
The idea behind using 4 differnt model is inspired by ensemble learning to improve the accuracy.
