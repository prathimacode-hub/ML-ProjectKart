
**Project Title**

Snapchat Filters using OpenCV 


**GOAL**
* To Make a snapchat filter for a Face which is detected

**Dependencies**
* Python
* The program makes use of Dlib-facial feature points
* OpenCV
* Tkinter
* Shape predictor 68 face landmark points Model

**Procedure USED**
-  In order to build our Snapchat filter, we shall focus on the Detection of Facial Features using OpenCV with Haar Cascade Classifiers



**Conclusion**
- This is the Picture corresponding to Output![Result](https://user-images.githubusercontent.com/65017645/193783150-073b66a2-e9b9-4bd1-8b48-a791384b8bf0.png)




**Installing**
* Git clone repository
```
git clone 
```
* Make sure to install the dependencies:
```
pip install dlib
```
* Any modifications needed to be made to files/folders
```
pip install opencv-python
```


**To run** 
- `facial_test.py`          <--- inital script that finds faces and eyes in images
- `halloween_masks.py`      <--- edited `facial_test.py` script that adds `witch.png` to faces
- `halloween_masks_vid.py`  <--- edited `halloween_masks.py` script with live video feed instead of static images
- `saved.png`               <--- static image of Saved by the Bell Cast used for testing
- `witch.png`               <--- filter image to be placed on faces
- `witch.gif`               <--- gif of screen recording of `halloween_masks_vid.py`
