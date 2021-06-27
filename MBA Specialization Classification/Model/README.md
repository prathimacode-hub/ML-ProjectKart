# MBA Specialization Classification
An MBA in sales and marketing will be involved in the core sales process of the organisations and will be expected to connect with clients, generating value and revenue. They will be responsible for end to end Business cycle management, right from engagement with the client to the signing of contracts. They will be responsible for new business development involving prospect development, understanding business and technology scenarios and needs, identifying opportunities, solution offerings and business cases to the client & involvement in preparation of proposals. They will also be responsible for relationship building and account management. The prime job role will be to manage sales with the sole focus of maximizing revenues in a timely, reliable and consistent basis.

In the present day many organisations are expecting MBA ops graduates to be well versed in mobile technologies. An MBA in operations are also expected to take on challenges in logistics, supply chain design and supply chain management. They are made to handle various strategic issues including determining project management methods and implementing the structure of information technology networks and other operational issues include inventory management, work-in-process levels, acquisition of raw materials, quality control, handling of materials and maintenance policies etc.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-21/MBA%20Specialization%20Classification/Images/mba1.png)

## Goal
The goal of this project is to find out the MBA students who will be having good scores in their MBA career based on past activities using Classification algorithms.

## Dataset
The dataset is collected from Kaggle website. Here is the link for the website : https://www.kaggle.com/balakrishcodes/others?select=MBA_ADMISSIONS.csv. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-21/MBA%20Specialization%20Classification/Dataset) folder too, you can access that!

## What Have I done
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-21/MBA%20Specialization%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data pre-processing
4. Finding out the correlation between the attributes
5. Spliting the dataset for model creation
6. Classification Models -
    - Logistic Regression
    - Decision Tree Classifier
    - Random forest classifier
    - Gaussian NB
    - K-Nearest Neighbouring
    - Support Vector Machine (SVM)
    * Gradient Boosting
    - MLP Classifier
    - Stochastic Gradient Descent (SGD)
    - Linear Discriminant Analysis (LDA)
7. Model Comparison
8. Conclusion

## Libraries used
1. Numpy
2. Seaborn
3. Pandas
4. Matplotlib
5. Sklearn
6. XgBoost


## Model Comparison
We have deployed ten machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.23|
|Decision Tree Classifier|0.99|
|Random Forest Classifier|0.99|
|Gausian NB Algorithm|0.21|
|KNN Algorithm|0.61|
|Support Vector Machine Algorithm|0.35|
|Gradient Boosting|0.08|
|MLP Classifier|0.26|
|Stochastic Gradient Descent|0.15|
|Linear Discriminant Analysis|0.23|


## Conclusion
**Comparing all those scores scored by the machine learning algorithms, it is clear that Random Forest and Decision Tree Classifier are having the upper hand in case of this dataset and after this, we can use KNN algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. Random forest classifier
2. Decision tree classifier
3. KNN
4. Support vector machine
5. MLP classifier
6. LDA
7. Logistic regression
8. Gaussian Naive Bayes
9. SGD
10. Gradient Boosting

Hooray!! The models are deployed successfully!

********************************************************************

## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
