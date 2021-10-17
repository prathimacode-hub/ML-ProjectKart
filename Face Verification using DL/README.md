# Live Face Verification Using Deep Learning

## Face Detection and landmark detection : 
OpenCV is the cross-platform open-source library for computer vision, machine learning, and image processing using which we can develop real-time computer vision applications. It is mainly used for image or video processing and also analysis including object detection, face detection, etc.
The model for 3D face landmarks has been employed using transfer learning and it is trained on a network with different objectives: the network predicts 3D landmark coordinates on synthetic rendered data. The resulting network performed reasonably well on real-world data.
The facial landmark detector included in the dlib library is an implementation of the One Millisecond Face Alignment with an Ensemble of Regression Trees paper by Kazemi and Sullivan (2014).
The 3D landmark network takes input as a cropped video frame without additional depth input. The model outputs the positions of the 3D points, reasonably aligned in the input.
It is done using Multi-task Cascaded Convolutional Networks(MTCNN) model. Used a pretrained model of MTCNN to detect face, to find the bounding box and landmark detection.

## Reference : 
* https://arxiv.org/pdf/1604.02878.pdf
* https://github.com/ipazc/mtcnn
* https://arxiv.org/pdf/1503.03832.pdf

Face Verification : The face Recognition is done using Facenet model. Used a pretrained facenet model to compare the captured image with images in database to verify person's face
1. MTCNN Pretrained Model : Follow link -https://github.com/ipazc/mtcnn
2. FaceNet Pretrained Model : https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk

## Dependency :
 1. Python 3.6
 2. tensorflow r1.12 or above 
 3. OpenCV 4.1.1 or above

## How to Run the Code :
 1. Download and extract the Face_verification.zip code into a folder.
 2. Download the pretrained model from the link given and place the files in the extracted folder in step 1.
 3. Input some images of person inside the database folder.
 4. Now execute the Live_Face_Verification.py script.

## Execution:  
 1. The image captured can be seen inside captured folder.
 2. The detected face with bounding box, cropped part of image and land mark detected images can be seen inside folder check.

### Note : 
 1. Use the port number for the webcam according to Device Configration of your sytem.(Edit :Face_Rec.py,  Line 9 ,                 camera=cv2.VideoCapture(0)). 
 2. Use webcam with resolution greater than 640x480 for better accuracy.

## Output :[Here](https://github.com/NEERAJAP2001/ML-ProjectKart/blob/6ea41751cb91bb4457d90cfa9ac5d61dd8151ee7/Face%20Verification%20using%20DL/Images/Output.jpeg)
![Output](https://user-images.githubusercontent.com/65017645/135712729-917ea8c9-a10c-4ebe-99d8-0bc8cafcec37.jpeg)

         
