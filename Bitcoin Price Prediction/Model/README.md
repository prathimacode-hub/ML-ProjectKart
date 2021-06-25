#  BITCOIN PRICE PREDICTION 

**GOAL** 
- The main purpose of this project is to predict the price of Bitcoin.

**DATASET**
- The data used in this project can be downloaded from [here](https://www.kaggle.com/vikramjeetsinghs/bitcoin-dataset)

**WHAT I HAD DONE**
- Performed Exploratory Data Analysis on data.
- Created data visualisations to understand the data in a better way.
- Found strong relationships between independent features and dependent feature using correlation.
- Handled missing values using strong correlations,dropping unnecessary ones.
- Used different Regression techniques like Linear Regression,Ridge Regression,Lasso Regression and deep neural networks to predict the dependent feature in most suitable manner.
- Compared various models and used best performance model to make predictions.
- Used Mean Squared Error and R2 Score for evaluating model's performance.
- Visualized best model's performance using matplotlib and seaborn library.

**MODELS USED**
- 
 Model | Mean Absolute Error| R2 Score |
  -------- | ---------- | ---------- |
 Deep Neural Network | 9.028034 | 0.999931 |
 Ridge Regression | 12.459064 | 0.999936 |
 Lasso Regression | 13.135666 | 0.999921 |
 Linear Regression | 13.528254 | 0.999930 |
 
 ***Deep Neural Network using Keras***
 - Input Dense Layer | Activation Function : Relu
 - Three Hidden Layers | Activation Function : Relu
 - Output layer | Activation Function : Linear
 - loss : mean_absolute_error
 - optimizer : adam


**LIBRARIES NEEDED**
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- tensorflow-keras


**CONCLUSION**
- R2 score for all the models are almost same value, so we can consider Mean Absolute Error for evaluating models.
- By Using Neural network, We can get the minimum Mean Absolute Error value possible.
- Here, deep neural network model can predict most accurate results for predicting bitcoin price which is highest model performance in comparison with other Models.
