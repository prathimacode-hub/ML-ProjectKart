# GOT Episodes IMDb Rating Prediction
A Game of Thrones is the first novel in A Song of Ice and Fire, a series of fantasy novels by the American author George R. R. Martin. It was first published on August 1, 1996. The novel won the 1997 Locus Award and was nominated for both the 1997 Nebula Award and the 1997 World Fantasy Award. The novella Blood of the Dragon, comprising the Daenerys Targaryen chapters from the novel, won the 1997 Hugo Award for Best Novella. In January 2011, the novel became a New York Times Bestseller and reached No. 1 on the list in July 2011.

In the novel, recounting events from various points of view, Martin introduces the plot-lines of the noble houses of Westeros, the Wall, and the Targaryens. The novel has inspired several spin-off works, including several games. It is also the namesake and basis for the first season of Game of Thrones, an HBO television series that premiered in April 2011. A March 2013 paperback TV tie-in re-edition was also titled Game of Thrones, excluding the indefinite article "A".

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/Images/got3.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/bakar31/game-of-thronesgot. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/Dataset) folder too, you can access that!


## Goal
The goal of this project is to create a prediction model which will predict the IMDb ratings of the episodes of the Game of Thrones series depending on the views and season of the GOT.

******************************************************
## What have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Cleaning
4. Data Visualization
5. Prediction Models
    - Spliting the dataset into 75:25 ratio
    - Deploying the models
        - Linear Regression
        - Decision Tree Regression
        - Random Forest Regression
        - Lasso Regression
        - Ridge Regression
        - MLP Regression
        - XgBoost Regression
        - Gradient Boosting Regression
        - Support Vector Regression
6. Comparing the accuracy of the models
7. Conclusion

****************************************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn
5. Seaborn
6. XgBoost
********************************************
## Data Visualization
1. **IMdB Rating less than or equals to 8**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/Images/got1.png)

2. **Unique Directors**

```
array(['Tim Van Patten', 'Brian Kirk', 'Daniel Minahan', 'Alan Taylor',
       'Alik Sakharov', 'David Petrarca', 'David Nutter', 'Neil Marshall',
       'David Benioff', 'Alex Graves', 'Michelle MacLaren', 'D. B. Weiss',
       'Michael Slovis', 'Mark Mylod', 'Jeremy Podeswa',
       'Miguel Sapochnik', 'Daniel Sackheim', 'Jack Bender',
       'Matt Shakman', 'David Benioff & D. B. Weiss'], dtype=object)
```

3. **Unique sources**

```
array(['A Game of Thrones', 'A Clash of Kings', 'A Storm of Swords',
       'A Feast for Crows, A Dance with Dragons and original content',
       'Outline from The Winds of Winter and original content ',
       'Outline from A Dream of Spring and original content '],
      dtype=object)
```

4. **Plotting the graph based on the views achieved by the show**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-35/GOT%20Episodes%20IMDb%20Rating%20Prediction/Images/got2.png)

*******************************************************
## Comparative analysis among the algorithms for this project

We have deployed nine machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Linear Regression|0.21|
|Decision Tree Regressor|0.13|
|Random Forest Regressor|0.29|
|Lasso Regression|0.18|
|Ridge Regression|0.21|
|XgBoost Regressor|0.21|
|MLP Regressor|-7.07|
|Gradient Boosting Regressor|0.14|
|Support Vector Regressor|0.25|
************************************************
## Conclusion

**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest Regressor is having the upper hand in case of this dataset and after this, we can use Support Vector Machine Regressor which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Random Forest Regressor
2. Support Vector Machine Regression
3. Linear Regression
4. XgBoost
5. Ridge
6. Lasso
7. Gradient Boosting
8. Decision Tree Regression
9. MLP regressor


Hooray!! The models are deployed successfully!

*****************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
