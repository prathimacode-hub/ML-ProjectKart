**PROJECT TITLE - Airline Passenger Satisfaction**
        
<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Airline%20Passenger%20Satisfaction/Images/project_viz.png" width = '500'>


**GOAL** - The aim of this project is to perform analysis of the passenger satisfaction data and data preprocessing to prepare the data and predict whether the passenger is satisfied or not with the airline services.

**WHAT HAVE I DONE**
- Loading datasets
- Imbalance check
  - Transform the satisfaction string category to numerical category for the imbalance check
- Dealing with Null values
- Numeric Columns Analysis
- Continuous Numeric Columns Analysis
- Categorical columns analysis
- Check the correlation between columns in the data
   - Correlation with the age
   - Correlation with the gender
- Visualizing the 'Type of Travel' column
- Data Preprocessing
    - Dealing with Null values¶
    - Using Log Transformation to transform the data to normally distributed data¶
    - Encode string categorical column into numeric using Indexing
    - Feature Scaling using MinMax Scaler
    - Column filtering
- Splitting the data
- Comparative model Analysis
- Random Forest Classifier 
    - Checking the amount of overfitting and underfitting occured in the model
    - Hyperparameter using RandomizedsearchCV
- Support Vector Classifier
    - Tweaking the parameters of Support Vector Machine
    - Drawing up the conclusion
- Saving the best models 
- Loading the test dataset
- Loading the saved models
- Performing predictions on the test data
- Saving the predictions in .CSV files

**MODELS USED**


- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- SVC - a nonparametric clustering algorithm that does not make any assumption on the number or shape of the clusters in the data.

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- seaborn
- pickle
- scikit-learn


**Comparative Model Analysis**

- **LogisticRegression()**
    - accuracy - 0.885087	
    - precission - 0.869842

- **RidgeClassifier(alpha=0.005)**
    - accuracy - 0.884991	
    - precission - 0.870149

- **KNeighborsClassifier()**
    - accuracy - 0.931187	
    - precission - 0.950513

- **RadiusNeighborsClassifier()**
    - accuracy - 0.903662
    - precission - 	0.929150

- **DecisionTreeClassifier()**
    - accuracy - 0.936432	
    - precission - 0.922373

- **Random Forest Classifier()**
    - accuracy - 1.000000	
    - precission - 0.970488

- **Hypertuned Random Forest Classifier()**
    - accuracy - 0.995865	
    - precission - 0.971519

- **SVC()**
    - accuracy - 0.960153	
    - precission - 0.958689

- **Hypertuned SVC()**
    - accuracy -0.971735	
    - precission - 0.965722



**Conclusion**

In this project we have performed a detailed analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. Then a comaparative analysis of different Classifier models have been done to predict the passenegr satisfaction class. After performing the model comparative analysis we can conclude that the Random Forest Classifier and the Support Vector classifier have performed better. HYpertuning on both of these classifiers have been done to reduce overfitting and achieve an improved accuracy of 97.15% and 96.57% respectively.  

