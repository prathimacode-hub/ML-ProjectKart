

# Book Genre Prediction

## Goal
The goal of this project is to make a prediction model which will predict genre of the book. 

## DATASET
The dataset which is used in this project, is CMU Book Summary Dataset. Here is the link of the dataset : http://www.cs.cmu.edu/~dbamman/booksummaries.html. I have uploaded the
same in [`Dataset`](https://github.com/prathimacode-hub/ML-ProjectKart/tree/main/Book%20Genre%20Prediction/Dataset) folder too, you can access that!

## LIBRARIES NEEDED

- Pandas
- Numpy
- Sklearn
- Matplotlib
- nltk 

## WHAT I HAD DONE
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/prathimacode-hub/ML-ProjectKart/blob/main/Book%20Genre%20Prediction/Model/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Loading dataset and cleaning summary data. 
4. Encoding Genre column to convert genre into numbers . 
5. Split dataframe into train and test data. 
6. Encoding all textual data. 
7. Apply different classification models and calculate their accuracy.
8. Choose best model for our prediction which has highest accuracy. 
9. Make the final prediction using best model. 
10. Compare actual genre of the book with predicted genre. 

## Model Comparison
We have deployed 5 machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the efficiency of the models based on the accuracy of each of the models. Now let's take a look at model with their accuracy. 

|Name of the Model|Accuracy|
|:---:|:---:|
|Support Vector Classifier|0.775|
|Decision Tree Classifier|0.43|
|Random Forest Classifier|0.6433|
|Gradient Boosting Classifier|0.6433|
|LightGBM Classifier |0.655|

*****************************************

## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest Classifier Model gives highest accuracy and will provide best prediction.**

Code Contributed by Akash Jain **(@Akash20x)**
