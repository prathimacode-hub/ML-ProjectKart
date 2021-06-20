*License Plate Detection and Recognition #39*

*Goal:* This project is to identify the license plate of a vechile.

*Dataset :* https://i.pinimg.com/originals/a7/9d/52/a79d52c1348a467f83b512669f1e8584.jpg

*What I have done :*
-Firstly I have imported the required libraries, and loaded the dataset onto the notebook

-resize the image and grayscale it

-Every image will have useful and useless information, in this case for us only the license plate is the useful information the rest are pretty much useless for our program. 

 This useless information is called noise. Normally using a bilateral filter (Blurring) will remove the unwanted details from an image.

-then i used canny for edge detection

-to find the license plate we need to find the contours(its nothing but closed area) using findContours method 

-then i sorted contours based on minimum area 30 and ignores the ones below that

-for finding the license plate i used the loop by looping every contour and checking weather they have 4 edges or not if they have 4 edges that means its the license plate so break the loop

-If the lisence plate is not found it displays No contour detected

-masking the entire picture except for the place where the number plate is so that i can removed unwanted information

-Extracting the license plate out of the masked image by cropping it and saving it as a new image

-reading the number plate information from the segmented image

-Using pytesseract package we can read characters from image

*Libraries Needed:* opencv,numpy,imutils,pytesseract,matplotlib

*Conclusion:* This project helps you to detect and recognize the license plate number from the vechile image.
