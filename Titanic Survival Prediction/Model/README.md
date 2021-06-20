
**TITANIC SURVIVAL PREDICTION**

# *GOAL*
Use machine learning to create a model that predicts which passengers survived the Titanic shipwreck


# *DATASET*
The dataset can be found in the link: https://www.kaggle.com/c/titanic/data


# *WHAT HAVE I DONE*

1. Imported the dataset and studied it carefully

2. Checked for the null values and filled them up by taking the mean in case of numerical values and by filling up the null spaces using the data   that was most 
  likely to survive in case of non numerical values.
 
3. Used bar graphs for data visualisation to see the difference between survived and dead passengers with respect to various parameters.

4. Carried out Mapping to convert textual data to numerical data.

5. Dropped of some unnecessary data from the data set which was not required.

6. Trained my model using train dataset 

7. Based on vrious classifiers , figured out which one dives highest accuracy score.

8. Finally ,tested my model using the test dataset.


# *MODELS USED*
The model I used to predict was initially Naive Bayes but since the accuracy score was less, other models used are:

1. Naive Bayes

2. Decision Tree Classifier

3. KNeighborsClassifier

4. Random Forest Classifier

5. Support Vector Machine


# *LIBRARIES NEEDED*
The libraries I used were:

1. Pandas

2. Numpy

3. Sklearn


# *CONCLUSION* 
The classifier which predicted that a particular person would survive or not with the highest accuracy was *Random Forest Classifier*

Accuracies of the models:

1. Naive Bayes: 81.04%
2. Decision Tree Classifier: 80.67%
3. K Neighbors Classifier : 81.13%
4. Random Forest Classifier: 81.48%
5. Support Vector Machine: 81.48%

Then I was able to predict by myself from the test dataset that whether a person would survive or not.

Link to the results:
https://github.com/RHEA211/ML-ProjectKart/tree/main/Titanic%20Survival%20Prediction/Images



