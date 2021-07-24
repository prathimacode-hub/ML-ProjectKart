
## OBJECT DETECTION USING OPENCV
<img src='Images/obj.png'></img>


### GOAL
* <font size=3> To understand Computer Vision Libraries like OpenCV .</font>
* <font size=3> To detect various objects using Deep Learning Models with pretrained weights.</font>


### DATASET
Link to the [Dataset](https://cocodataset.org/#overview)

### DESCRIPTION
* <font size=3>This Project aims to develop model for detecting objects using OpenCV. </font>
* <font size=3>OpenCV is a library of programming functions mainly aimed at real-time computer vision. </font>
* <font size=3>Using Deep Neural Network Detcetion Model with pretrained weights we will detect objects like book etc and draw bounding box around them for detection.</font>
* <font size=3>We will be using pretrained weights of the [ssd_mobilenet_v2_coco](https://docs.openvinotoolkit.org/2021.3/omz_models_model_ssd_mobilenet_v2_coco.html) or the Single Shot Multiobject Detection Network for building our DNN model.
* <font size=3>DetectionModel allows to set params for preprocessing input image. DetectionModel creates net from file with trained weights and config, sets preprocessing input, runs forward pass and return result detections. For DetectionModel SSD, Faster R-CNN, YOLO topologies are supported.</font>
  
 
### WHAT I HAVE DONE
  * <font size=3>Capture the Video Input Stream and set the width and height of the stream.</font>
  * <font size=3>Open the coco_names file in reading mode and copy the contents to a list by removing any right whitspaces .</font>
  * <font size=3>Initialize the configuration and weights to configPath and weightsPath.</font>
  
  <img src='Images/obj2.png'></img>
  
  * <font size=3>Create a Deep Neura Network Model using the Configuration and Pretrained Weights.</font>
  * <font size=3>Start capturing the images through video stream.</font>
  * <font size=3>Detect classIDs ,confidence, bounding box by setting a confidence threshold of 0.5.</font>
  * <font size=3>Draw a Bounding rectangle for every detection and label the object detected with a text.</font>
  * <font size=3>Display the object detected and stop video input stream by setting 'q' as the quitting key.</font>
  
  
  <img src='Images/obj3.png'></img>
  
  ### MODELS USED
  * <font size=3>DNN Detection Model</font>
  * <font size=3>SSD Mobile-Net network.</font>
  
  ### LIBRARIES NEEDED
  * <font size=3>OpenCV</font>
  
  ### CONCLUSION
  * Understood object detection using OpenCV.
  * We can use OpenCV for tasks like object detection,face recognition,Image segmentation etc.
  * We can use pretrained weights of classic networks for our own customized tasks.
  
  ### REFERENCES
  * https://docs.opencv.org/4.5.0/d3/df1/classcv_1_1dnn_1_1DetectionModel.html
  * https://cocodataset.org/#home
  * https://docs.openvinotoolkit.org/2021.3/omz_models_model_ssd_mobilenet_v2_coco.html
  
  ## BY
  ## VAISHNAVI PATIL
