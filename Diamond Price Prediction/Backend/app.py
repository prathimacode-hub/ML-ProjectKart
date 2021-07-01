# #import required packages
# from flask import Flask, render_template, request
# import jsonify
# import requests
# import pickle
# import numpy as np
# import sklearn
# from sklearn.preprocessing import StandardScaler

# #create a Flask object
# app = Flask("diamond_model")

# #load the ml model which we have saved earlier in .pkl format
# model = pickle.load(open('diamond_price_model.pkl', 'rb'))

# #define the route(basically url) to which we need to send http request
# #HTTP GET request method
# @app.route('/',methods=['GET'])

# #create a function Home that will return index.html(which contains html form)
# #index.html file is created seperately
# def Home():
#     return render_template('index.html')

# #creating object for StandardScaler
# standard_to = StandardScaler()

# #HTTP POST request method
# #define the route for post method 
# @app.route("/predict", methods=['POST'])

# #define the predict function which is going to predict the results from ml model based on the given values through html form
# def predict():
#     #Fuel_type_Petrol is used in the html form and therefore we are initiating Fuel_Type_Diesel as zero 
#     Fuel_Type_Diesel=0
#     if request.method == 'POST':

#         #Use request.form to get the data from html form through post method.
#         #these all are nothing but features of our dataset(ml model)
#         Year = int(request.form['Year'])
#         Year = 2020 - Year
#         Carat = float(request.form['carat'])
#         Depth = float(request.form['depth'])
#         Table = float(request.form['table'])

#         Kms_Driven=int(request.form['Kms_Driven'])
#         Kms_Driven2=np.log(Kms_Driven)
#         Owner=int(request.form['Owner'])
#         Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        
#         #Fuel_Type(feature) is categorised into petrol, diesel, cng, therefore we have done one-hot encoding on it while building model 
#         if(color_E=='E'):
#                 color_E=1
#                 Fuel_Type_Diesel=0
#         elif(Fuel_Type_Petrol=='Diesel'):
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=1
#         else:
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=0
            
#         #Seller_type(feature) is categorised into indivividual and dealer,therefore we have done one-hot encoding on it while building model
#         Seller_Type_Individual=request.form['Seller_Type_Individual']
#         if(Seller_Type_Individual=='Individual'):
#             Seller_Type_Individual=1
#         else:
#             Seller_Type_Individual=0
            
#         #Transmission mannual(feature) is categorised into mannual and automatic,therefore we have done one-hot encoding on it while building model
#         Transmission_Mannual=request.form['Transmission_Mannual']
#         if(Transmission_Mannual=='Mannual'):
#             Transmission_Mannual=1
#         else:
#             Transmission_Mannual=0
#         prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
#         output=round(prediction[0],2)
        
#         #condition for invalid values
#         if output<0:
#             return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        
#         #condition for prediction when values are valid
#         else:
#             return render_template('index.html',prediction_text="You Can Sell the Car at {} lakhs".format(output))
        
#     #html form to be displayed on screen when no values are inserted; without any output or prediction
#     else:
#         return render_template('index.html')


# if __name__=="__main__":
#     #run method starts our web service
#     #Debug : as soon as I save anything in my structure, server should start again
#     app.run(debug=True)





import numpy as np 
from flask import Flask, request, jsonify,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Price of Diamond should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)