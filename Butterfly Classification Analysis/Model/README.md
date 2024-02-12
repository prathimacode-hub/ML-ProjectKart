# Butterfly CLASSIFICATION ANALYSIS<br>

## 🎯 Goal<br>
The primary goal of this project is to develop an image classification system for identifying different species of butterflies. The purpose is to create a model that can accurately categorize butterfly images into predefined classes, aiding in biodiversity monitoring and conservation efforts.<br>

## 🧵 Dataset<br>
The dataset used for this project consists of a collection of butterfly images sourced from [Dataset Link](https://www.kaggle.com/datasets/bertcarremans/butterfly-images). The dataset is curated to include various species of butterflies with labeled classes.<br>

## 🧾 Description
This project focuses on using machine learning techniques to build a robust butterfly image classification system. The developed models aim to distinguish between different butterfly species based on visual features extracted from images.<br>

## 🧮 What I had done!<br>
1. **Data Preprocessing:**<br>
   - Resized images to a standard input size for model compatibility.<br>
   - Normalized pixel values to the range [0, 1].<br>

2. **Model Architectures:**<br>
   - Custom Convolutional Neural Network (CNN): Designed for butterfly image features.
   - Transfer Learning: Utilized pre-trained models like VGG16 and ResNet50 for enhanced performance.

3. **Data Augmentation:**<br>
   - Applied image data augmentation techniques using TensorFlow's ImageDataGenerator to improve model generalization.

4. **Model Training:**<br>
   - Trained the custom CNN, VGG16, and ResNet50 models on the preprocessed and augmented dataset.
   - Evaluated models on a validation set to monitor performance.

5. **Save Models:**<br>
   - Saved the trained models for future use and predictions.

## 🚀 Models Implemented<br>
   - Custom Convolutional Neural Network (CNN)
   - VGG16-based Convolutional Neural Network
   

**Why these models:**<br>
   - Custom CNN: Designed for dataset-specific features.
   - VGG16: Known for simplicity and effectiveness in image classification tasks.
   

## 📚 Libraries Needed<br>
1. TensorFlow
2. Matplotlib
3. Numpy
4. Scikit-learn (for additional evaluation metrics if required)

## 📊 Exploratory Data Analysis Results<br>
**Distribution of Classes**
To gain an understanding of the dataset, we analyzed the distribution of images across different classes.

| Class | Number of Images |
|-------|-------------------|
| Maniola_jurtina |  900 |
| pyronia_tithonus |  900 |



**Model Accuracy Comparison**

| Model | Accuracy (%) |
|-------|--------------|
| Custom CNN | 76% |
| VGG16 | 75% |


**Insight:**
The table presents the accuracy scores achieved by different models during training and validation. It allows us to compare the performance of each model and identify the most effective one for butterfly image classification.

## 📈 Performance of the Models based on Accuracy Scores<br>
   - Custom CNN Model Accuracy: 76%
   - VGG16 Model Accuracy: 75%
   

## 📢 Conclusion
The butterfly image classification project demonstrates effective learning and categorization across different species. The models show promising accuracy, with [best_model_name] achieving the highest accuracy of XX%. These results indicate the potential of the models for real-world applications in butterfly species identification.

## ✒️ Your Signature
Dipayan Majumder
[GitHub: dipayan22](https://github.com/dipayan22)

