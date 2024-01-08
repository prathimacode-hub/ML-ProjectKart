
# Gun Detection

This project focuses on implementing a gun detection system using YOLOv5, an efficient object detection model.




## Goal

The main goal of this project is to develop a robust gun detection system using YOLOv5 to accurately identify firearms within images. The purpose is to enhance safety measures by automating the detection process.


## Dataset

The dataset used for training this model is sourced from https://www.kaggle.com/atulyakumar98/gundetection

It providing diverse instances for model training and validation.


## Description

This project focuses on implementing a gun detection system using YOLOv5, an efficient object detection algorithm. The model is trained on a custom dataset specifically tailored for firearm identification within images.


## What I Had Done

### Dataset Preparation

Gathered a diverse dataset containing gun images from [https://www.kaggle.com/atulyakumar98/gundetection].

### Splitting the Dataset

Utilized a 70-20-10 split ratio for the dataset:

70% for Training: Contains a significant portion of the dataset for model training.

20% for Validation: Used for hyperparameter tuning and model validation during training.

10% for Testing: Reserved for evaluating the model's performance on unseen data.

### Data Augmentation Techniques:

Applied various data augmentation techniques during training, including:
* Horizontal and vertical flips to increase dataset diversity.
* Image blurring up to 2.5 pixels to simulate varying image     quality.
* Addition of noise up to 0.14 pixels to introduce variability in images.

### Transfer Learning

Transfer learning by initializing the model with YOLOv5s pre-trained weights.

## Models Used

### YOLOv5s Pre-trained Weights:
* Utilized YOLOv5s pre-trained weights as a base for transfer learning.
* These weights contain knowledge learned from a broader dataset (e.g., COCO) and serve as a starting point for the gun detection task.

## Libraries Used

### PyTorch

Used for building and training neural networks, essential for implementing machine learning models.

### Matplotlib

Used for creating visualizations, including plotting images and drawing bounding boxes around detected objects.


### PIL

The Python Imaging Library used for image processing tasks like opening, manipulating, and processing images.



## Accuracies

### Summary:

* Model: 157 layers, 7,012,822 parameters, 0 gradients, 15.8 GFLOPs
### Accuracy Metrics:

* Precision (P): 85.2%
* Recall (R): 83%
* mAP50: 87.1%

![P_curve](https://github.com/Pranay38/Surface-Defect-Detection/assets/100509183/90a3f707-1b4e-44df-bc1d-8cc5771e6807)
![PR_curve](https://github.com/Pranay38/Surface-Defect-Detection/assets/100509183/baa77313-4e35-481a-9754-a59d1cc38f30)
![R_curve](https://github.com/Pranay38/Surface-Defect-Detection/assets/100509183/6851823a-7d3f-44d9-8032-06df9425c138)

## Conclusion

The project successfully implements a guns detection system using YOLOv5 with high accuracy. The trained model reliably identifies guns within images, contributing to enhanced safety measures.
## Authors

- This code contributed by [Pranay Agrawal](https://github.com/Pranay38)

