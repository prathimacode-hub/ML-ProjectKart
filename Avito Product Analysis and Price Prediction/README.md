# Avito Product Analysis and Price Prediction
### Aim
Perform exploratory data analysis on the dataset of products from Avito Advertising website and develop a ML model to predict prices of the other products in the website.

### Dataset
https://www.kaggle.com/abderrahimalakouche/data-analysis-products-dataset

#### Description of features in the dataset:
1. **Product_name**: Name of the product, it can be written in English, Arabic, or French 
2. **Product_id**: Product id or product reference number
3. **Product_Category**: Category of Product
4. **price**: Product price
5. **Professional_Publication**: If publication is 'pro'(professional) or private
6. **Region_address**: Regional address of seller
7. **Local_address**: Local address (City) of seller

### Project Description and Approach
* **Cleaned** the Product dataset by removing unwanted spaces, quotes and by replacing unwanted strings and empty string with NAN. 
* Distributed the dataset in test and training set.
* Dealt with **missing values** and removed **duplicates** from the test and training dataset.
* Analysed the training dataset by plotting countplot to check the frequency of products and used **histogram distribution** for prices and applied **normalisation fit** to the price (target value) to check for **skewness** present in the dataset.
* **Box plot** and **Swarmplot** was plotted to detect the presence of **outliers** in the dataset.
* **Hist plot** was plotted between the different publications of the product and the price range they belong to.
* **Bar plot** was plotted between different regions of sellers and total price of all the products sold by the seller in each region to check for the demand of diiferent products.
* Categorial features were **label encoded** for applying regression models for the prediction of price.
* Features were **scaled** before applying ML model to it. 
* Applied multiple regression models on the scaled dataset, then predicted price of test dataset using the best model.

### Models Used
* **Random Forest Regressor**: A random forest is a supervised machine learning algorithm that can be used for both classification and regression tasks. Here, random forest is used for regression task. 
Random Forest Regression is a supervised learning algorithm that uses ensemble learning method for regression. The model works by sampling the training dataset, building multiple decision trees, and outputting the mean/mode of prediction of the individual trees.

* **Logistic Regression**: Logistic regression is a fundamental classification technique, but can also be used for regression tasks. It is an algorithm that measures the probability of a binary response as the value of response variable based on the mathematical equation relating it with the predictor variables. It uses sigmoid function for the feature modelling.

* **XGBoost Regressor**: XGBoost is a powerful approach for building supervised regression models. It is based on the Gradient Boosting model which uses the boosting technique of ensemble learning where the underfitted data of the weak learners are passed on to the strong learners to increase the strength and accuracy of the model.

* **Kernel Ridge**: Kernel ridge regression (KRR) combines ridge regression (linear least squares with l2-norm regularization) with the kernel trick. It thus learns a linear function in the space induced by the respective kernel and the data. For non-linear kernels, this corresponds to a non-linear function in the original space.

* **Linear Regression**: Linear regression is a linear model that assumes a linear relationship between the input variables matrix (x) and the single output variable (y).

* **Isolation Forest Regressor**: Isolation Forest is an outlier detection technique that identifies anomalies instead of normal observations. Similarly to Random Forest, it is built on an ensemble of binary (isolation) trees. It can be scaled up to handle large, high-dimensional datasets.

* **Support Vector Regressor**: Support vector machine (SVM) is machine learning algorithm that analyzes data for classification and regression analysis. SVM is a supervised learning method that looks at data and sorts it into one of two categories. An SVM outputs a map of the sorted data with the margins between the two as far apart as possible.

* **CATBoost Regressor**: CatBoost builds upon the theory of decision trees and gradient boosting. The main idea of boosting is to sequentially combine many weak models (a model performing slightly better than random chance) and thus through greedy search create a strong competitive predictive model. Because gradient boosting fits the decision trees sequentially, the fitted trees will learn from the mistakes of former trees and hence reduce the errors. This process of adding a new function to existing ones is continued until the selected loss function is no longer minimized.

* **LightGBM Regressor**: LightGBM is a gradient boosting framework based on decision trees to increases the efficiency of the model and reduces memory usage.
It uses two novel techniques: Gradient-based One Side Sampling and Exclusive Feature Bundling (EFB) which fulfills the limitations of histogram-based algorithm that is primarily used in all GBDT (Gradient Boosting Decision Tree) frameworks. 

### Libraries Needed
* sklearn==0.0
* seaborn==0.10.1
* numpy==1.18.5
* pandas==1.0.5
* matplotlib==3.2.2
* scipy==1.5.0
* xgboost==1.4.2
* catboost==0.26
* lightgbm==3.2.1

### Accuracy Score of each model
#### R2 score:
* Linear Regression: -0.0026346917168460493
* Logistic Regression: -0.03122870736746952
* Kernel Ridge: 0.07499918734424516
* XGBoost Regressor: 0.3137444676862252 
* Random Forest Regressor: 0.14197453549962025
* Isolation Forest Regressor: -0.0524807016999953
* Support Vector Regressor: -0.04639285849695862
* CATBoost Regressor: 0.44380079463588373
* LightGBM Regressor: -0.38778501400658194
#### Mean absolute error:
* Linear Regression: 54734.79893339306
* Logistic Regression: 32590.526946107784
* Kernel Ridge: 49940.906857801936
* XGBoost Regressor: 31042.433791535583
* Random Forest Regressor: 45087.353552894216
* Isolation Forest Regressor: 34873.577619854346
* Support Vector Regressor: 34037.63516031823
* CATBoost Regressor: 48696.472942350345
* LightGBM Regressor: 84983.95482918626
#### Mean squared error:
* Linear Regression: 23234632070.370255
* Logistic Regression: 23897257689.197605
* Kernel Ridge: 21435577408.605682
* XGBoost Regressor: 15902995309.551525
* Random Forest Regressor: 19883519031.780075
* Isolation Forest Regressor: 24389742412.853348
* Support Vector Regressor: 24248665310.601425
* CATBoost Regressor: 12889125023.530657
* LightGBM Regressor: 32159942658.679493

For concluding a perfect model, I used all the three errors and score to calculate a new score by introducing a new measure to the model,
* **Final score**=(R2 score * 100)/(Mean absolute error + Mean squared error)
#### Final score:
* Linear Regression: -1.1339475926397641e-11
* Logistic Regression: -1.3067886359469486e-10
* Kernel Ridge: 3.4988100008162664e-10
* XGBoost Regressor: 1.972860138328688e-09
* Random Forest Regressor: 7.14029610833203e-10 
* Isolation Forest Regressor: -2.15174993537938e-10
* Support Vector Regressor: -1.9132101821507556e-10
* CATBoost Regressor: 3.443205936057163e-09
* LightGBM Regressor: -1.20579813648076e-09

### Conclusion
Some of the scores above are negative, this shows that the dataset was underfitted to the models.
Since, final score of CATBoost Regressor is the highest among all the rest of the models, so, CATBoost Regressor model works best for Product Price Prediction.
The price of test dataset was predicted using CATBoost model and compiled in the dataset.

### My Name
* Palak Singh
* https://www.linkedin.com/in/palak-singh-9066271a4/
