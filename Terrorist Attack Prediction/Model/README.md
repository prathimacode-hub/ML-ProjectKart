 ## Terrorist Attack Prediction
 
 ![is-it-going-to-end-soon](https://github.com/23-24/ML-ProjectKart/blob/23-24-patch-1/Terrorist%20Attack%20Prediction/Images/is-it-going-to-end-soon.jpg)

This modal analyses terrorist attack dataset to findout cities ,regions that are prone to attacks . Earlier prediction on Increased rate of  attack at a region provides sufficient time and efficiency in taking measurements against them.

## Goal
 **Analysis of given dataset and prediction of Terrorist attack using regression modal**

## Dataset
**[https://www.kaggle.com/START-UMD/gtd]**



## PROCEDURE
1.for this project first of all the given dataset was imported  and was preprocessed.

2.The given data contains different missing values which were first preprocessed and a plot of these missing values were made

3.from the large dataset provided the important columns were chosen and their missing values were calculated and plotted
  missing values were filled

4.after making sure that there are no more missing values the datatypes of each colums were analysed 

5.since different columns were of different datatypes the categorical values were converted in to numerical data using LabEncoder() from preprocessing library

6.analysis of assassination attack type was made.country, region and the month of highest attack rate was found

7.United kigdom(country),western Europe(region) and month of september was found with highest attack rates. 

8.Plots depicting the attacks and rates is given

9.the given dataset was splitted in to training and testing dataset

10.Logistic regression model was used to predict the city which is highly prone to terrorist attack

11.the model obtained have an accuracy about 0.09513395297977037(95%)

12.additional models like decision tree and random forest classifier were used.



## IMPORTED LIBRARIES :

 numpy 
 
 pandas
 
 matplotlib
 
 seaborn 

 sklearn
 
 ## DATA VISUALISATION:
 
 
 ### Region with higher Assassination attack rate
 
 ![im2.png](https://github.com/23-24/ML-ProjectKart/blob/23-24-patch-1/Terrorist%20Attack%20Prediction/Images/im2.PNG)
 
 ### Country with higher Assassination attack rate
 
 ![im1.png](https://github.com/23-24/ML-ProjectKart/blob/23-24-patch-1/Terrorist%20Attack%20Prediction/Images/img1.PNG)
 
 ### Month with higher Assassination rate
 
 ![im3.png](https://github.com/23-24/ML-ProjectKart/blob/23-24-patch-1/Terrorist%20Attack%20Prediction/Images/im3.PNG)
 
 ## ATTRIBUTES FROM DATASET FOR PREDICTION
- eventid	
- iyear	
- imonth	
- iday	
- extended	
- country	
- country_txt	
- region	
- region_txt	
- provstate
 
## MODELS USED
 
 LogisticRegression
 
 RandomForestClassifier
 
 DecisionTreeClassifier
 
 # Accuracy obtained
 
 Logistic regression :0.09513395297977037
 
 Random Forest Classifier:0.6036085292509568
 
 Decision Tree Classifier:0.589939857845817

## Conclusion

from the three models comparison it is clear that logistic regression provided better prediction.
using different attributes such as month,year,date etc for previous occurances of each attack type ,we could predict upcoming terrorist attacks in different regions
country and month of future attacks.This modal is able to predict the cities which is highly prone to attacks using the attribute given above.


## Author

code contributed by Archana.M 2021 @23-24 #LGM SOC21

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
