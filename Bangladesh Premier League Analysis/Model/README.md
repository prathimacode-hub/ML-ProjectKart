# Bangladesh Premier League Analysis

# GOAL 
The main goal of the project is to analyze the performance of the bangladesh players in their premier league and obtaining the top 5 players in all of them in different fields like bowling, batting, toss_winner, highest runner, man of the match, etc.

# DATASET 
* (Dataset Link)[https://www.kaggle.com/abdunnoor11/bpl-data]

# WHAT I HAD DONE 
* Performed Exploratory Data Analysis on data.
* Created data visualisations to understand the data in a better way.
* Found strong relationships between independent features and dependent feature using correlation.
* Handled missing values using strong correlations,dropping unnecessary ones.
* Used different Regression techniques like Linear Regression,Ridge Regression,Lasso Regression and deep neural networks to predict the dependent feature in most suitable manner.
* Compared various models and used best performance model to make predictions.
* Used Mean Squared Error and R2 Score for evaluating model's performance.
* Visualized best model's performance using matplotlib and seaborn library.

**MODELS USED**

| Model                        | MSE        | R2         |
|------------------------------|------------|------------|
| Random Forest Regression     | 19.355984  | 0.371316   |
| Gradient Boosting Regression | 19.420494  | 0.369221   |
| XG Boost Regression          | 21.349168  | 0.306577   |
| Ridge Regression             | 26.813981  | 0.129080   |
| Linear Regression            | 26.916888  | 0.125737   |
| Deep Neural Network          | 27.758216  | 0.098411   |
| Decision Tree Regression     | 29.044533  | 0.056631   |

 ***Deep Neural Network using Keras***
 * Input Dense Layer | Activation Function : Relu
 * Three Hidden Layers | Activation Function : Relu
 * Output layer | Activation Function : Linear
 * loss : mean_absolute_error
 * optimizer : adam

# LIBRARIES NEEDED 
* Pandas
* Numpy
* Matplotlib
* XGboost
* Seaborn
* Scikit-learn
* Tensorflow
* Keras

# CONCLUSION 

* Here we can see that R2 Score and Mean Absolute Error is best for Random Forest Regression.
* By Using Neural network, We cannot get the minimum Mean Absolute Error value possible.
* Here, Random Forest Regression model can predict most accurate results for predicting bangladesh premier league winning team which is the highest model performance in comparison with other Models.

