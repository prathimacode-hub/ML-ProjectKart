**GOAL**

The goal is to predict Profit of the Startups.
The dataset contains data about 50 startups. It has 5 columns: “R&D Spend”, “Administration”, “Marketing Spend”, “State”, “Profit”.

The first 3 columns indicate how much each startup spends on Research and Development, how much they spend on Marketing, and how much they spend on Administration cost.
The state column indicates which state the startup is based in and the last column states the profit made by the startup.

Dataset can be downloaded from [here](https://www.kaggle.com/karthickveerakumar/startup-logistic-regression)

**BACKEND**

<img align="center" alt="output"  src="https://raw.githubusercontent.com/Jagannath8/ML-ProjectKart/startup/Startup%20Profit%20Prediction/Images/deploy.jpg" />

**ACCESS**

https://startup-pred.herokuapp.com


**WHAT I HAD DONE**
- Discussed some major columns on which Profit depends.
- Handling outliers of diagnosis columns. As, it is very important because at last we're predicting Profit of Startup.
- Then I used different Logistic Regression model present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.
- Created Backend for our model.
- Deployed the model in Heroku.

**MODELS USED**
-  Logistic Regression

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn

**CONCLUSION**
By using Logistic Regression I got 
 ```
    Accuracy of training data: 93.83444814482027
    Accuracy of testing data: 99.17459017235682
 ``` 
 

<img align="center" alt="output"  src="https://raw.githubusercontent.com/Jagannath8/ML-ProjectKart/startup/Startup%20Profit%20Prediction/Images/img.png" />

<a href="https://github.com/Jagannath8">Jagannath Pal</a>
