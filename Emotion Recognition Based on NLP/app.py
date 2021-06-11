
# Importing essential libraries
from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import nltk


# load pickle files 
filename = 'nlp.pkl'
classifier = pickle.load(open(filename, 'rb'))  ## classfier model
cv = pickle.load(open('transform.pkl', 'rb'))   ## this is used for transforming the data using CV class


app = Flask(__name__)  ## Flask constructor takes the name of current module (__name__) as argument


@app.route('/')
def home():
    return render_template('home.html')          ## inital home page


@app.route('/predict', methods=['POST'])
def predict():
    errors=[]                                     ## for finding out errors
    if request.method == 'POST':
        try:                                      ## try block starts here
            message = request.form['text']        ## get the data from home.html
            data = [message]                  
            vect = cv.transform(data).toarray()   ## transform them to array for prediction
            prediction = classifier.predict(vect) ## predict over the model
            string = " "                          ## an empty string , will be used for getting the emotion  
            emotion = string.join(prediction)     ## join to return the answer
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."   ## If any errors would , then this block would execute
            )
    return render_template('home.html', prediction=emotion, errors=errors)        ## render the page for the user


if __name__ == '__main__':     ## Execution starts here
    app.run(debug=True)
