**GOAL**

The goal is to perform analysis and predict Followers gained per stream.

Dataset can be downloaded from [here](https://www.kaggle.com/aayushmishra1512/twitchdata)

**WHAT I HAD DONE**
- Done analysis of Twitch data
- Discussed some major columns on which followers gained depends.
- Handling outliers of diagnosis columns. As, it is very important because at last we're predicting followers gained.
- Then I used different Regression models present in sklearn to train the model.
- Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**
-  Linear Regression
-  Decission Tree Regressor
-  Random Forest Regressor

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn

**CONCLUSION**

By using Linear Regression I got 
 ```
    Accuracy of training data: 53.69612929734367
    Accuracy of testing data: 53.29426334264469
 ``` 

By using Decission Tree Regressor I got 
 ```
    Accuracy of training data: 83.1597328505062
    Accuracy of testing data: 58.87655619841754
 ``` 

 By using Random Forest Regressor I got 
 ```
    Accuracy of training data: 89.73371716934986
    Accuracy of testing data: 63.58769967999709
 ``` 


As accuracy of **Random Forest Regressor** algorithm is more ie. **63.58%** ~ **64%**

Hence this model is selected.


<img align="center" alt="acc"  src="https://github.com/Jagannath8/ML-ProjectKart/blob/twitch/Twitch%20Streamer%20Analysis/Images/accuracy.png" />


<a href="https://github.com/Jagannath8">Jagannath Pal</a>
