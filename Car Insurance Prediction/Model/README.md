
# Car Insurance Problem-


Road traffic accidents claim the lives of about 1.35 million people per year. For children and young adults aged 5 to 29, road traffic accidents are the leading cause of death.Therefore, in most countries, for the sake of safety and protection, the law has made so its mandatory for all vehicle owners to have vehicle insurance.

## GOAL

The goal of the project is to do Exploratory Data Analysis to  visualise do the analysis and make the car insurance predictions  using the best fit  Ml Algorithms.

## DATASET
You can have dataset from Dataset folder also it is availbale on kaggle 
Link to the dataset= https://www.kaggle.com/infernape/fast-furious-and-insured

## WHAT I HAD DONE-
I have load necessary libraries, preprossed data and build a model that predicts the insurance claim of the cars that are provided in the dataset.I have build random forest regression model
1.Loading required packages
2.Loading training data
3.Loading testing data
4.Exploratory Data Analysis
4.Pre-processing
5.Label encoding and scaling
6.Train a random forest regressor
7.CatBoostRegressor
8.XGBoost
9.Transfer learning with MobileNet
10.Getting the test prediction


## Algorithms or models used in this project 

- Random Forest Regression
- StandardScaler
- OneHotEncoder
- Mobile-Net
- CatBoostRegressor
- XGBoost

## LIBRARIES NEEDED

sklearn==0.0
Numpy==1.19.2
pandas==1.2.4
matplotlib==3.4.2
Tensorflow==1.14.0
Keras==2.4.3
os



## MODELS and Accuracy Scores :
 XGBoost : 94%
 RandomForestRegressor-99%
 CatBoostRegressor-98.5%

## CONCLUSION
It can be concluded from the model that all the preprocessing techniques and the  Random Forest Regression works really well on the data.The data was higly imbalanced and the image of damaged vehicles wer not also good, howsoever transfer learning works well and also  data was label encoded so as to assign a numeric value to a categorical value. The data was also normalissed using the standard StandardScaler.Also the Exploratory Data Analysis done on the data gives us various insights about the data which would be greately usfull for the future predictions.So we get a good accuracy and training score of about 99 % using RandomForestRegressor


## Done by
Somasree Majumder

