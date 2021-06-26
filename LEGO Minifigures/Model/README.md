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

```
Epoch 1/200
42/42 [==============================] - 18s 364ms/step - loss: 7.6387 - accuracy: 0.0714 - val_loss: 2.4793 - val_accuracy: 0.3310
Epoch 2/200
42/42 [==============================] - 14s 343ms/step - loss: 1.6754 - accuracy: 0.5429 - val_loss: 2.3015 - val_accuracy: 0.3592
Epoch 3/200
42/42 [==============================] - 15s 348ms/step - loss: 0.7527 - accuracy: 0.7667 - val_loss: 1.8752 - val_accuracy: 0.4930
Epoch 4/200
42/42 [==============================] - 15s 350ms/step - loss: 0.4276 - accuracy: 0.8571 - val_loss: 1.8997 - val_accuracy: 0.5211
Epoch 5/200
42/42 [==============================] - 14s 346ms/step - loss: 0.4316 - accuracy: 0.8429 - val_loss: 1.6431 - val_accuracy: 0.6127
Epoch 6/200
42/42 [==============================] - 15s 351ms/step - loss: 0.2855 - accuracy: 0.9095 - val_loss: 1.7669 - val_accuracy: 0.5704
Epoch 7/200
42/42 [==============================] - 14s 348ms/step - loss: 0.2346 - accuracy: 0.9143 - val_loss: 1.6811 - val_accuracy: 0.5775
Epoch 8/200
42/42 [==============================] - 14s 347ms/step - loss: 0.0855 - accuracy: 0.9714 - val_loss: 1.5086 - val_accuracy: 0.6127
Epoch 9/200
42/42 [==============================] - 15s 355ms/step - loss: 0.1016 - accuracy: 0.9714 - val_loss: 1.6270 - val_accuracy: 0.6127
Epoch 10/200
42/42 [==============================] - 15s 352ms/step - loss: 0.1826 - accuracy: 0.9429 - val_loss: 1.4215 - val_accuracy: 0.6549
Epoch 11/200
42/42 [==============================] - 15s 350ms/step - loss: 0.1346 - accuracy: 0.9667 - val_loss: 1.5183 - val_accuracy: 0.6268
Epoch 12/200
42/42 [==============================] - 15s 358ms/step - loss: 0.1271 - accuracy: 0.9667 - val_loss: 1.5587 - val_accuracy: 0.6268
Epoch 13/200
42/42 [==============================] - 15s 359ms/step - loss: 0.0565 - accuracy: 0.9857 - val_loss: 1.6340 - val_accuracy: 0.6549
Epoch 14/200
42/42 [==============================] - 15s 353ms/step - loss: 0.0713 - accuracy: 0.9810 - val_loss: 1.5267 - val_accuracy: 0.6056
Epoch 15/200
42/42 [==============================] - 15s 355ms/step - loss: 0.0841 - accuracy: 0.9714 - val_loss: 1.6919 - val_accuracy: 0.6127
Epoch 16/200
42/42 [==============================] - 15s 358ms/step - loss: 0.1101 - accuracy: 0.9714 - val_loss: 1.5332 - val_accuracy: 0.6620
Epoch 17/200
42/42 [==============================] - 15s 357ms/step - loss: 0.0326 - accuracy: 0.9905 - val_loss: 1.5283 - val_accuracy: 0.6268
Epoch 18/200
42/42 [==============================] - 15s 354ms/step - loss: 0.0527 - accuracy: 0.9857 - val_loss: 1.5016 - val_accuracy: 0.6479
Epoch 19/200
42/42 [==============================] - 15s 356ms/step - loss: 0.0342 - accuracy: 0.9905 - val_loss: 1.7716 - val_accuracy: 0.6197
Epoch 20/200
42/42 [==============================] - 15s 354ms/step - loss: 0.1007 - accuracy: 0.9810 - val_loss: 1.6320 - val_accuracy: 0.5915
Epoch 21/200
42/42 [==============================] - 15s 356ms/step - loss: 0.0322 - accuracy: 0.9905 - val_loss: 1.8103 - val_accuracy: 0.5563
Epoch 22/200
42/42 [==============================] - 15s 356ms/step - loss: 0.1270 - accuracy: 0.9524 - val_loss: 1.7684 - val_accuracy: 0.5704
Epoch 23/200
42/42 [==============================] - 15s 354ms/step - loss: 0.0948 - accuracy: 0.9571 - val_loss: 1.9310 - val_accuracy: 0.5493
Epoch 24/200
42/42 [==============================] - 15s 356ms/step - loss: 0.2025 - accuracy: 0.9333 - val_loss: 2.6596 - val_accuracy: 0.4648
Epoch 25/200
42/42 [==============================] - 15s 360ms/step - loss: 0.1570 - accuracy: 0.9429 - val_loss: 2.2202 - val_accuracy: 0.5563
Epoch 26/200
42/42 [==============================] - 15s 362ms/step - loss: 0.2505 - accuracy: 0.9143 - val_loss: 2.5507 - val_accuracy: 0.5563
Epoch 27/200
42/42 [==============================] - 15s 361ms/step - loss: 0.3230 - accuracy: 0.9143 - val_loss: 1.9816 - val_accuracy: 0.6127
Epoch 28/200
42/42 [==============================] - 15s 360ms/step - loss: 0.4504 - accuracy: 0.9238 - val_loss: 2.3056 - val_accuracy: 0.5563
Epoch 29/200
42/42 [==============================] - 15s 361ms/step - loss: 0.2336 - accuracy: 0.9333 - val_loss: 2.0168 - val_accuracy: 0.6127
Epoch 30/200
42/42 [==============================] - 15s 360ms/step - loss: 0.1952 - accuracy: 0.9381 - val_loss: 2.2124 - val_accuracy: 0.6056
Epoch 31/200
42/42 [==============================] - 15s 361ms/step - loss: 0.2531 - accuracy: 0.9333 - val_loss: 2.4299 - val_accuracy: 0.5282
Epoch 32/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1593 - accuracy: 0.9619 - val_loss: 2.6356 - val_accuracy: 0.5845
Epoch 33/200
42/42 [==============================] - 15s 362ms/step - loss: 0.1647 - accuracy: 0.9571 - val_loss: 2.9127 - val_accuracy: 0.5704
Epoch 34/200
42/42 [==============================] - 15s 363ms/step - loss: 0.1283 - accuracy: 0.9476 - val_loss: 2.6563 - val_accuracy: 0.5845
Epoch 35/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1222 - accuracy: 0.9667 - val_loss: 2.3495 - val_accuracy: 0.5845
Epoch 36/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1515 - accuracy: 0.9524 - val_loss: 2.4961 - val_accuracy: 0.5915
Epoch 37/200
42/42 [==============================] - 15s 361ms/step - loss: 0.0493 - accuracy: 0.9667 - val_loss: 2.5609 - val_accuracy: 0.5986
Epoch 38/200
42/42 [==============================] - 15s 359ms/step - loss: 0.2743 - accuracy: 0.9476 - val_loss: 2.2196 - val_accuracy: 0.6127
Epoch 39/200
42/42 [==============================] - 15s 360ms/step - loss: 0.2338 - accuracy: 0.9619 - val_loss: 2.1984 - val_accuracy: 0.6408
Epoch 40/200
42/42 [==============================] - 15s 360ms/step - loss: 0.1790 - accuracy: 0.9476 - val_loss: 2.5410 - val_accuracy: 0.6197
Epoch 41/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1005 - accuracy: 0.9762 - val_loss: 2.7992 - val_accuracy: 0.6408
Epoch 42/200
42/42 [==============================] - 15s 360ms/step - loss: 0.0975 - accuracy: 0.9619 - val_loss: 3.0096 - val_accuracy: 0.5915
Epoch 43/200
42/42 [==============================] - 15s 362ms/step - loss: 0.1063 - accuracy: 0.9762 - val_loss: 3.4727 - val_accuracy: 0.5563
Epoch 44/200
42/42 [==============================] - 15s 362ms/step - loss: 0.3687 - accuracy: 0.9476 - val_loss: 3.7773 - val_accuracy: 0.5352
Epoch 45/200
42/42 [==============================] - 15s 362ms/step - loss: 0.1335 - accuracy: 0.9476 - val_loss: 3.1740 - val_accuracy: 0.5352
Epoch 46/200
42/42 [==============================] - 15s 359ms/step - loss: 0.0262 - accuracy: 0.9952 - val_loss: 2.9987 - val_accuracy: 0.6056
Epoch 47/200
42/42 [==============================] - 15s 365ms/step - loss: 0.1647 - accuracy: 0.9810 - val_loss: 2.7377 - val_accuracy: 0.6197
Epoch 48/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1088 - accuracy: 0.9810 - val_loss: 2.7518 - val_accuracy: 0.6197
Epoch 49/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1626 - accuracy: 0.9714 - val_loss: 2.7016 - val_accuracy: 0.5986
Epoch 50/200
42/42 [==============================] - 15s 363ms/step - loss: 0.1865 - accuracy: 0.9762 - val_loss: 2.9235 - val_accuracy: 0.5915
Epoch 51/200
42/42 [==============================] - 15s 362ms/step - loss: 0.2457 - accuracy: 0.9476 - val_loss: 2.5556 - val_accuracy: 0.6268
Epoch 52/200
42/42 [==============================] - 15s 365ms/step - loss: 0.1067 - accuracy: 0.9667 - val_loss: 2.7299 - val_accuracy: 0.5845
Epoch 53/200
42/42 [==============================] - 15s 365ms/step - loss: 0.2815 - accuracy: 0.9619 - val_loss: 3.1733 - val_accuracy: 0.5915
Epoch 54/200
42/42 [==============================] - 15s 368ms/step - loss: 0.1375 - accuracy: 0.9810 - val_loss: 2.9380 - val_accuracy: 0.5775
Epoch 55/200
42/42 [==============================] - 15s 365ms/step - loss: 0.0366 - accuracy: 0.9857 - val_loss: 3.0353 - val_accuracy: 0.6127
Epoch 56/200
42/42 [==============================] - 15s 365ms/step - loss: 0.0559 - accuracy: 0.9905 - val_loss: 2.7017 - val_accuracy: 0.6197
Epoch 57/200
42/42 [==============================] - 15s 363ms/step - loss: 0.0562 - accuracy: 0.9857 - val_loss: 2.7598 - val_accuracy: 0.6197
Epoch 58/200
42/42 [==============================] - 15s 363ms/step - loss: 0.0299 - accuracy: 0.9857 - val_loss: 3.3836 - val_accuracy: 0.5563
Epoch 59/200
42/42 [==============================] - 15s 363ms/step - loss: 0.0965 - accuracy: 0.9667 - val_loss: 3.1335 - val_accuracy: 0.5986
Epoch 60/200
42/42 [==============================] - 15s 365ms/step - loss: 0.0371 - accuracy: 0.9905 - val_loss: 3.6907 - val_accuracy: 0.5211
Epoch 61/200
42/42 [==============================] - 15s 364ms/step - loss: 0.1528 - accuracy: 0.9714 - val_loss: 3.1125 - val_accuracy: 0.5704
Epoch 62/200
42/42 [==============================] - 15s 365ms/step - loss: 0.1287 - accuracy: 0.9762 - val_loss: 3.1658 - val_accuracy: 0.5986
Epoch 63/200
42/42 [==============================] - 15s 364ms/step - loss: 0.0804 - accuracy: 0.9810 - val_loss: 2.8640 - val_accuracy: 0.5845
Epoch 64/200
42/42 [==============================] - 15s 364ms/step - loss: 0.2523 - accuracy: 0.9524 - val_loss: 2.9089 - val_accuracy: 0.6127
Epoch 65/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1826 - accuracy: 0.9667 - val_loss: 3.2598 - val_accuracy: 0.6056
Epoch 66/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1862 - accuracy: 0.9714 - val_loss: 2.6677 - val_accuracy: 0.6690
Epoch 67/200
42/42 [==============================] - 15s 361ms/step - loss: 0.0883 - accuracy: 0.9714 - val_loss: 2.9492 - val_accuracy: 0.6549
Epoch 68/200
42/42 [==============================] - 15s 363ms/step - loss: 0.0417 - accuracy: 0.9857 - val_loss: 3.1435 - val_accuracy: 0.6549
Epoch 69/200
42/42 [==============================] - 15s 362ms/step - loss: 0.1945 - accuracy: 0.9667 - val_loss: 2.7247 - val_accuracy: 0.6620
Epoch 70/200
42/42 [==============================] - 15s 363ms/step - loss: 0.0642 - accuracy: 0.9762 - val_loss: 3.3598 - val_accuracy: 0.6197
Epoch 71/200
42/42 [==============================] - 15s 363ms/step - loss: 0.1639 - accuracy: 0.9667 - val_loss: 4.2676 - val_accuracy: 0.5704
Epoch 72/200
42/42 [==============================] - 15s 365ms/step - loss: 0.1601 - accuracy: 0.9667 - val_loss: 3.3348 - val_accuracy: 0.6408
Epoch 73/200
42/42 [==============================] - 15s 363ms/step - loss: 0.2626 - accuracy: 0.9667 - val_loss: 2.9382 - val_accuracy: 0.6479
Epoch 74/200
42/42 [==============================] - 15s 362ms/step - loss: 0.2013 - accuracy: 0.9762 - val_loss: 2.9589 - val_accuracy: 0.6408
Epoch 75/200
42/42 [==============================] - 15s 361ms/step - loss: 0.0639 - accuracy: 0.9857 - val_loss: 3.3422 - val_accuracy: 0.5986
Epoch 76/200
42/42 [==============================] - 15s 363ms/step - loss: 0.0792 - accuracy: 0.9810 - val_loss: 2.9832 - val_accuracy: 0.6620
Epoch 77/200
42/42 [==============================] - 15s 364ms/step - loss: 0.0570 - accuracy: 0.9857 - val_loss: 3.0069 - val_accuracy: 0.6690
Epoch 78/200
42/42 [==============================] - 15s 362ms/step - loss: 0.1412 - accuracy: 0.9857 - val_loss: 3.2859 - val_accuracy: 0.6690
Epoch 79/200
42/42 [==============================] - 15s 361ms/step - loss: 0.0576 - accuracy: 0.9810 - val_loss: 4.4903 - val_accuracy: 0.5563
Epoch 80/200
42/42 [==============================] - 15s 363ms/step - loss: 0.1879 - accuracy: 0.9667 - val_loss: 4.0252 - val_accuracy: 0.5563
Epoch 81/200
42/42 [==============================] - 15s 362ms/step - loss: 0.2431 - accuracy: 0.9381 - val_loss: 3.9363 - val_accuracy: 0.5915
Epoch 82/200
42/42 [==============================] - 15s 361ms/step - loss: 0.1515 - accuracy: 0.9667 - val_loss: 3.1591 - val_accuracy: 0.6408
Epoch 83/200
42/42 [==============================] - 15s 362ms/step - loss: 0.0102 - accuracy: 0.9952 - val_loss: 3.2909 - val_accuracy: 0.6197
Epoch 84/200
42/42 [==============================] - 15s 369ms/step - loss: 0.0318 - accuracy: 0.9905 - val_loss: 3.7883 - val_accuracy: 0.5845
Epoch 85/200
42/42 [==============================] - 15s 365ms/step - loss: 0.0732 - accuracy: 0.9810 - val_loss: 3.3367 - val_accuracy: 0.6338
Epoch 86/200
42/42 [==============================] - 15s 366ms/step - loss: 0.0376 - accuracy: 0.9905 - val_loss: 3.7622 - val_accuracy: 0.6127
Epoch 87/200
42/42 [==============================] - 15s 365ms/step - loss: 0.0901 - accuracy: 0.9857 - val_loss: 3.9197 - val_accuracy: 0.6479
Epoch 88/200
42/42 [==============================] - 15s 367ms/step - loss: 0.1051 - accuracy: 0.9762 - val_loss: 3.5323 - val_accuracy: 0.6690
Epoch 89/200
42/42 [==============================] - 15s 367ms/step - loss: 0.0535 - accuracy: 0.9905 - val_loss: 3.5348 - val_accuracy: 0.6268
Epoch 90/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0497 - accuracy: 0.9952 - val_loss: 4.1677 - val_accuracy: 0.5845
Epoch 91/200
42/42 [==============================] - 15s 366ms/step - loss: 0.1228 - accuracy: 0.9905 - val_loss: 4.4428 - val_accuracy: 0.5704
Epoch 92/200
42/42 [==============================] - 15s 368ms/step - loss: 0.3404 - accuracy: 0.9524 - val_loss: 3.3655 - val_accuracy: 0.6197
Epoch 93/200
42/42 [==============================] - 15s 367ms/step - loss: 0.2027 - accuracy: 0.9810 - val_loss: 3.8378 - val_accuracy: 0.6127
Epoch 94/200
42/42 [==============================] - 15s 366ms/step - loss: 0.1769 - accuracy: 0.9714 - val_loss: 3.1176 - val_accuracy: 0.6479
Epoch 95/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0630 - accuracy: 0.9857 - val_loss: 3.1713 - val_accuracy: 0.6761
Epoch 96/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0391 - accuracy: 0.9810 - val_loss: 3.1849 - val_accuracy: 0.6972
Epoch 97/200
42/42 [==============================] - 15s 367ms/step - loss: 0.0467 - accuracy: 0.9857 - val_loss: 3.5254 - val_accuracy: 0.6197
Epoch 98/200
42/42 [==============================] - 15s 366ms/step - loss: 0.1356 - accuracy: 0.9857 - val_loss: 3.8755 - val_accuracy: 0.6479
Epoch 99/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0596 - accuracy: 0.9857 - val_loss: 4.3422 - val_accuracy: 0.6056
Epoch 100/200
42/42 [==============================] - 15s 367ms/step - loss: 0.1034 - accuracy: 0.9762 - val_loss: 3.7196 - val_accuracy: 0.6479
Epoch 101/200
42/42 [==============================] - 15s 366ms/step - loss: 0.0768 - accuracy: 0.9857 - val_loss: 2.9536 - val_accuracy: 0.6901
Epoch 102/200
42/42 [==============================] - 15s 366ms/step - loss: 0.1477 - accuracy: 0.9714 - val_loss: 3.2976 - val_accuracy: 0.6549
Epoch 103/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0502 - accuracy: 0.9857 - val_loss: 3.7025 - val_accuracy: 0.6338
Epoch 104/200
42/42 [==============================] - 15s 367ms/step - loss: 0.2449 - accuracy: 0.9810 - val_loss: 3.3066 - val_accuracy: 0.6831
Epoch 105/200
42/42 [==============================] - 15s 369ms/step - loss: 0.0272 - accuracy: 0.9905 - val_loss: 3.2070 - val_accuracy: 0.6620
Epoch 106/200
42/42 [==============================] - 15s 367ms/step - loss: 0.0055 - accuracy: 0.9952 - val_loss: 3.5586 - val_accuracy: 0.6408
Epoch 107/200
42/42 [==============================] - 15s 367ms/step - loss: 0.0948 - accuracy: 0.9857 - val_loss: 3.6657 - val_accuracy: 0.5775
Epoch 108/200
42/42 [==============================] - 15s 366ms/step - loss: 0.0335 - accuracy: 0.9952 - val_loss: 3.6026 - val_accuracy: 0.5634
Epoch 109/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0740 - accuracy: 0.9857 - val_loss: 3.6745 - val_accuracy: 0.5634
Epoch 110/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0109 - accuracy: 0.9952 - val_loss: 3.4832 - val_accuracy: 0.5845
Epoch 111/200
42/42 [==============================] - 15s 370ms/step - loss: 0.0889 - accuracy: 0.9762 - val_loss: 3.2334 - val_accuracy: 0.6338
Epoch 112/200
42/42 [==============================] - 15s 368ms/step - loss: 0.0610 - accuracy: 0.9810 - val_loss: 4.2257 - val_accuracy: 0.6056
Epoch 113/200
42/42 [==============================] - 15s 369ms/step - loss: 2.5253e-04 - accuracy: 1.0000 - val_loss: 4.2005 - val_accuracy: 0.5986
Epoch 114/200
42/42 [==============================] - 15s 369ms/step - loss: 0.0737 - accuracy: 0.9857 - val_loss: 3.9294 - val_accuracy: 0.6338
Epoch 115/200
42/42 [==============================] - 15s 371ms/step - loss: 0.0635 - accuracy: 0.9905 - val_loss: 4.2533 - val_accuracy: 0.6408
Epoch 116/200
42/42 [==============================] - 15s 371ms/step - loss: 0.0650 - accuracy: 0.9857 - val_loss: 3.8322 - val_accuracy: 0.6408
Epoch 117/200
42/42 [==============================] - 15s 370ms/step - loss: 0.0510 - accuracy: 0.9857 - val_loss: 4.5183 - val_accuracy: 0.6056
Epoch 118/200
42/42 [==============================] - 15s 368ms/step - loss: 0.3650 - accuracy: 0.9714 - val_loss: 3.8299 - val_accuracy: 0.6620
Epoch 119/200
42/42 [==============================] - 15s 367ms/step - loss: 0.0679 - accuracy: 0.9857 - val_loss: 4.3229 - val_accuracy: 0.6197
Epoch 120/200
42/42 [==============================] - 15s 368ms/step - loss: 0.1396 - accuracy: 0.9810 - val_loss: 5.0849 - val_accuracy: 0.6127
Epoch 121/200
42/42 [==============================] - 16s 372ms/step - loss: 0.1308 - accuracy: 0.9810 - val_loss: 4.1512 - val_accuracy: 0.6620
Epoch 122/200
42/42 [==============================] - 16s 373ms/step - loss: 0.0856 - accuracy: 0.9810 - val_loss: 3.9306 - val_accuracy: 0.6549
Epoch 123/200
42/42 [==============================] - 15s 370ms/step - loss: 0.1001 - accuracy: 0.9857 - val_loss: 3.4930 - val_accuracy: 0.6690
Epoch 124/200
42/42 [==============================] - 15s 367ms/step - loss: 0.1527 - accuracy: 0.9714 - val_loss: 3.8911 - val_accuracy: 0.6197
Epoch 125/200
42/42 [==============================] - 15s 368ms/step - loss: 0.1511 - accuracy: 0.9667 - val_loss: 4.2805 - val_accuracy: 0.6268
Epoch 126/200
42/42 [==============================] - 15s 366ms/step - loss: 0.0922 - accuracy: 0.9762 - val_loss: 5.5147 - val_accuracy: 0.5915
Epoch 127/200
42/42 [==============================] - 16s 374ms/step - loss: 0.0722 - accuracy: 0.9905 - val_loss: 5.3339 - val_accuracy: 0.5845
Epoch 128/200
42/42 [==============================] - 15s 370ms/step - loss: 0.1952 - accuracy: 0.9667 - val_loss: 4.7809 - val_accuracy: 0.5493
Epoch 129/200
42/42 [==============================] - 15s 369ms/step - loss: 0.0894 - accuracy: 0.9857 - val_loss: 4.2969 - val_accuracy: 0.5775
Epoch 130/200
42/42 [==============================] - 15s 368ms/step - loss: 0.1456 - accuracy: 0.9762 - val_loss: 4.0827 - val_accuracy: 0.6197
Epoch 131/200
42/42 [==============================] - 16s 380ms/step - loss: 0.3461 - accuracy: 0.9667 - val_loss: 4.6653 - val_accuracy: 0.6268
Epoch 132/200
42/42 [==============================] - 16s 376ms/step - loss: 0.1053 - accuracy: 0.9857 - val_loss: 4.5893 - val_accuracy: 0.6408
Epoch 133/200
42/42 [==============================] - 16s 379ms/step - loss: 0.0409 - accuracy: 0.9810 - val_loss: 4.1805 - val_accuracy: 0.6761
Epoch 134/200
42/42 [==============================] - 16s 373ms/step - loss: 0.0037 - accuracy: 0.9952 - val_loss: 4.1702 - val_accuracy: 0.6620
Epoch 135/200
42/42 [==============================] - 16s 376ms/step - loss: 0.0567 - accuracy: 0.9810 - val_loss: 4.2528 - val_accuracy: 0.6268
Epoch 136/200
42/42 [==============================] - 15s 371ms/step - loss: 0.0973 - accuracy: 0.9905 - val_loss: 3.9560 - val_accuracy: 0.6549
Epoch 137/200
42/42 [==============================] - 15s 370ms/step - loss: 0.0731 - accuracy: 0.9905 - val_loss: 3.8633 - val_accuracy: 0.6268
Epoch 138/200
42/42 [==============================] - 16s 380ms/step - loss: 0.1613 - accuracy: 0.9857 - val_loss: 3.8864 - val_accuracy: 0.5775
Epoch 139/200
42/42 [==============================] - 16s 378ms/step - loss: 0.1190 - accuracy: 0.9810 - val_loss: 4.4565 - val_accuracy: 0.5775
Epoch 140/200
42/42 [==============================] - 15s 368ms/step - loss: 0.1699 - accuracy: 0.9810 - val_loss: 4.5863 - val_accuracy: 0.6056
Epoch 141/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0281 - accuracy: 0.9810 - val_loss: 3.7630 - val_accuracy: 0.6831
Epoch 142/200
42/42 [==============================] - 16s 381ms/step - loss: 0.0371 - accuracy: 0.9905 - val_loss: 4.3993 - val_accuracy: 0.6268
Epoch 143/200
42/42 [==============================] - 16s 382ms/step - loss: 0.0622 - accuracy: 0.9952 - val_loss: 4.0806 - val_accuracy: 0.6549
Epoch 144/200
42/42 [==============================] - 16s 382ms/step - loss: 0.0636 - accuracy: 0.9905 - val_loss: 3.9622 - val_accuracy: 0.6620
Epoch 145/200
42/42 [==============================] - 16s 382ms/step - loss: 0.0568 - accuracy: 0.9905 - val_loss: 4.1947 - val_accuracy: 0.6549
Epoch 146/200
42/42 [==============================] - 16s 383ms/step - loss: 0.0734 - accuracy: 0.9952 - val_loss: 3.7089 - val_accuracy: 0.6690
Epoch 147/200
42/42 [==============================] - 16s 385ms/step - loss: 0.0035 - accuracy: 0.9952 - val_loss: 3.7228 - val_accuracy: 0.6549
Epoch 148/200
42/42 [==============================] - 16s 383ms/step - loss: 0.2080 - accuracy: 0.9762 - val_loss: 4.1512 - val_accuracy: 0.5986
Epoch 149/200
42/42 [==============================] - 16s 382ms/step - loss: 0.0053 - accuracy: 0.9952 - val_loss: 4.0288 - val_accuracy: 0.6408
Epoch 150/200
42/42 [==============================] - 16s 380ms/step - loss: 0.1201 - accuracy: 0.9905 - val_loss: 3.5606 - val_accuracy: 0.6831
Epoch 151/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0510 - accuracy: 0.9952 - val_loss: 3.8266 - val_accuracy: 0.6831
Epoch 152/200
42/42 [==============================] - 16s 383ms/step - loss: 0.0056 - accuracy: 0.9952 - val_loss: 3.8662 - val_accuracy: 0.6479
Epoch 153/200
42/42 [==============================] - 16s 385ms/step - loss: 0.0719 - accuracy: 0.9857 - val_loss: 3.2341 - val_accuracy: 0.6901
Epoch 154/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0291 - accuracy: 0.9905 - val_loss: 3.9150 - val_accuracy: 0.6620
Epoch 155/200
42/42 [==============================] - 16s 385ms/step - loss: 0.0077 - accuracy: 0.9952 - val_loss: 3.6480 - val_accuracy: 0.6901
Epoch 156/200
42/42 [==============================] - 16s 384ms/step - loss: 0.1182 - accuracy: 0.9857 - val_loss: 4.4275 - val_accuracy: 0.6620
Epoch 157/200
42/42 [==============================] - 16s 381ms/step - loss: 0.0915 - accuracy: 0.9857 - val_loss: 4.2538 - val_accuracy: 0.6620
Epoch 158/200
42/42 [==============================] - 16s 383ms/step - loss: 0.0540 - accuracy: 0.9905 - val_loss: 4.3135 - val_accuracy: 0.6268
Epoch 159/200
42/42 [==============================] - 16s 383ms/step - loss: 0.1379 - accuracy: 0.9810 - val_loss: 4.1699 - val_accuracy: 0.6408
Epoch 160/200
42/42 [==============================] - 16s 382ms/step - loss: 0.1105 - accuracy: 0.9857 - val_loss: 4.5657 - val_accuracy: 0.6127
Epoch 161/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0789 - accuracy: 0.9952 - val_loss: 5.9129 - val_accuracy: 0.5563
Epoch 162/200
42/42 [==============================] - 16s 381ms/step - loss: 0.1000 - accuracy: 0.9857 - val_loss: 6.8696 - val_accuracy: 0.5563
Epoch 163/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0305 - accuracy: 0.9905 - val_loss: 5.6172 - val_accuracy: 0.6268
Epoch 164/200
42/42 [==============================] - 16s 382ms/step - loss: 0.0096 - accuracy: 0.9952 - val_loss: 5.3447 - val_accuracy: 0.6268
Epoch 165/200
42/42 [==============================] - 16s 382ms/step - loss: 0.0783 - accuracy: 0.9952 - val_loss: 4.4530 - val_accuracy: 0.6761
Epoch 166/200
42/42 [==============================] - 16s 384ms/step - loss: 0.1154 - accuracy: 0.9905 - val_loss: 5.3148 - val_accuracy: 0.5845
Epoch 167/200
42/42 [==============================] - 16s 385ms/step - loss: 0.0582 - accuracy: 0.9857 - val_loss: 5.3868 - val_accuracy: 0.6197
Epoch 168/200
42/42 [==============================] - 16s 386ms/step - loss: 0.0343 - accuracy: 0.9952 - val_loss: 5.1869 - val_accuracy: 0.6056
Epoch 169/200
42/42 [==============================] - 16s 381ms/step - loss: 0.1957 - accuracy: 0.9857 - val_loss: 6.0718 - val_accuracy: 0.5915
Epoch 170/200
42/42 [==============================] - 16s 382ms/step - loss: 0.1490 - accuracy: 0.9857 - val_loss: 6.3423 - val_accuracy: 0.5704
Epoch 171/200
42/42 [==============================] - 16s 384ms/step - loss: 0.1534 - accuracy: 0.9857 - val_loss: 5.3125 - val_accuracy: 0.6268
Epoch 172/200
42/42 [==============================] - 16s 384ms/step - loss: 0.1573 - accuracy: 0.9905 - val_loss: 5.4818 - val_accuracy: 0.6268
Epoch 173/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0250 - accuracy: 0.9952 - val_loss: 5.8140 - val_accuracy: 0.6408
Epoch 174/200
42/42 [==============================] - 16s 385ms/step - loss: 0.0181 - accuracy: 0.9952 - val_loss: 5.4369 - val_accuracy: 0.5845
Epoch 175/200
42/42 [==============================] - 16s 384ms/step - loss: 0.1913 - accuracy: 0.9857 - val_loss: 4.8012 - val_accuracy: 0.5986
Epoch 176/200
42/42 [==============================] - 16s 384ms/step - loss: 0.0073 - accuracy: 0.9952 - val_loss: 5.2953 - val_accuracy: 0.5634
Epoch 177/200
42/42 [==============================] - 16s 385ms/step - loss: 0.1024 - accuracy: 0.9810 - val_loss: 5.1965 - val_accuracy: 0.6127
Epoch 178/200
42/42 [==============================] - 16s 383ms/step - loss: 0.0978 - accuracy: 0.9857 - val_loss: 5.8964 - val_accuracy: 0.6408
Epoch 179/200
42/42 [==============================] - 16s 383ms/step - loss: 0.0882 - accuracy: 0.9905 - val_loss: 6.9194 - val_accuracy: 0.6056
Epoch 180/200
42/42 [==============================] - 16s 382ms/step - loss: 0.1981 - accuracy: 0.9857 - val_loss: 5.9908 - val_accuracy: 0.6338
Epoch 181/200
42/42 [==============================] - 16s 381ms/step - loss: 0.0582 - accuracy: 0.9905 - val_loss: 5.9898 - val_accuracy: 0.6408
Epoch 182/200
42/42 [==============================] - 16s 379ms/step - loss: 0.2245 - accuracy: 0.9762 - val_loss: 5.6543 - val_accuracy: 0.5915
Epoch 183/200
42/42 [==============================] - 16s 383ms/step - loss: 0.0141 - accuracy: 0.9905 - val_loss: 6.5006 - val_accuracy: 0.5634
Epoch 184/200
42/42 [==============================] - 16s 386ms/step - loss: 0.2954 - accuracy: 0.9762 - val_loss: 5.1639 - val_accuracy: 0.6408
Epoch 185/200
42/42 [==============================] - 16s 385ms/step - loss: 0.0731 - accuracy: 0.9952 - val_loss: 5.2009 - val_accuracy: 0.6901
Epoch 186/200
42/42 [==============================] - 16s 386ms/step - loss: 0.0653 - accuracy: 0.9857 - val_loss: 5.8856 - val_accuracy: 0.6690
Epoch 187/200
42/42 [==============================] - 16s 385ms/step - loss: 0.1170 - accuracy: 0.9905 - val_loss: 5.2181 - val_accuracy: 0.6549
Epoch 188/200
42/42 [==============================] - 16s 386ms/step - loss: 0.1895 - accuracy: 0.9810 - val_loss: 4.5151 - val_accuracy: 0.6690
Epoch 189/200
42/42 [==============================] - 16s 390ms/step - loss: 0.1125 - accuracy: 0.9905 - val_loss: 4.9886 - val_accuracy: 0.6972
Epoch 190/200
42/42 [==============================] - 16s 394ms/step - loss: 0.0930 - accuracy: 0.9905 - val_loss: 5.0631 - val_accuracy: 0.6831
Epoch 191/200
42/42 [==============================] - 16s 393ms/step - loss: 0.0735 - accuracy: 0.9905 - val_loss: 4.6383 - val_accuracy: 0.6901
Epoch 192/200
42/42 [==============================] - 16s 396ms/step - loss: 0.0261 - accuracy: 0.9905 - val_loss: 4.9773 - val_accuracy: 0.6549
Epoch 193/200
42/42 [==============================] - 16s 396ms/step - loss: 0.0016 - accuracy: 1.0000 - val_loss: 5.6043 - val_accuracy: 0.6479
Epoch 194/200
42/42 [==============================] - 16s 395ms/step - loss: 5.6601e-04 - accuracy: 1.0000 - val_loss: 5.6145 - val_accuracy: 0.6408
Epoch 195/200
42/42 [==============================] - 16s 391ms/step - loss: 0.0119 - accuracy: 0.9905 - val_loss: 4.9712 - val_accuracy: 0.6831
Epoch 196/200
42/42 [==============================] - 16s 393ms/step - loss: 0.0266 - accuracy: 0.9952 - val_loss: 4.9249 - val_accuracy: 0.6831
Epoch 197/200
42/42 [==============================] - 16s 393ms/step - loss: 0.1385 - accuracy: 0.9952 - val_loss: 4.2090 - val_accuracy: 0.7183
Epoch 198/200
42/42 [==============================] - 16s 394ms/step - loss: 0.1222 - accuracy: 0.9905 - val_loss: 4.7764 - val_accuracy: 0.6761
Epoch 199/200
42/42 [==============================] - 16s 396ms/step - loss: 0.0546 - accuracy: 0.9952 - val_loss: 4.4567 - val_accuracy: 0.6620
Epoch 200/200
42/42 [==============================] - 16s 378ms/step - loss: 0.0866 - accuracy: 0.9857 - val_loss: 5.1646 - val_accuracy: 0.6479
```
