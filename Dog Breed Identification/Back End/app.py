#flask
from flask import Flask,request,render_template,redirect,url_for

#keras
from tensorflow import keras
from keras.preprocessing.image import load_img,img_to_array
from keras.models import load_model

#basic
import numpy as np 
import os
import pickle

app =Flask(__name__)

#load model
model = load_model("Model_nasnet.h5")

print("Model Loaded!")

#images folder
IMAGE_FOLDER = os.getcwd()+ "/static"

#function to load image and predict 
def predict_img(path):
    classes = ['affenpinscher',
 'afghan_hound',
 'african_hunting_dog',
 'airedale',
 'american_staffordshire_terrier',
 'appenzeller',
 'australian_terrier',
 'basenji',
 'basset',
 'beagle',
 'bedlington_terrier',
 'bernese_mountain_dog',
 'black-and-tan_coonhound',
 'blenheim_spaniel',
 'bloodhound',
 'bluetick',
 'border_collie',
 'border_terrier',
 'borzoi',
 'boston_bull',
 'bouvier_des_flandres',
 'boxer',
 'brabancon_griffon',
 'briard',
 'brittany_spaniel',
 'bull_mastiff',
 'cairn',
 'cardigan',
 'chesapeake_bay_retriever',
 'chihuahua',
 'chow',
 'clumber',
 'cocker_spaniel',
 'collie',
 'curly-coated_retriever',
 'dandie_dinmont',
 'dhole',
 'dingo',
 'doberman',
 'english_foxhound',
 'english_setter',
 'english_springer',
 'entlebucher',
 'eskimo_dog',
 'flat-coated_retriever',
 'french_bulldog',
 'german_shepherd',
 'german_short-haired_pointer',
 'giant_schnauzer',
 'golden_retriever',
 'gordon_setter',
 'great_dane',
 'great_pyrenees',
 'greater_swiss_mountain_dog',
 'groenendael',
 'ibizan_hound',
 'irish_setter',
 'irish_terrier',
 'irish_water_spaniel',
 'irish_wolfhound',
 'italian_greyhound',
 'japanese_spaniel',
 'keeshond',
 'kelpie',
 'kerry_blue_terrier',
 'komondor',
 'kuvasz',
 'labrador_retriever',
 'lakeland_terrier',
 'leonberg',
 'lhasa',
 'malamute',
 'malinois',
 'maltese_dog',
 'mexican_hairless',
 'miniature_pinscher',
 'miniature_poodle',
 'miniature_schnauzer',
 'newfoundland',
 'norfolk_terrier',
 'norwegian_elkhound',
 'norwich_terrier',
 'old_english_sheepdog',
 'otterhound',
 'papillon',
 'pekinese',
 'pembroke',
 'pomeranian',
 'pug',
 'redbone',
 'rhodesian_ridgeback',
 'rottweiler',
 'saint_bernard',
 'saluki',
 'samoyed',
 'schipperke',
 'scotch_terrier',
 'scottish_deerhound',
 'sealyham_terrier',
 'shetland_sheepdog',
 'shih-tzu',
 'siberian_husky',
 'silky_terrier',
 'soft-coated_wheaten_terrier',
 'staffordshire_bullterrier',
 'standard_poodle',
 'standard_schnauzer',
 'sussex_spaniel',
 'tibetan_mastiff',
 'tibetan_terrier',
 'toy_poodle',
 'toy_terrier',
 'vizsla',
 'walker_hound',
 'weimaraner',
 'welsh_springer_spaniel',
 'west_highland_white_terrier',
 'whippet',
 'wire-haired_fox_terrier',
 'yorkshire_terrier']
    img = load_img(path,target_size=(331,331))
    img_arr = img_to_array(img)
    img_arr_expnd  = np.expand_dims(img_arr,axis=0)
    img = keras.applications.densenet.preprocess_input(img_arr_expnd)

    pred = model.predict(img)
    result = classes[np.argmax(pred)]

    return result

@app.route("/",methods=["GET","POST"])
def index():
    #main page
    return render_template("index.html",data="Hey!!")


@app.route("/predict",methods=["POST"])
def predict():
    #get image
    if request.method == "POST":
        img = request.files['img']

        if img:
            img_location = os.path.join(
                IMAGE_FOLDER,
                img.filename
            )
            img.save(img_location)

    image = predict_img(img_location)

    return render_template("index.html",data=image,image_loc = img.filename)






if __name__ == '__main__':
    app.run(debug=True,port=10000)
