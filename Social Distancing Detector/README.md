# :dart: Social Distancing Detector
## :star2: Objective:
To detect whether people are maintaining social distancing in public places or not.
<p align="center">
  <img width="600" height="300" src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7603992/bin/gr2_lrg.jpg">

</p>

## :star2: Introduction
   Recent improvement in deep learning allows object detection tasks more effective.This work aims to present a deep learning-based social distance monitoring framework for the public campus environment from an overhead perspective. A deep learning model, i.e., YOLOv3 (You Only Look Once), is applied for human detection. The current model (pre-trained on frontal or normal view data sets) is initially tested on the overhead data set. Transfer learning is also used to improve the efficiency of the detection model. To the best of our knowledge, this work could be considered as the first effort to use an overhead view perspective to monitor social distance with transfer learning. The detection model detects humans and gives bounding box information. After human detection, the Euclidean distance between each detected centroid pair is computed using the detected bounding box and its centroid information. A predefined minimum social distance violation threshold is specified using pixel to distance assumptions. To check, either the calculated distance comes under the violation set or not, the estimated information is matched with the violation threshold.
   The model is designed for individuals who do not obey a social distance restriction, i.e., 6 feet of space between them. The authors used a mobile robot with an RGB-D camera and a 2-D lidar to make collision-free navigation in mass gatherings.
## :star2: Implementation:
:sparkle: Import numpy ,argparse , imutils ,cv2,os.

:sparkle: Deploy pre-trained YOLOv3 for human detection and computing their bounding box centroid information. In addition, a transfer learning method is applied to enhance the performance of the model.

:sparkle: Next, Use Euclidean distance to approximate the distance between each pair of the centroid of the bounding box detected. In addition, a social distance violation threshold is specified using a pixel to distance estimation.

:sparkle: Utilize a centroid tracking algorithm to keep track of the person who violates the social distance threshold.

:sparkle: Assess the performance of pre-trained YOLOv3 by evaluating it on an overhead data set.

## :star2: Output :
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/66861391/136165422-fe72461f-5342-4a80-884a-2717f1b9cc8b.gif">

</p>

## :star2: Applications:
It will be beneficial in crowded public places (eg: Airport , markets) to detect whether people are maintaining social distance among them or not.
## :star2: Conclusion:
In this work, a deep learning-based social distance monitoring framework is presented using an overhead perspective. The pre-trained YOLOv3 paradigm is used for human detection. As a person's appearance, visibility, scale, size, shape, and pose vary significantly from an overhead view, the transfer learning method is adopted to improve the pre-trained model's performance. The model is trained on an overhead data set, and the newly trained layer is appended with the existing model. To the best of our knowledge, this work is the first attempt that utilized transfer learning for a deep learning-based detection paradigm, used for overhead perspective social distance monitoring. The detection model gives bounding box information, containing centroid coordinates information. Using the Euclidean distance, the pairwise centroid distances between detected bounding boxes are measured. To check social distance violations between people, an approximation of physical distance to the pixel is used, and a threshold is defined.
 Experimental results indicated that the framework efficiently identifies people walking too close and violates social distancing.
