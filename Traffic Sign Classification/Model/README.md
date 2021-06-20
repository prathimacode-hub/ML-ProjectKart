## Traffic Sign Classification

# GOAL

To make human readable traffic sign class.

# What Have I Done

There are 42 classification of the dataset and have following labels:

<table>
  <tr>
    <th> Class Id </th>
    <th> Name </th>
  </tr>
   <tr>
<tr><th> 0 </th><th> Speed limit (20km/h) </th> </tr>
 <tr><th> 1 </th><th> Speed limit (30km/h) </th> </tr>
 <tr><th> 2 </th><th> Speed limit (50km/h) </th> </tr>
 <tr><th> 3 </th><th> Speed limit (60km/h) </th> </tr>
 <tr><th> 4 </th><th> Speed limit (70km/h) </th> </tr>
 <tr><th> 5 </th><th> Speed limit (80km/h)  </th></tr>
 <tr><th> 6 </th><th> End of speed limit (80km/h) </th> </tr>
 <tr><th> 7 </th><th> Speed limit (100km/h)  </th></tr>
 <tr><th> 8 </th><th> Speed limit (120km/h) </th> </tr>
 <tr> <th>9 </th><th> No passing </th> </tr>
 <tr><th> 10 </th><th> No passing for vechiles over 3.5 metric tons </th> </tr>
 <tr><th> 11 </th><th> Right-of-way at the next intersection </th> </tr>
 <tr><th> 12 </th><th> Priority road  </th></tr>
 <tr><th> 13 </th><th> Yield </th> </tr>
 <tr><th> 14 </th><th> Stop  </th></tr>
 <tr><th> 15 </th><th> No vechiles </th></tr>
 <tr><th> 16 </th><th> Vechiles over 3.5 metric tons prohibited  </th></tr>
 <tr><th> 17 </th><th> No entry </th> </tr>
 <tr><th> 18 </th><th> General caution  </th></tr>
 <tr><th> 19 </th><th> Dangerous curve to the left </th> </tr>
 <tr><th> 20 </th><th> Dangerous curve to the right  </th></tr>
 <tr><th> 21 </th><th> Double curve  </th></tr>
 <tr><th> 22 </th><th> Bumpy road  </th></tr>
 <tr><th> 23 </th><th> Slippery roadv  </th></tr>
 <tr><th> 24 </th><th> Road narrows on the right  </th></tr>
 <tr><th> 25 </th><th> Road work  </th></tr>
 <tr><th> 26 </th><th> Traffic signals  </th></tr>
 <tr><th> 27 </th><th> Pedestrians </th> </tr>
 <tr><th> 28 </th><th> Children crossing </th> </tr>
 <tr><th> 29 </th><th> Bicycles crossing  </th></tr>
 <tr><th> 30 </th><th> Beware of ice/snow </th> </tr>
 <tr><th> 31 </th><th> Wild animals crossing </th> </tr>
 <tr><th> 32 </th><th> End of all speed and passing limits </th> </tr>
 <tr><th> 33 </th><th> Turn right ahead  </th></tr>
 <tr><th> 34 </th><th> Turn left ahead  </th></tr>
 <tr><th> 35 </th><th> Ahead only  </th></tr>
 <tr><th> 36 </th><th> Go straight or right  </th></tr>
 <tr><th> 37 </th><th> Go straight or left  </th></tr>
 <tr><th> 38 </th><th> Keep right  </th></tr>
 <tr><th> 39 </th><th> Keep left  </th></tr>
 <tr><th> 40 </th><th> Roundabout mandatory </th> </tr>
 <tr><th> 41 </th><th> End of no passing </th> </tr>
 <tr><th> 42 </th><th> End of no passing by vechiles over 3.5 metric tons  </th></tr>
  </table>
  
 ![](https://github.com/Isha307/ML-ProjectKart/blob/main/Traffic%20Sign%20Classification/Model/Image/Class.png)
  
 I created a model that will label the pictures on the basis of above labels and you can check the demo in output file.
 
  * [MODEL](https://github.com/Isha307/ML-ProjectKart/blob/main/Traffic%20Sign%20Classification/Model/model.ipynb)
  * [OUTPUT](https://github.com/Isha307/ML-ProjectKart/blob/main/Traffic%20Sign%20Classification/Model/output.ipynb)
  
 ## Output will be like:
 
 ![](https://github.com/Isha307/ML-ProjectKart/blob/main/Traffic%20Sign%20Classification/Model/Image/imgOriginal.png)
  
# Model Used
  
  ## CNN
  
# Libraries Needed
  
 * pandas 
  
 * numpy 
  
 * matplotlib

 * cv2

 * tensorflow 
 
 * sklearn
 
 * pickle
 
 * PIL 

# CONCLUSION
  
  ```
  Test Score: 0.07600177079439163
  Test Accuracy: 0.9776217341423035
  ```
