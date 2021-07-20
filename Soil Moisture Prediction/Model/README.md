**PROJECT TITLE - Soil Moisture Prediction**
        
<img src = https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/project_viz.png width = '500'>


**GOAL** - The aim of this project is to predict the moisture present in soil.

**WHAT HAVE I DONE**
- Loading datasets
- Exploratory Data Analysis and Visualizations
- Correlations
- Data Preprocessing
    - Performing Feature Scaling using Standard Scaler     
- Splitting the data
- Using Linear Regression
- Using Random Forest Regressor
- Using KNNs
- Using Decision Tree Regressor
-  Using Using XGBoost Regressor
- Hyperparameter Tuning of Random Forest Regressor using RandomisedSearchCV
- Hyperparameter Tuning of Random Forest Regressor using GridSearchCV
- Hyperparameter Tuning of XGBoost Classifier using GridSearchCV


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/viz7.png" width = "400">


**MODELS USED**
- Linear Regression - *Linear Regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting.*
- XGBoost - *Extreme Gradient Boost algorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- KNNs - *An algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- RandomisedSearchCV, GridSearchCV - *To tune the hyperparameters of the regressor models*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/viz3.png" width = "400">

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- plotly
- seaborn
- scikit-learn
- xgboost



<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/viz1.png" width = "400">


**Comparing the models**

- **Random Forest Regressor model**
    - *Train Accuracy: 0.9795332166765373*
    - *Test Accuracy: 0.8890280801421555*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/rf.png" width = "400">

    
- **Linear Regressor model**
    - *Train Accuracy: 0.5041848832473712*
    - *Test Accuracy: 0.5326493426777246*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/linear_rg.png" width = "400">

    
- **KNN Regressor model**
    - *Train Accuracy: 0.902437059019282*
    - *Test Accuracy: 0.8537095608308689*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/knn.png" width = "400">


- **Decision Tree Regressor model**
    - *Train Accuracy: 1.0*
    - *Test Accuracy: 0.831017644524106* 

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/decisiontree.png" width = "400">


- **XGBoost Regressor model**
    - *Train Accuracy: 0.958998725106501*
    - *Test Accuracy: 0.8894250637732644*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/xgb.png" width = "400">



**Comparing the best models after Hypertuning using RandomisedSearchCV and GridSearchCV**


- **Hypertuned Random Forest Regressor using RandomisedSeachCV**
    - *Train Accuracy: 0.9560722468708732*    
    - *Test Accuracy: 0.9020565600627217*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/random_rf.png" width = "400">

 
- **Hypertuned Random Forest Regressor using GridSearchCV**
    - *Train Accuracy: 0.9602558429574107*
    - *Test Accuracy: 0.8955140515099078*

<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/grid_rf.png" width = "400">


- **Hypertuned XGBoost Regressor using GridSearchCV**
     - *Train Accuracy: 0.9602558429574107*
     - *Test Accuracy: 0.8955140515099078* 


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/Soil%20Moisture%20Prediction/Images/hypertuned_xgb.png" width = "400">



**Conclusion**

In this project we have performed a detailed analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. Then a comparative analysis of different ML Regressors have been done to predict moisture present in the soil. After performing the model comparative analysis we can conclude that only the Random Forest Regressor and XGBoost Regressor have performed well. Hypertuning using RandomisedSearchCV anD GridSearchCV have also been done to prevent overfitting and the best testing accuracy achieved is 90.5% by the Hypertuned Random Forest Regressor using RandomisedSeachCV.  

