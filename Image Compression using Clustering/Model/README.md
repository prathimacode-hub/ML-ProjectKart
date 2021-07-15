   **PROJECT TITLE - Image Compression using Clustering**
        
   <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/project_viz1.png" width="300">

**GOAL** - This is a image compression algorithm where clustering approach has been used to redude the color vectors of the image to k colors. 

**DATASET** Just upload an image of any format!

**WHAT HAVE I DONE**
- Loading images
- Converting the image into array -> (height,width,RGB channels) 
- Reshaping the RGB channels into 3 long vectors
- Developing the plot utils .py file
- Creating a ColorSpace vizualization of all the pixels in original image with 16 million colors.
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Original%20ColorSpace/image3_colorspace.png" width="300">

- Using MiniBatch K-Means to create clusters of k-colors and using ColorSpace to visualize the reduced pixel spread into k-colors.
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Compressed%20ColorSpace/image3_compressed_colorspace.png" width="300">

- Displaying both the original image and compressed image side by side for a better understanding. 
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Compressed%20Images/image3_compressed.png" width="300">

- Compressing each image one at a time is time-consuming, therefore created a Interactive Control widget to toggle between any image present in the directory and the compressed image gets displayed in real time.
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interactive_control.png" height='200' width="500">

**MODELS USED**
- K-Means Clustering - This algorithm group similar colors together into ‘k’ clusters of different colors (RGB values). Therefore, each cluster centroid is the representative of the three dimensional color vector in RGB color space of its respective cluster. You might have guessed by now how smoothly K-means can be applied on the pixel values to get the resultant compressed image. Now, these ‘k’ cluster centroids will replace all the color vectors in their respective clusters.
 
 **The working of this algorithm can be understood from the animation given below**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/project_amim1.png" width="300">


**LIBRARIES NEEDED**
- numpy
- os
- matplotlib
- plot_utils
- scikit-learn
- ipywidgets

**ScreenShots of Compressed Image in Interactive control**

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interact_1.png" width="500">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interact_2.png" width="500">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interact_3.png" width="500">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interact_4.png" width="500">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interact_5.png" width="500">

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Image%20Compression%20using%20Clustering/Images/Interactive%20Control%20Displays/interact_6.png" width="500">


**Conclusion**

The K-Means Clustering algorithm is an Unsupervised Machine Learning algorithm that deals with unlabelled data like the image data. Ih this project the k-clusters keep on changing their centroid coordinates until it reaches threshold convergence.  

