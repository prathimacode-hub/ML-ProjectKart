import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle


app = Flask(__name__)

model = pickle.load(open("knn.pkl","rb"))
print("Model Loaded!")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods = ["POST"])
def predict():

    data = [int(x) for x in request.form.values()]
    final_data = [np.array(data)]
    pred = model.predict(final_data)

    output = round(pred[0],2)

    return render_template("index.html",prediction_text = "Salary : {}".format(output))



if __name__ == "__main__":
    app.run(debug=True,port=14000)
