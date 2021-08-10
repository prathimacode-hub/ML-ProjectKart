# Detecting Motion and Moving Objects in a Video

**GOAL:**
In this project, we will build something that can help us to detect motion and moving objects from a video using some libraries with Python programming language.

**DATASET:**
No dataset is required or available. Instead we will be using a video of our choice.

**WHAT I HAD DONE:**

I have created a project for detecting motion and moving objects from a video.

First I am reading the video of moving objects for getting the frames from the video to check the motion of objects.

Then after getting two different frames from the video, we are applying the gaussian blurr on both the frames.

We are taking the absloute difference between the frames so that the cars that has moved are highlighted in grayish-white color.

And now first we will create a threshold, it will give us total white color for those cars which are moving or in motion.

Then we will find these white pixels to detect motion by calculating the number of white pixels.

After that we are checking the condition if white pixels are more than 5% of total pixels in the frame, if pixels are detected then the object is in motion otherwise not.

Now filling the gaps in white pixels using dilate (dilation) so that we can draw bounding boxes, now these are the counters and can be detected. 

After doing this, we will find the counters then will draw the rectangles or bounding boxes to highlight the objects

And finally, displaying the frame or image in which the objects have moved from their positon.

**MODELS USED:**

We are not using any traditional model for performing this task.

**LIBRARIES NEEDED:**
- Numpy
- OpenCV
- Matplotlib
