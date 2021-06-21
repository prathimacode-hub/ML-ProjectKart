# Age, Gender and Ethnicity Prediction
![Demo](https://raw.githubusercontent.com/Anshal55/ML-ProjectKart/Age_gender_ethnicity/Age%2C%20Gender%20and%20Ethnicity%20Prediction/Images/h103.png)

### Acess at : https://genderdetection101.herokuapp.com/

### Goal
The goal of this project is to be able to predict age , gender and ethnicity of a person just by looking at an image of a person.

### Dataset 
Used the dataset at : https://www.kaggle.com/nipunarora8/age-gender-and-ethnicity-face-data-csv

## Steps:
- From the data given wrote functions to extract the image data from the "pixels" column and reshape it into suitable format.
- Split the data into train,test and validation subsets.
- Used an Image Data generator to perform some processing on the images and get them ready for training.
- Built sequential as well as functional models for all the three predictions and used the ones I got best results from.
- Trained the models
- Tested the models
- Finally , Deployed the model for identifying the gender.

### I used CNN model for prediction

### Libraries used
- Numpy
- Pandas
- Matplotlib, Seaborn
- Keras,Tensorflow
- Scikit-Learn
- Flask
- Gunicorn
- OS

### Results
I got following results:
- For Age prediction : Best MAE of 6.7
- For Gender Prediction : Accuracy of 89%
- For Ethnicity Prediction : Accuracy of 76%
