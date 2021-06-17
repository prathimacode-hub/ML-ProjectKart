**Spam mail detection -#24**

**Goal:** This project predicts whether the received message is spam or ham.

**Dataset :** https://www.kaggle.com/team-ai/spam-text-message-classification

**What I have done :**
-Firstly I have imported the required libraries, and loaded the dataset onto the notebook.

-It is important to understand and preprocess the data before feeding it to model.

-As my dataset here include string data , I have preprocessed the text by converting it into lowercase and removing all the unnecessary word from the data which do not help in model building.

-As we cannot directly feed this data to the model I have converted the text to vector format .

-Before fitting the dataset to the model it is important to check the accuracy of data which can done by testing the data , So I have split the data for training and testing the data.

-I have used 2 algorithms here Logistic Regression and Naive Bayes , by feed the data to the algorithms , I have predicted the messages are spam/ham.

-As it is always important to know how are our algorithms performing the accuracy of the scores using the test data and comparing it to actual data.

**Models used:** Logistic Regression and Naive Bayes algorithms

**Libraries Needed:** Numpy, Pandas, Matplotlib, seaborn, nltk, sklearn, string

**Conclusion:** This project helps you predict the message is spam/ ham . From the two algorithms I have used the Naive bayes classifier is more accurate than Logistic regression.

Performance of Naive bayes:

classification report:
               precision    recall  f1-score   support

         ham       0.99      0.98      0.98      1445
        spam       0.89      0.91      0.90       227

    accuracy                             0.97      1672
	   macro avg       0.94      0.95      0.94      1672
	weighted avg       0.97      0.97      0.97      1672


confuion matrix:
 [[1420   25]
 [  20  207]]

Accuracy score: 0.9730861244019139
