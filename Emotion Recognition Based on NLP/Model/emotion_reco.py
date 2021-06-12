
## initial imports 
import nltk           ## for text processing
import pandas as pd   ## pandas for csv data processing 
import numpy as np    ## numpy for calculations,reshaping arrays etc
import pickle         ## pickle for saving model and exporting it to use in the API

## Reading up the dataset using pandas library
train = pd.read_csv("/content/train.txt", delimiter=';', header=None, names=['sentence','label'])  ## We have seperator ; in the file(txt) so that's the delimeter.
test = pd.read_csv("/content/test.txt", delimiter=';', header=None, names=['sentence','label'])    ## test dataset
val = pd.read_csv("/content/val.txt", delimiter=';', header=None, names=['sentence','label'])      ## validation dataset


df_data = pd.concat([train, test,val])           ## Getting the total dataset by Concatinating them using pandas 
df_data.to_csv (r'exportdata.txt', index=False)  ## Convert it to csv file
dt_data =  pd.read_csv("exportdata.txt")         ## Now Read The File with Pandas

from sklearn.feature_extraction.text import CountVectorizer  ## Imports for Model from sklearn
from nltk.tokenize import RegexpTokenizer                    ## Getting the Review from the DataSet using ReGex

token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(stop_words='english', ngram_range=(1,1), tokenizer = token.tokenize)  ## cv is the Object of Class CountVectorizer with the parameters
text = cv.fit_transform(dt_data['sentence'])                 ## Transform the text using our object.
 
# cv dumping
pickle.dump(cv,open('transform.pkl','wb'))               ## This is crucial as we have to use it in our Flask API

from sklearn.model_selection import train_test_split     ## Data Splitting using sklearn module
X_train, X_test, y_train, y_test = train_test_split(text,dt_data['label'], test_size=0.30, random_state=5)    ## splitting up the dataset into train and test


from sklearn.naive_bayes import MultinomialNB  ## Modelling starts here 
classifier = MultinomialNB()                   ## Multinomial Naive Bayes Model is being implemented here.
classifier.fit(X_train, y_train)               ## fitting the model
predicted = classifier.predict(X_test)         ## Now get the prediction

#Dummy data (test)
test_data = ['I love the way website looks']                         ## Our test data 
test_result = classifier.predict(cv.transform(test_data))            ## transforming it and predicting the result.
print(test_result)                                                   ## printing the result ( here:Emoruion will be printed)

#classifier dumping 
pickle.dump(classifier,open('nlp.pkl','wb'))                         ## Dumping the model to reuse it in the API
classifier= pickle.load(open('nlp.pkl','rb'))                        ## Loading the file with the required classifier.
