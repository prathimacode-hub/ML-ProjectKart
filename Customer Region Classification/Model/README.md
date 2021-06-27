**GOAL**

The goal is to predict Customer Region.

Dataset can be downloaded from [here](https://www.kaggle.com/balakrishcodes/others?select=Customer.csv)

**WHAT I HAD DONE**

   1. Discussed some major columns on which the category of the customer regions depends.
   2. Handling outliers of diagnosis columns. As, it is very important because at last we're predicting customer regions.
   3. Then I used different classification models present in sklearn to train the model.
   4. Use Correlation coefficients to measure how strong a relationship is between two variables.

**MODELS USED**

    1. Decision Tree
    2. Naive Bayes
    3. Random Forest Classifier

**LIBRARIES NEEDED**

    1. numpy
    2. pandas
    3. seaborn
    4. matplotlib
    5. scikit-learn

**Conclusion**

By using Decision Tree I got
```
   Accuracy of Training Data:  100.0
   Accuracy of Testing Data:  100.0
```
By using Naive Bayes I got
```
   Accuracy of Training Data:  84.68468468468468
   Accuracy of Testing Data:  82.35294117647058
```
By using Random Forest Classifier I got
```
   Accuracy of Training Data:  100.0
   Accuracy of Testing Data:  100.0
```
