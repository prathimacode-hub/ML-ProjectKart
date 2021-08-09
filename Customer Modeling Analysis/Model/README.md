PROJECT TITLE : Customer Modeling Analysis

Dataset : https://www.kaggle.com/shivan118/churn-modeling-dataset

GOAL : To predict about the customers modeling using ANN .

WHAT I HAD DONE : In this project first I performed a exploratory data analysis on the Customer Modeling dataset which includes of data cleaning , data manipulation, data preprocessing , data visualization and after that I did training and testing , then I did the feature scaling and used ANN for the prediction. While in the EDA part I have included different plots for the different visualizations of our dataset . In feature scaling I scaled the whole data and then did fit it into our training and testing dataset .
During ANN I used the different layers used in keras library like Sequentail , Dense that would work on the 1 -D layer and I also used the optimizers and loss during the compiling of our model . There are different activation functions like sigmoid , threshold , relu , softmax , tanh . In our dataset I used relu activation function and Adam optimizer , fitting the data with giving 200 epochs and got a accuracy of about 68 % which can be further increased more , and then I did the Label Encoding as our dataset was containing a lot of labels and text so that it could convert into numeric digits and then the training and testing of the data could be performed easily to find out the accuracy score and all the predictions.
During the prediction I kept the epochs as 200 and batch size as 256 using different activation function and the optimizers and got a accuracy score of 68 % which can be further increase by Hyper parameter Tuning.
Some plots which we used for visualizing the dataset are Histogram , Barplot , Boxplot, Heatmap , Scatter plot , Pairplot , Jointplot etc.

LIBRARIES:

PANDAS

NUMPY

MATPLOTLIB

SEABORN

SCIPY

SKLEARN

Keras

TensorFlow

Conclusion : We get to know why customers are withdrawing their account from bank.
The accuracy we got using ANN in 200 epochs is 68 % and the loss is 0.002 which can be further reduced durinh hyperparameter tuning .

-Aryan Tiwari























 














