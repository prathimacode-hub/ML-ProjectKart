![Dogs](https://s.wsj.net/public/resources/images/B3-EU419_201908_GR_20190822110317.jpg)

# Dog Breed Identification
This project is about predicting the breed of a dog, this can be helpful to people who are not expert in the field.
- The dataset consists of about 10,000 images for training, I used an Image data generator to get the train and validation data.
- The preprocessing fumction used on the images is from a pre-built model.
- I have used transfer leaning to get the level of desired acuuracy.
- The model is saved which produces best results.
- After that I use that model to build a service that would predict the breed of a dog based on the images uploaded by the user.
- I use flask for this
- How it would work is explained in the "Working Section".

## What it does?
Given an image model predicts the breed of the dog present in the said image.

The Dataset I used for this can be found here:
https://www.kaggle.com/c/dog-breed-identification/data

The Notebook can be found here or at:
https://www.kaggle.com/anshalsingh/dog-breed-identification

## Working
To get the model setup on your machine downlad the model from here https://drive.google.com/file/d/1PoZVJyJibe36KJIrdGa52YIrkPQ52uHZ/view?usp=sharing and put in the main directory.

Run the "app.py" script given in the folder if requirements satisfied it would lead to a link , open that in browser and you're ready to predict.

![Demo](https://raw.githubusercontent.com/Anshal55/ML-ProjectKart/Dog_breed_identification/Dog_Breed_Detection/Images/WorkingDemo.png)
