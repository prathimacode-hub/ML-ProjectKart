#  DRIVER DROWSINESS DETECTION SYSTEM

**GOAL** 
- The main purpose of this project is to awake the driver's if they fall asleep in order to avoid drowsiness related road-accidents.

**DATASET**
- The data used in this project can be downloaded from [here](http://mrl.cs.vsb.cz/eyedataset)

**WHAT I HAD DONE**
- Cleaned the data manually by adding 2 folder closed and open images from the original dataset
- Used MobileNet, since it is light-weighted model than the others(a pre-trained model on ImageNet dataset) for model selection
- Converted all the images into grayscale and resized it to 224 as the model can take this size as an i/p and is fed into the model
- Compared various models and used best performance model to make predictions.

**MODELS USED**
| Model | Accuracy Score |
| :--------: | :----------: |
| MobileNet | 1.0 |



**LIBRARIES NEEDED**
- pandas
- numpy
- matplotlib
- tensorflow
- opencv
- flask


**CONCLUSION**
- Hence a driver drowsiness system is built with the help of a CNN model which would alert the user whenever he/she falls asleep

**Author(s)**
Dilrose Reji
- DevIncept Participant
My Social Media Handles: 
- LinkedIn: [here](https://www.linkedin.com/in/dilrose-reji-7622081b2/)