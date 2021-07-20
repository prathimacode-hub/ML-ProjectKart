**PROJECT TITLE - Glass Classification**
        
<img src = https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Glass%20Classification/Images/project_viz.png width = '500'>


**GOAL** - The aim of this project is to classify the glass type using percentage of minerals present in each class of glass

**WHAT HAVE I DONE**
- Loading datasets
- Features in data
- Exploratory Data Analysis and Data Pre-processing
    - Checking distribution of the features
    - Univariate Box Plot
    - Bivariate Box plots
    - Scatter Matrix
    - Pairplot
    - Correlation Plot
- Feature Engineering - Based on the mean of K and Ca in classes
- Statistical Importance Check for Variable
- Splitting the data¶
- Model Building and Comparison Analysis
    - Using Logistic Regression
    - Using Random Forest Classifier
    - Using Gradient Boost
    - Using Decision tree Classifier
    - Using KNN
    - Using Support Vector Classifier
- Saving the Random Forest Classifier model
#### Making classification using the Keras Sequential Model approach
- Data Pre-processing
- Building the Keras model
- Building the Keras model accuracy
- Model evaluation
- Saving the Keras model


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Glass%20Classification/Images/scatterplot.png" width = "700">


**MODELS USED**
- Logistic Regression
- Random Forest Classifier
- Gradient Boost
- Decision tree Classifier
- KNN
- Support Vector Classifier
- Keras Sequential Model


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Glass%20Classification/Images/boxplots.png" width = "700">

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- scipy
- seaborn
- scikit-learn
- pickle
- tensorflow

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Glass%20Classification/Images/skweness.png" width = "700">


**Comparing the models**

- **Logistic Regressor model**
    - *Accuracy Score of Logistic Regression : 0.6976744186046512*

- **Random Forest Classifier model**
    - *Accuracy Score of Random Forest Classifier : 0.8372093023255814*
    
- **Gradient Boost classifier model**
    - *Accuracy Score of Gradient Boosting Classifier : 0.7906976744186046*


- **Decision Tree Classifier model**
    - *Accuracy Score of Decision Tree Classifier : 0.5581395348837209* 


- **KNN Classifier model**
    - *Accuracy Score of K-Nearest Neighbors Classifier :  0.813953488372093*


- **Support Vector Classifier model**
    - *Accuracy Score of Support Vector Classifier : 0.7441860465116279*  


#### From the model comparison it is evident that the Random Forest Classifier gives the best results with a score of 83.72%.Now, we are going to build a Keras Sequential model to check whether it performs better than the Random Forest Classifier.

- **Keras Sequential Model**
    -  *Validation Accuracy - 95.24%*
    -  *Testing Accuracy - 90.91%*



<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Glass%20Classification/Images/corr_plot.png" width = "500">



**Conclusion**

In this project we have performed a analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. Then a comparative analysis of different ML Classifiers have been done to predict type of glass. After performing the comparative analysis of the classifiers, we can see that the Random Forest Classifier gives the best results with a score of 83.72%. However to get better accuracy we build a Keras Sequential model which gives a validation accuracy of 95.24% and Testing accuracy of 90.91%.   

