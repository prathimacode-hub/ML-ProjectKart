**Stress Level Prediction**

**GOAL**

The goal of this project is to predict stress level from features taken from the survey responses.The survey questions included 

How many events have you Volunteered in ?,

How many events have you Participated in ?,

How many activities are you Interested in ?,
        
How many activities are you Passionate about ?,
        
How Satisfied You are with your Student Life ?',

How much effort do you make to interact with others ?,

About How events are you aware about ? 

**DATASET**

Dataset can be downloaded from [here](https://www.kaggle.com/shivamb/ideal-student-life-survey?select=survey_responses.csv).

**WHAT I HAD DONE**
- Step 1: Data Exploration
- Step 2: Data Cleaning
- Step 3: Data Visualization
- Step 4: Data Training
- Step 5: Model Creation
- Step 6: Performance Evaluation


**MODELS USED**
-  Decision Tree Regressor
-  Random Forest Regressor
-  Ridge Regression



**LIBRARIES NEEDED**
- pandas
- numpy
- matplotlib
- seaborn
- sklearn (For data traning, importing models and performance check)



**CONCLUSION**

 - By using Decision Tree Regressor model 
 ```python
    Accuracy achieved :  72.49
 ``` 
 - By using Random Forest Regressor model 
 ```python
    Accuracy achieved :  64.63
 ``` 
  - By using Ridge Regression model 
 ```python
    Accuracy achieved :  14.09
 ``` 
* Decision Tree Regressor has more accuracy  when compared to random forest regressor and ridge regression.
