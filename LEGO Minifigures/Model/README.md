# LEGO Minifigures

## Goal

This dataset contains a lot of pictures of various LEGO Minifigures.
There are several images in different poses or with different environments for each Minifigure in the dataset. 
You can use this dataset for the image classification tasks or try to create more interesting things. 
You can try getting more accurate predictions for the test set.

## DATASET

You can download dataset [here](https://www.kaggle.com/ihelon/lego-minifigures-classification/)

## WHAT I HAD DONE

* Importing Libraries

* Loading Dataset - Exploratory Data Analysis

* Data Preprocessing

* Loading Base Model for Transfer Learning

* Compiling Model

* Training Model

## MODELS USED

"CNN"

"Sequential_2"

## Details:

![](https://github.com/Isha307/ML-ProjectKart/blob/main/LEGO%20Minifigures/Images/model.png)

## LIBRARIES NEEDED

* pandas

* numpy

* matplotlib

* seaborn

* sklearn

* seaborn

* tensorflow

## CONCLUSION

I tried to train this data with different CNN architectures but none worked for me. 

ResNet18 and Inception accuracy were low as compared to VGG16.

So I finally used **VGG16** with 200 epochs to highly train the data.

```
Epoch 200/200
42/42 [==============================] - 16s 378ms/step - loss: 0.0866 - accuracy: 0.9857 - val_loss: 5.1646 - val_accuracy: 0.6479
```

## Author

Code Contributed by, [@Isha307](https://github.com/Isha307)
