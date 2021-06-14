# Sign Language Prediction
![image](https://user-images.githubusercontent.com/54211313/121914426-e13e5080-cd4f-11eb-93d7-42596867f4ae.png)

### Goal
The goal of this project is to be able to identify the sign language from an image. This could have a lot of useful applications in bridging the gap in communication by providing people not familiar with sign language a way to understand and communicate better.

### Dataset
The dataset for this project can be found at https://www.kaggle.com/datamunge/sign-language-mnist  .

### Steps I followed
- Get the data and separate labels and image information.
- Reshape image data into usable form.
- Used Image Data generator to get the data ready for model.
- Built a CNN model to train on the data.
- Trained the model and saved the best performing model.
- Test on the test data to see the performance of the model.

### Model I used is a Convolutional Neural Network

### Libraries Needed
- Numpy , Pandas
- Matplotlib , Seaborn
- Keras
- Scikit-Learn

### Results
After training the model using CNN I got an acuuracy of approx 93%.
