# dependencies

from utilities import makePrediction
import os
from flask import Flask,request,render_template

app = Flask(__name__)

IMAGE_FOLDER = os.getcwd() + "/static"

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

    image = makePrediction(img_loc)

    return render_template("index.html",data = image, image_loc = img.filename)


if __name__ == "__main__":
    app.run(debug=True,port=38000)
