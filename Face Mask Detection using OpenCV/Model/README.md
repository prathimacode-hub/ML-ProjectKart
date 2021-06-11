**PROJECT TITLE - Face mask detection using OpenCV**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Face%20Mask%20Detection%20using%20OpenCV/Images/Project_vis.png" width="300">

**GOAL** - This a Face Mask Detection project that uses both Haar Cascades and Caffe framework approaches for face detection and a finetuned MobileNetV2 model to detect masks on face taking real time video stream as input.

**DATASET** Download the data set from https://www.kaggle.com/omkargurav/face-mask-dataset

**WHAT HAVE I DONE**
- Loading datasets
- Separating images according to labels
- Scaling down the images and using Labelbinarizer to convert the labels into class 0 and 1(categorical).
- Internal splitting the training dataset for validation purposes and using ImageDataGenerator to create more sample images using zooming and rotating technique.
- Loading the base model MobileNetV2 and creating the Head model by removing the top layers.
- Finetuning the topmost layers by adding Flatten(), Dense(), Dropout and Dense() layers.
- Training this Neural Network keeping Batch size = 12 and 30 epochs.
- Performing Predictions with a 99% achieved accuracy.
- After training is done the video stream is taken as input once using Haar Cascades and then with caffemodel by deploying the framework using the prototxt file.Both of these algorithms detect the face. Now they are combined with the finetuned mask detection CNN model to detect face mask.
- The input video frames are converted into blobs by using the BlobFromImage concept of OpenCV and real time predictions are delivered.

**The Haar Cascades approach was found to be inefficient as the model was unable to detect the dark contoured mask. It also failed to detect the face when the angle of face with respect to the camera exceeded from 0 degree(straight) in either sides. However the Caffe approach proved to be quite efficient and deliver appropriate predictions. This can be verified from the provided demonstration video.**

**MODELS USED**
- MobileNetV2 - *This is a very light weight and versatile model with a high accuracy rate compared to others like MobileNetV1 or VGG16. It can also be deployed on applications.*
- Haar Cascades - *Haar cascades is remarkably fast and delivers speedy predictions. Its one of the most coomon approach for Computer Vision Projects and so I used it too but unfortunately, it did not perfrom very well.*
- Caffe - *After getting unsatisfactory results from Haar Cascades I tried to stitch up the Caffe framework with the finetuned mask detection model and the results were good. Caffe is a Deep learning framework with features like layering architecture and implementation, modularity and test coverage.Lastly, its open source:)*

**LIBRARIES NEEDED**
- numpy
- os
- matplotlib
- imutils
- tensorflow
- keras
- scikit-learn
- cv2

**ScreenShots**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Face%20Mask%20Detection%20using%20OpenCV/Images/testing_snap2.png" width="400">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Face%20Mask%20Detection%20using%20OpenCV/Images/testing_snap1.png" width="400">

**Here is the Demonstration Video link -** https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Face%20Mask%20Detection%20using%20OpenCV/Images/Demonstration%20video%20of%20both%20models(Compressed).mp4 


**Conclusion**

We can conclude from this project that the Caffe framework outstands the Haar Cascades approach. The finetuned MobileNetV2 mask predictor model with 99% accuracy is a good example of transfer learning.
Here, I am providing the training plot for a better understanding of the Mask predictor model.

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Face%20Mask%20Detection%20using%20OpenCV/Images/plot_v2.png" width="400">
