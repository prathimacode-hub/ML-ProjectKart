# Mobile Price Range Classification

## Data Visualization 

![](https://github.com/Isha307/ML-ProjectKart/blob/main/Mobile%20Price%20Range%20Classification/Image/Price-Range.png)

## Columns: 

* battery_power: Battry power 

* blue:  Bluetooth or not

* clock_speed: microprocessor speed to executes instructions

* dual_sim: Dual sim or not

* fc:Front Camera mega pixel

* four_g:Has 4G or not

* int_memory: Internal Memory

* m_dep: Mobile Dept

* mobile_wt: Weight

* n_cores: Number of cores of processor

* pc:Primary Camera mega pixels

* px_height: Pixel Resolution Height

* px_width: Pixel Resolution Width

* ram: RAM

* sc_h: Screen Height

* sc_w: Screen Width

* talk_time: Aingle battery charge's longest time

* three_g: 3G or not

* touch_screen: Touch screen or not

* wifi: Wifi or not

 I created a model that with the help of [train.csv](https://github.com/Isha307/ML-ProjectKart/blob/main/Mobile%20Price%20Range%20Classification/Dataset/data1/train.csv) 
 and tested it on the [test.csv](https://github.com/Isha307/ML-ProjectKart/blob/main/Mobile%20Price%20Range%20Classification/Dataset/data1/test.csv). 
 
 # Algorithm Used
  
  ## "Linear Regression"
  
  ## "KNN"
  
  ## "SVM" 
  
  ## "Naive Bayes"
    
  ## "Decisiontree"
   
  ## "RandomForest"
   
  ## "LogisticRegression"

# Libraries Needed
  
 * pandas 
  
 * numpy 
  
 * matplotlib

 * seaborn
 
 * sklearn
 

# CONCLUSION
```
Linear Regression
Score:  0.917989082336092

KNN
Score:  0.9133333333333333

SVM
Score:  0.95

Naive Bayes
Score:  0.835

Decisiontree
Score:  0.8283333333333334

RandomForest
Score:  0.8866666666666667

LogisticRegression
Score:  0.6533333333333333
```

>>We used SVM because it has the highest score among all other algorithm. 
