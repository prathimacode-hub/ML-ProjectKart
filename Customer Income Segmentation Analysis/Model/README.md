### PROJECT TITLE: Customer Income Analysis Segmentation

### GOAL
The project revolves around classifying people into 5 types:
- low income low spending
- low income high spending
- medium income medium spending
- high income high spending
- low income low spending


### DATASET

https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python

### DESCRIPTION

Mall Customer Data has hypothetical customer data. It puts you in the shoes of the owner of a supermarket. You have customer data and on the basis of this data, I have divided the customers into various groups which are mentioned above.
It has features such as CustomerID, Gender, Age, Annual Income(in thousand rupees) and Spending Score(based on customer behaviour and spending nature). 

### WHAT I HAD DONE

- First did my data preprocessing
- Did scaling on the features since all of them are not in the same range.
- I selected features which would contribute more such as annual income and spending score
- Then I used some Classification models which is Logistic Regression ,Decision Trees, SVM, KMeans on the training data. 
- Then I calculate accuracy of every model on the test and training data and reviewed thier respective confusion matrix.

### MODELS USED

- BernoulliNB
- Logistic Regression
- KMeans

### LIBRARIES NEEDED
- pandas
- sklearn
- matplotlib


### ACCURACIES
- BernoulliNB: 34%
- Logistic Regression: 70%
- KMeans: As we can see in the diagram, that all of them are grouped into 5 categories properly


### CONCLUSION
As we can see in the diagram, that all of them are grouped into 5 categories properly, which are also giving proper predictions on known as well as unknown data.
Tried logistic regression, but it is not able to predict correctly on known data & hence it will also not able to predict properly on unknown data and in naive bayes algorithm, the accuracy is itself low. But KMeans is dividing the data into 5 groups perfectly as seen in the plot.
Therefore, KMeans is the best model.


### YOUR NAME

Dilrose Reji
- DevIncept Participant

