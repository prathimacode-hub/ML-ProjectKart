**GOAL**

The goal is to predict radiation of Sun.

    There are 5 variables that are of numeric structure: Temperature, Pressure, Humidity, WindDirection(Degrees), Speed

    There is 1 variable that has an float structure: Radiation

Dataset can be downloaded from [here](https://www.kaggle.com/dronio/SolarEnergy?select=SolarPrediction.csv)

**BACKEND**

<img align = "center" alt = "acc" src = "https://github.com/anishamurmu13/ML-ProjectKart/blob/solar/Solar%20Radiation%20Prediction/Images/output.png"/>

**ACCESS**

https://solar-radiation-pred.herokuapp.com

**WHAT I HAD DONE**

    1. Discussed some major columns on which radiation of Sun depends.
    2. Handling outliers of diagnosis columns. As, it is very important because at last we're radiation of Sun.
    3. Then I used different Linear Regression model present in sklearn to train the model.
    4. Use Correlation coefficients to measure how strong a relationship is between two variables.
    5. Created Backend for our model.
    6. Deployed the model in Heroku.

**MODELS USED**

    Linear Regression
    Decision Tree Regressor
    KNN Regressor

**LIBRARIES NEEDED**

    numpy
    pandas
    seaborn
    matplotlib
    scikit-learn
    
**Conclusion**

By using Linear Regression I got
```
   Accuracy of Training Data:  56.50680254695581
   Accuracy of Testing Data:  56.78128871445479
```
By using Decision Tree Regressor I got
```
   Accuracy of Training Data:  66.61756372459058
   Accuracy of Testing Data:  66.6854677492044
```
By using KNN Regressor I got
```
   Accuracy of Training Data:  77.75923134849062
   Accuracy of Testing Data:  72.79401759176586
```
Hence, **KNN Regressor has the Highest Accuracy** i.e., **72.79%**.
Therefore, this model is selected.

<img align = "center" alt = "acc" src = "https://github.com/anishamurmu13/ML-ProjectKart/blob/solar/Solar%20Radiation%20Prediction/Images/accuracy.png"/>
