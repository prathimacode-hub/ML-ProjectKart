
# Generating Faces using DCGANs 

DataSet: [CelebFaces Attributes Dataset (CelebA)](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) to train the adversarial networks.

### Some samples of generated faces:
![generated_faces](https://user-images.githubusercontent.com/65017645/123641859-56298400-d840-11eb-9a5f-cdf1a5fd8cd3.png)


### Processed faces
<img width="697" alt="processed_face_data" src="https://user-images.githubusercontent.com/65017645/123641912-60e41900-d840-11eb-8679-d22e7a02624a.png">




## Face Generation
In this project, you'll define and train a DCGAN on a dataset of faces. Your goal is to get a generator network to generate new images of faces that look as realistic as possible!

The project will be broken down into a series of tasks from loading in data to defining and training adversarial networks. At the end of the notebook, you'll be able to visualize the results of your trained Generator to see how it performs; your generated samples should look like fairly realistic faces with small amounts of noise.


## To Generate Faces:
1. Just run the script ```dlnd_face_generation.ipynb```

## Project Steps:
1.Get the Data
You'll be using the CelebFaces Attributes Dataset (CelebA) to train your adversarial networks.
This dataset is more complex than the number datasets (like MNIST or SVHN) you've been working with, and so, you should prepare to define deeper networks and train them for a longer time to get good results. It is suggested that you utilize a GPU for training.

2.Pre-processe the Data
Since the project's main focus is on building the GANs, we've done some of the pre-processing for you. Each of the CelebA images has been cropped to remove parts of the image that don't include a face, then resized down to 64x64x3 NumPy images. Some sample data is show below.

3.Pre-process and Load the Data
Since the project's main focus is on building the GANs, we've done some of the pre-processing for you. Each of the CelebA images has been cropped to remove parts of the image that don't include a face, then resized down to 64x64x3 NumPy images. This pre-processed dataset is a smaller subset of the very large CelebA data.

4.Create a DataLoader

6.Define the Model
A GAN is comprised of two adversarial networks, a discriminator and a generator.

7.Initialize the weights of your networks

8.Build complete network

9.Discriminator and Generator Losses

10.Generator samples from training


## Libraries Imported :

* import pickle as pkl
* import matplotlib.pyplot as plt
* import numpy as np
* import problem_unittests as tests


-Neeraj Ap


