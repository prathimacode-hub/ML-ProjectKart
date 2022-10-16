💠**PROJECT TITLE**

Social Distancing Detector

💠**GOAL**

To detect whether people are maintaining social distancing in public places or not.


💠**DESCRIPTION**

In this work, a deep learning-based social distance monitoring framework is presented using an overhead perspective. The pre-trained YOLOv3 paradigm is used for human detection. Euclidean distance is used to calculate distance among people.

💠**WHAT I HAD DONE**

❇Import numpy ,argparse , imutils ,cv2,os.

❇ Deploy pre-trained YOLOv3 for human detection and computing their bounding box centroid information. In addition, a transfer learning method is applied to enhance the performance of the model.

❇ Next, Use Euclidean distance to approximate the distance between each pair of the centroid of the bounding box detected. In addition, a social distance violation threshold is specified using a pixel to distance estimation.

❇ Utilize a centroid tracking algorithm to keep track of the person who violates the social distance threshold.

❇ Assess the performance of pre-trained YOLOv3 by evaluating it on an overhead data set.

💠**MODELS USED**

I have used YOLOV3 Algorithm because YOLOv3  is fast, has at par accuracy with best two stage detectors (on 0.5 IOU) and this makes it a very powerful object detection model. . A very good accuracy with the best speed makes YOLOv3 a go to object detection model 

💠**LIBRARIES NEEDED**

numpy , argparse , imutils , cv2 , os.

💠 **Output**
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/66861391/136165422-fe72461f-5342-4a80-884a-2717f1b9cc8b.gif">

</p>

💠**CONCLUSION**

The model is trained on an overhead data set, and the newly trained layer is appended with the existing model. To the best of our knowledge, this work is the first attempt that utilized transfer learning for a deep learning-based detection paradigm, used for overhead perspective social distance monitoring. The detection model gives bounding box information, containing centroid coordinates information. Using the Euclidean distance, the pairwise centroid distances between detected bounding boxes are measured. To check social distance violations between people, an approximation of physical distance to the pixel is used, and a threshold is defined. Experimental results indicated that the framework efficiently identifies people walking too close and violates social distancing.


💠**CONTRIBUTOR**

 FRENY REJI
 
 ![LinkedIn](www.linkedin.com/in/freny-reji-2401)
 
 ![GitHub](https://github.com/freny24)
