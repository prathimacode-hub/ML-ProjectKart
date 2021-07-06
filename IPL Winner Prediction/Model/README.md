**PROJECT TITLE - IPL Winner Prediction**
        
<img src = https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/IPL%20Winner%20Prediction/Images/project_viz.png width = '500'>


**GOAL** - The aim of this project is to perform analysis of the IPL data and predict the winner of the IPL matches.

**WHAT HAVE I DONE**
- Loading datasets
- Exploratory Data Analysis and Visualizations
    - Number of matches played in each IPL season¶
    - Most wins in the Eliminator
    - Team which has won maximum Tosses
    - Team with maximum Match Winnings
    - Team which has won both Toss and the MatResult margin analysis
    - Total matches won by the all the teams
    - Understanding the Toss Decision trend
    - Preferred Toss decision
    - Matches Played, Wins and Win Percentage by each Team
    - Result margin analysis
    - Win basis pie chart
    - Performance of teams with respect to Win basis
    - Whether the team has won or lost on the basis of their toss decision
- Data Preprocessing
    - Replacing with proper team names
    - Renaming the Eliminator Column
    - Filling null values wirh median value
    - Changing into Datetime format
    - Replacing team names with codes
    - Encoding the Teams in specific numeric codes
    - Label encoding the categorical columns having ordinal data
    - Perfroming One Hot Encoding on categorical columns having nominal data   
    - Concatinating the one hot encoded daatset with the training dataset
    - Dropping the unnecessary columns
    - Performing Feature Scaling using Standard Scaler     
- Splitting the data
- Using Logistic Regression
- Using Random Forest Classifier
- Using Using XGBoost classifier
- Using GaussianNB
- Using KNNs
- Using SVMs
- Using Decision Tree Classifier
- Hyperparameter Tuning of Random Forest Classifier using RandomisedSearchCV
- Hyperparameter Tuning of Random Forest Classifier using GridSearchCV
- Saving the predictions of the the hypertuned Random Forest Classifier in CSV file
- Hyperparameter Tuning of XGBoost Classifier using GridSearchCV
- Saving the predictions of the the hypertuned XGBoost Classifier in CSV file
- Visualization of the predicted winners


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/IPL%20Winner%20Prediction/Images/viz1.png" width = "800">


**MODELS USED**
- Logistic Regression - *Logistic regression is a statistical analysis method used to predict a data value based on prior observations of a data set. Logistic regression has become an important tool in the discipline of machine learning.*
- XGBoost - *eXtreme Gradient Boost algorithm is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.*
- Decision Tree - *This algorithm works on the basis of creating tree structures to take decisions*
- KNNs - *An algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.*
- Random Forest - *This algorithm works on the concept of emsemble learning.It used bagging technique to train multiple predictors on the same sampled instances to achieve a higher degree of accuracy.*
- GaussianNB - *A Gaussian Naive Bayes algorithm is a special type of NB algorithm. It’s specifically used when the features have continuous values. It’s also assumed that all the features are following a gaussian distribution i.e, normal distribution*
- SVMs - *A support vector machine (SVM) is machine learning algorithm that analyzes data for classification and regression analysis. SVM is a supervised learning method that looks at data and sorts it into one of two categories. An SVM outputs a map of the sorted data with the margins between the two as far apart as possible.*


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/IPL%20Winner%20Prediction/Images/viz2.png" width = "800">

**LIBRARIES NEEDED**
- numpy
- pandas
- matplotlib
- plotly
- seaborn
- scikit-learn
- datetime
- xgboost
- pickle


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/IPL%20Winner%20Prediction/Images/viz3.png" width = "800">


**Comparing the models**

- **Random Forest Classifier model**
    - *Train Accuracy: 1.0*
    - *Test Accuracy: 0.6639344262295082*
    
- **Logistic Regressor model**
    - *Train Accuracy: 0.29401408450704225*
    - *Test Accuracy: 0.2581967213114754*
   
- **GaussianNB model**
    - *Train Accuracy: 0.13204225352112675*
    - *Test Accuracy: 0.10245901639344263* 
    
- **KNN Regressor model**
    - *Train Accuracy: 0.6584507042253521*
    - *Test Accuracy: 0.3319672131147541*

- **Decision Tree Classifier**
    - *Train Accuracy: 1.0*
    - *Test Accuracy: 0.5286885245901639* 

- **Using SVM Classifier model**
    - *Train Accuracy: 0.8697183098591549*
    - *Test Accuracy: 0.4385245901639344* 


- **XGBoost Classifier model**
    - *Train Accuracy: 1.0*
    - *Test Accuracy: 0.6270491803278688*


**Comparing the best models after Hypertuning using RandomisedSearchCV and GridSearchCV**

- **Hypertuned Random Forest Classifier using RandomisedSeachCV**
    - *Train Accuracy: 0.9665492957746479*    
    - *Test Accuracy: 0.6311475409836066*
 
- **Hypertuned Random Forest Classifier using GridSearchCV**
    - *Train Accuracy: 1.0*
    - *Test Accuracy: 0.6557377049180327*

- **Hypertuned XGBoost Classifier using GridSearchCV**
     - *Train Accuracy: 0.9964788732394366*
     - *Test Accuracy: 0.6639344262295082* 


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/IPL%20Winner%20Prediction/Images/viz4.png" width = "800">




**Visualization of the Predicted Winners in IPL matches**


<img src = "https://github.com/Soumayan-pal01/ML-ProjectKart/blob/main/IPL%20Winner%20Prediction/Images/viz5.png">


**Conclusion**

In this project we have performed a detailed analysis and visualization of the training dataset with different Exploratory Data Analysis techniques. Then a comaparative analysis of different ML Classifiers have been done to predict the winners of the IPL matches. After performing the model comparative analysis we can conclude that only the Random Forest Classifier and XGBoost Classifier have performed well. Hypertuning using RandomisedSearchCV anD GridSearchCV have also been done to prevent overfitting and the best testing accuracy achieved is 66.4% 

