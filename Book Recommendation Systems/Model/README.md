# Book Recommendation Systems
Machine learning is a scientific study of statistical model and algorithms. In this project I will use the machine learning algorithms, K-NN and matrix factorization. In the books recommendations system BX books dataset is used. Suggestion method is a selection strategy which was used for collective selection and material-based sorting strategies. Pattern filtering technique is carried to suggest a consumer to an element the "rank" or "first option." Suggestion process collected information was about either the customer's first option on unusual subject relevant to films, books, travel, TV and commerce, etc. And from the other side, an effective selection of books recommendation system design utilizes prior scores or background of the customer. Cooperative sorting is a process of measuring and processing the categories across user opinions. Cooperative filtering first gathers the rankings or a preference of books provided by multiple users and then suggests books to different individuals based on various previous tastes and preferences. K-Means Multipathing together with K-Nearest Neighbor is applied on the BX dataset to achieve the greatest-optimized outcome. In prior methodology, the information is dispersed and ends in a high amount of matrices, whereas the information is collected throughout the suggested strategy and concludes in a small number of groupings. The preferred framework forecasts the customer's desire for a book based on various criteria. These consumers will affect their views on one another. It maximizes the succession and has smaller RMSE.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book1.jpg)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/jealousleopard/goodreadsbooks. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-45/Book%20Recommendation%20Systems/Dataset) folder too, you can access that!

## Goal
The goal of this project is to make a recommendation system which will recommend the user a book, based on the search results given input by the users.
*************************************
## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Description
4. Data Processing
5. Data Visualization
6. Outliers Handling
7. Machine Learning Models
    - KNN
    - t-SNE
    - DBSCAN
8. Testing the models
9. Conclusion

**************************************
## Libraries used
|Numpy|Pandas|Matplotlib|Sklearn|Seaborn|XgBoost|isbnlib|
|-|-|-|-|-|-|-|
|progressbar|copy|scipy|mpl_toolkits|newspaper|tqdm|
************************************
## Data Visualization
- **Data Processing**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book2.png)

- **PC1 vs PC2 Plotting**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book3..png)

- **PC1 vs PC3 Plotting**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book4.png)

- **PC3 vs PC2 Plotting**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book5.png)

- **Outliers Plotting**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book6.png)
******************************************
## Model Visualization
- **KNN Algortihm**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book7.png)

- **t-SNE Algorithm**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book8.png)

- **DBSCAN Algorithm**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-45/Book%20Recommendation%20Systems/Images/book9.png)
*************************************************
## Conclusion
* **Clustering** is the best way to represent this project.
* we have deployed three different types of clusters, such as, **KNN**, **t-SNE** and **DBSCAN**.
* After deploying all the algorithms, we have seen that more or less all the models are showing **similar results**.
* Hence, to develop the recommendation system one can use **any of the three algorithms** used here.
* But, using **DBSCAN algorithm** provides the user better experience in terms user data given, so I will recommend to use DBSCAN algorithm over the KNN and t-SNE clustering.
* DBSCAN Model is having the accuracy of **92.56%**.
*******************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
