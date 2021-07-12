 ## TERRORIST ATTACK PREDICTION
 ![is-it-going-to-end-soon](https://user-images.githubusercontent.com/72660504/124961744-783eb580-e03b-11eb-9eac-cc9d08b13708.jpg)


## Goal
 **Analysis of given dataset and prediction of Terrorist attack using regression modal**

## Dataset
**[https://www.kaggle.com/START-UMD/gtd]**



## PROCEDURE
1.for this project first of all the given dataset was imported and preprocessed using Data preprocessing techniques

2.The given data contains different missing values which were first preprocessed and a plot of these missing values were made

3.from the large dataset provided the important columns were chosen and their missing values were calculated and plotted
  missing values were filled

4.after making sure that there are no more missing values the datatypes of each colums were analysed 

5.since differentcolumns were of different datatypes the categorical values were converted in to numerical data using LabEncoder() from preprocessing library

6.analysis of assassination attack type was made .country, region and the month of highest attack rate was found

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
 
## MODELS USED
 
 LogisticRegression
 
 RandomForestClassifier
 
 DecisionTreeClassifier

