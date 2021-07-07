import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('../Dataset/model.pickle', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['variance', 'skewness', 'curtosis', 'entropy']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
        
    if output[0] == 0:
        res_val = " not a fake note"
    else:
        res_val = " a fake note"
        

    return render_template('index.html', prediction_text='This note is {}'.format(res_val))

if __name__ == "__main__":
    app.run()