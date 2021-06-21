# Importing Dependencies

import numpy as np
import pandas as pd
import os

from keras.models import  load_model
from keras.preprocessing.image import load_img,img_to_array

from flask import Flask, request , render_template

app = Flask(__name__)

#load model
model = load_model("Model_gender.h5")
print("Model Loaded!!")

IMAGE_FOLDER = os.getcwd() + "/static"

# function lo load image and predict
def predictImage(path):
    classes = ["Male","Female"]
    img = load_img(path,target_size=(48,48,1),color_mode="grayscale")
    img = img_to_array(img)
    img = np.expand_dims(img,axis=0)

    pred = model.predict(img)
    result = classes[int(np.round(pred[0][0]))]

    return result

@app.route("/",methods = ["GET","POST"])
def index():
    return render_template("index.html",data = "Hey there!!")

@app.route("/predict",methods = ["POST","GET"])
def predict():
    if request.method == "POST":
        img = request.files["img"]

        if img:
            img_loc = os.path.join(
                IMAGE_FOLDER,
                img.filename
            )
            img.save(img_loc)

    image = predictImage(img_loc)

    return  render_template("index.html",data = image,image_loc = img.filename)

if __name__ == "__main__":
    app.run(debug=True,port=9666)