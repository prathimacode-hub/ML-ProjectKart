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

Mall Customer Data has hypothetical customer data. According to this data , i have divided the customers into various groups which are mentioned above.

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
KMeans is the best model.


### YOUR NAME

Dilrose Reji
- DevIncept Participant

