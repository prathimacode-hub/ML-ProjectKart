**PROJECT TITLE - Human Activity Recognition using Smartphones**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/project_viz.png"  width="800">



**GOAL** - The aim of this project is to build a model that predicts the human activities such as Walking, Walking_Upstairs, Walking_Downstairs, Sitting, Standing or Laying using data recorded by multiple smartphone sensors.

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/data_imbalance_plot.png"  width="400">



**DATASET INFO** = This dataset is collected from 30 persons(referred as subjects in this dataset), performing different activities with a smartphone to their waists. The data is recorded with the help of sensors (accelerometer and Gyroscope) in that smartphone. This experiment was video recorded to label the data manually. 

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/feature_dist30_40.png"  width="400">



**WHAT HAVE I DONE**

 **Exploratory Data Analysis**

- Loading the datasets
- Cleaning the data
  - Check for Duplicates
  - Checking for NaN/null values
  - Checking for data imbalance
  - Analysis of the activity feature to understand how many types of activites have been performed
  - Cleaning the feature names for an easy understanding
- Saving the new dataframes with cleaned feature names in csv files¶
- Exploratory Data Analysis
  - Visualization of the Stationary and Moving activities
  - Maximizing the Static and Dynamic activities plots
  - Visualization of the magnitude of acceleration data captured by the accelerometer sensor of the smartphone
  - Visualizing the position of GravityAccelerationComponants data captured by the gyroscopic sensor of the smartphone
  - Visualizations for feature distribution in space.
  - Visualizations with stripplot
- Apply t-sne on the data

  **ML CLASSIFIERS approach**
  
  - Importing libraries
  - Loading the cleaned datasets
  - Defining a function to plot the confusion matrix
  - Defining a generic function to run any model specified
  - Defining a function to print the gridsearch Attributes for Hypertuning the model
  - Logistic Regression with GridSearchCV
  - Linear SVC with GridSearch
  - Decision Trees with GridSearchCV
  - Comparing all models
  - Getting predictions using the Hypertuned Logistic regression model
  - Getting predictions using the Hypertuned Linear SVC model
  
  
 **Artificial Neural Network(ANN) approach**
 
 - Loading datsets
 - Pre-processing and data preparation to feed data into Artificial Neural Network.
    - Feature Scaling
    - Using Principle Component Analysis(PCA) approach for Dimensionality Reduction
 = Building the ANN Model
 = Saving the model


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/tSNE_final.png"  width="400">


**MODELS USED**

- **Artificial Neural Network** - *Artificial neural networks (ANNs) use learning algorithms that can independently make adjustments - or learn, in a sense - as they receive new input. This makes them a very effective tool for non-linear statistical data modeling.* 

- **Logistic Regression** - *Logistic Regression is a machine learning (ML) algorithm for supervised learning – classification analysis. Within classification problems, we have a labeled training dataset consisting of input variables (X) and a categorical output variable (y).*

- **Linear SVC** - *The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a "best fit" hyperplane that divides, or categorizes, the data*

- **Decision Tree** = *Decision tree algorithm falls under the category of supervised learning. They can be used to solve both regression and classification problems. Decision tree uses the tree representation to solve the problem in which each leaf node corresponds to a class label and attributes are represented on the internal node of the tree.*

**Comparative Analysis of the Models**

- **Logistic Regression**

    *Accuracy - 95.52%*
    
    <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/lg_matrix.png"  width="400">
    
    
- **Linear SVC**
- 
     *Accuracy - 96.71%*
     
     <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/svc_matrix.png"  width="400">
     
     
- **DEcision Trees**
- 
     *Accuracy - 86.46%*
     
     <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/dt_matrix.png"  width="400">
     
 
- **Artificial Neural Network(ANN)*
- 
     *Accuracy - 85.00%*
     
     <img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/ann_matrix.png"  width="400">
     
     
 **Therefore we can conclude that the Linear SVC model outperforms all the other model approaches with a accuracy of 96.71%**


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/StaticvsMoving_plot.png"  width="500">



**LIBRARIES NEEDED**

- pandas
- matplotlib
- numpy
- tensorflow
- itertools
- datetime
- pickle
- os
- keras
- scikit learn


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Human%20Activity%20Recognition%20using%20Smartphones/Images/gyroscopic.png"  width="400">


**Conclusion**

In this project we have first tried to understand the training and testing data using different Exploratory Data Analysis techniques and visualizations. Then we have tried to implement some classical machine learning algorithms and deep learning frameworks to train models and observe how each model perform. After performing all these operations, we see that the  Linear SVC model performs best among all the other models.
