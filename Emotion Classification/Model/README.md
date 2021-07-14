# Emotion Classification
The classification of emotion varies according to the researchers, the general basic emotion found in most research studies includes happy, sad, anger, fear, disgust, surprise, where these emotions were based on a two-dimensional plane commonly called the valence-arousal plane. Positive emotions can be categorized as happiness or surprise, while negative emotions can be associated with sadness, anger, fear, and disgust. Emotional stress may be influenced by negative experiences over a long and continuous period. Emotion classification can be divided into two classes, primary emotion such as joy, sadness, anger, fear disgust, and surprise, and secondary emotion, which evokes a mental image that correlates to memory or primary emotion.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-38/Emotion%20Classification/Images/107360-byxhzxvmlb-1544009839.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/anjaneyatripathi/emotion-classification-nlp?select=emotion-labels-train.csv. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-38/Emotion%20Classification/Dataset) folder too, you can access that!

## Goal
The goal of this project is to create a model which will classify different emotions based on the text provided in the dataset.
************************************

## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-38/Emotion%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Cleaning
4. Data Exploration
5. Creating the Baseline
6. Text Tokenizer Comparison
7. Data Preprocessing
8. Deploying Models
    - KNN Classifier
    - Linear Support Vector Machine Classifier
    - Random Forest Classifier
9. Error Analysis
10. Hyper Parameter Tweaking
11. Model Comparison
12. Conclusion 

*************************************
## Data Visualization
1. **Ratio of different labels in the dataset**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-38/Emotion%20Classification/Images/em1.png)

2. **Vectorizer Model to the Dataset**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-38/Emotion%20Classification/Images/em3.png)
**************************************
## Error Analysis
- **Error analysis of all the deployed models**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-38/Emotion%20Classification/Images/em2.png)

**************************************
## Final Model Comparison
We have deployed three machine learning models and created the final model structure. Now lets check the accuracy of the models.

|Model|Accuracy Score|
|---|---|
|KNN Classifier|0.39|
|Random Forest Clasifier|0.83|
|Linear SVC|0.83|

Best Classifier Model here, **Random Forest Classifier and Linear SVC**, *with accuracy score of 0.83*.

But here we are going with a single model, based on the baseline score and tokenizer score, **Random Forest Classifier** is the best model in this case and we'll be going with this model.

After hyper parameter tweaking the **Random Forest Classifier** is having the accuracy score of 0.84!
**************************************

## Conclusion
1. For creating the baseline model, Linear SVC is showing the accuracy of 0.84. Although the Random Forest classifier was not far behind, it is also having the score of 0.82.
2. For Tokenizer model the Random Forest Classifier is having the accuracy of 0.74, but the Linear SVC is showing a poor accuracy score.
3. Final model was created by Random forest classifier and it provides the accuracy of 0.83.
4. After Hyper-parameter tweaking the Random Forest classifier improves its accuracy and the score is 0.84.
5. The best model for this dataset and for this classification model is **Random Forest Classifier on Grid Search on 5-fold Cross Validation**.
*******************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
