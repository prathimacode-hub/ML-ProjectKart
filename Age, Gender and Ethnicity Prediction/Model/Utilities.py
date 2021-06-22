import numpy as np
import pandas as pd

# Function to split the values in pixels column


def toPixels(pixels):

    arr = np.array(pixels.split(),"float64")
    return arr

# Function to convert splitted data into image data of shape (48,48,1)

def reshapetoImage(data):

    Images = np.reshape(data["pixels"].to_list(),(data.shape[0],48,48,1))

    return Images

def getData():
    data = pd.read_csv("/home/anshal/Work/ML⁄DL⁄NLP/DL/Age-Gender_Race_prediction/Dataset/age_gender.csv")
    return data

