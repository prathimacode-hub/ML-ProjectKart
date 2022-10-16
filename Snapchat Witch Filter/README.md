
## Project Title

Snapchat Filters using OpenCV 


## GOAL
* To Make a snapchat filter for a Face which is detected

## Dependencies
* Python
* The program makes use of Dlib-facial feature points
* OpenCV
* Tkinter
* Shape predictor 68 face landmark points Model

## Approach/Procedure Used
* In order to build our Snapchat filter, we shall focus on the Detection of Facial Features using OpenCV with Haar Cascade Classifiers
* OpenCV uses machine learning algorithms to search for faces within a picture. Because faces are so complicated, there isn’t one simple test that will tell you if it found a face or not. Instead, there are thousands of small patterns and features that must be matched
* For something like a face, you might have 6,000 or more classifiers, all of which must match for a face to be detected (within error limits, of course).
* Since face detection is such a common case, OpenCV comes with a number of built-in cascades for detecting everything from faces to eyes to hands to legs. There are even cascades for non-human things
* The detectMultiScale function is a general function that detects objects. Since we are calling it on the face cascade, that’s what it detects.

  * The first option is the grayscale image.

  * The second is the scaleFactor. Since some faces may be closer to the camera, they would appear bigger than the faces in the back. The scale factor compensates for this.

  * The detection algorithm uses a moving window to detect objects. minNeighbors defines how many objects are detected near the current one before it declares the face found. minSize, meanwhile, gives the size of each window.



## Conclusion
- This is the Picture corresponding to Output![Result](https://user-images.githubusercontent.com/65017645/193783150-073b66a2-e9b9-4bd1-8b48-a791384b8bf0.png)




## Installing
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


## To run
- `facial_test.py`          <--- inital script that finds faces and eyes in images
- `halloween_masks.py`      <--- edited `facial_test.py` script that adds `witch.png` to faces
- `halloween_masks_vid.py`  <--- edited `halloween_masks.py` script with live video feed instead of static images
- `saved.png`               <--- static image of Saved by the Bell Cast used for testing
- `witch.png`               <--- filter image to be placed on faces
- `witch.gif`               <--- gif of screen recording of `halloween_masks_vid.py`
