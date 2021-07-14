# Campus Recruitment - Analysis and Prediction
Campus recruitment is a strategy for sourcing, engaging and hiring young talent for internship and entry-level positions. College recruiting is typically a tactic for medium- to large-sized companies with high-volume recruiting needs, but can range from small efforts (like working with university career centers to source potential candidates) to large-scale operations (like visiting a wide array of colleges and attending recruiting events throughout the spring and fall semester). Campus recruitment often involves working with university career services centers and attending career fairs to meet in-person with college students and recent graduates. Some industries participate in campus recruiting more than others; finance, technology, business consulting, manufacturing and engineering are a few of the most popular.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Images/camp13.jpg)

## Dataset
The dataset is collected from Kaggle website. Here is the link for the dataset : https://www.kaggle.com/benroshan/factors-affecting-campus-placement?select=Placement_Data_Full_Class.csv. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Dataset) folder too, you can access that!

## Goal
The goal of this project is to analyze the factors that can effect the Campus Recruitment, and also creating a model which will predict the chances of getting placed depending on various factors.

## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/requirements.txt.)
2. Upload the dataset and the Jupyter Notebook file.
3. Data wrangling
    - Gender
    - ssc
    - hsc
    - work experience
    - specialization
    - status
4. Data Visualization
    - Gender vs Placed
    - Scores vs Placed
    - High School stream
    - Salary
5. Prediction Models
    - KNN Classifier
    - Logistic Regression
    - Random Forest Classifier
    - Support Vector Machine Classifier
    - XgBoost Classifier
6. Model Comparison
7. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Seaborn
5. Sklearn
6. XgBoost

## Data Visualization
1. **Gender vs Placed Candidates**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Images/camp1.png)

2. **10th Board Score vs Placed Candidates**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Images/camp2.png)

3. **12th Board Score vs Placed Candidates**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Images/camp3.png)

4. **UG Percentage distribution vs Placement**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Images/camp4.png)

### For more visualization, check out the [`Images`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-29/Campus%20Recruitment%20-%20Analysis%20and%20Prediction/Images) folder!

******************************************************

## Model Comparison
We have deployed five machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|KNN Classifier|0.77|
|Logistic Regression|0.77|
|Random Forest Classifier|0.78|
|Support Vector Machine Classifier|0.77|
|XgBoost Classifier|0.79|

**Comparing all those scores scored by the machine learning algorithms, it is clear that XgBoosting Classifier is having the upper hand in case of this dataset and after this, we can use Random Forest Classifier, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. XgBoost Classifier
2. Random Forest Classifier
3. KNN Classifier
4. Logistic Regression
5. Support Vector Machine Classifier

*************************************

## Conclusion
1. As it can be seen, **high percentage of male candidates got placed**. On the other hand, comparitively lower number of female candidates got placed. This is expected as male candidates are generally higher in most brances. Hence, their chances of getting placed is normally higher as well. Let us check the male to female ratio of this branch.

2. The M/F ratio is approximately 2. This can be interpreted as for every 1 female candiate, there are 2 male candiates sitting for placements. **Males outperformed the female candidates in the batch.**

3. All students scoring 80-100% in 10th grade got placed. **Most students in 60-80% range did get placed** while maximum students below 60% **in 10th standard** couldn't get placed. It shows that generally, a student who has done well in 10th grade is more likely to get placed.

4. Almost entire students with 80-100 % got placed. **Most students in 60-80 % range also got placed**. Just like in the case of 10th boards, most students could not get placed in the 0-60 % range.

5. Upon studying the MBA percentage data, we can see that more students from percentage class 2 got placed as opposed to class 3. However, the difference is not as high as for board and UG percentages. Hence, we can say that MBA percentage is not as big as a factor. This could be because MBA is a branch that places much more importance on speaking skills, internships, case studies, etc rather than academic scores. Hence, the play is much more level fielded in this case.

6. **Maximum students enrolled in the program were either from commerce or science background. Very few students were from Arts background.**

7. For 10th Board, the placement ratio for each of the boards is similar. Hence, **we could say that 10th board of examination doesn't hold much value towards placement.**

8. Unlike the case for 10th board, more students opted for state boards in their 12th examinations. The performance of state board students was better as more students from state board of 12th were placed. However, the placed/unplaced ratio for both is nearly identical once again. Hence, **12th board is not playing a significant role once again.**

9. **Majority of the packages will be in the region of 2-4 LPA.**

10. For the prediction model, the best fitted algorithm is **XgBoost Classifier Algorithm** with an accuracy score of 0.79.

*****************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
