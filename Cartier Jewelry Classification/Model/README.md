# Cartier Jewelry Classification
Cartier International SNC, or simply Cartier (/ˈkɑːrtieɪ/; French: [kaʁtje]), is a French luxury goods conglomerate which designs, manufactures, distributes, and sells jewellery and watches. Founded by Louis-François Cartier in Paris in 1847, the company remained under family control until 1964. The company maintains its headquarters in Paris, although it is a wholly owned subsidiary of the Swiss Richemont Group. Cartier operates more than 200 stores in 125 countries, with three Temples (Historical Maisons) in London, New York, and Paris.

Cartier is regarded as one of the most prestigious jewellery manufacturers in the world. In 2018, it is ranked by Forbes as the world's 59th most valuable brand. Cartier has a long history of sales to royalty. King Edward VII of Great Britain referred to Cartier as "the jeweller of kings and the king of jewellers." For his coronation in 1902, Edward VII ordered 27 tiaras and issued a royal warrant to Cartier in 1904. Similar warrants soon followed from the courts of Spain, Portugal, Russia and the House of Orlean

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-31/Cartier%20Jewelry%20Classification/Images/cart8.jpeg)

## Dataset
The Dataset is collected from Kaggle website. Here is the link : https://www.kaggle.com/marcelopesse/cartier-jewelry-catalog?select=cartier_catalog.csv. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-31/Cartier%20Jewelry%20Classification/Dataset) folder too, you can access that!

## Goal
The goal of this project is to make a classification model, which will classify the jewelries based on the various features.

## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-31/Cartier%20Jewelry%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Exploratory Data Analysis
    - Which gem are mostly used in the products?
    - Which metal mostly used in Cartier Jewellery?
    - How much is the mean of Cartier jewellery as metal type?
    - How much the mean price for every metal type in cartier jewels?
    - How many gems in every jewels category?
    - How much the gem price in every jewels category?
    - Which gem is the most expensive?
4. Classification Model
    - KNN Classifier
    - Logistic Regression
    - Random Forest Classifier
    - Support Vector Machine Classifier
    - XgBoost Classifier
    - Gaussian Naive Bayes
    - Decision Tree Classifier
5. Model Comparison
6. Conclusion

## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. XgBoost
5. Sklearn
6. seaborn
**********************************************************
## Data Analysis
1. **Which gem are mostly used in the products?**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-31/Cartier%20Jewelry%20Classification/Images/cart1.png)

2. **Which metal mostly used in Cartier Jewellery?**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-31/Cartier%20Jewelry%20Classification/Images/cart2.png)

### For more Data Analysis, check out the [`Images`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-31/Cartier%20Jewelry%20Classification/Images) folder!

**********************************************************************

## Comparative analysis among the algorithms for this project

We have deployed six machine learning algorithms and every algorithm is deployed successfully without any hesitation. We have checked the accuracy of the models based on the accuracy score of each of the models. Now let's take a look at the scores of each models.

|Name of the Model|Accuracy Score|
|:---:|:---:|
|Logistic Regression|0.37|
|Decision Tree Classifier|0.81|
|Random Forest Classifier|0.60|
|Gausian NB Algorithm|0.37|
|KNN Algorithm|0.43|
|Support Vector Machine Algorithm|0.36|
|XgBoost Classifier|0.82|

**Comparing all those scores scored by the machine learning algorithms, it is clear that XgBoost Classifier is having the upper hand in case of this dataset and after this, we can use Decision Tree algorithm, which is also having good score as compared to the other deployed algorithms**

Best Fitted Models ranking - 
1. XgBoost Classifier
2. Decision Tree Classifier
3. Random Forest Classifier
4. KNN Algorithm
5. Logistic Regression
6. Gausian NB Algorithm
7. Support Vector Machine


Hooray!! The models are deployed successfully!
*******************************************************
## Conclusion
1. 66 percent of the product have diamonds in them, more than any other gems, Its most popular gem. onyx and emeralds are into the next ranks.
2.  Jewels type include 4 category: rings, earring, necklaces and bracelets
Ranks of metals in every category are the same and equal: 1.White Gold 2.Pink Gold 3.Yellow Gold 4.Platinum 5.Non-Rhodiumized White Gold
3.  In every category Platinum in most valuable metal with a huge difference in price as $. After that White Gold have a second place but other metals are close in price for every category
4. As we saw earlier Platinium is the most valuable metal that the Cartier used in jewels. The mean price of Platinium jewels is more than 40000 Dollars after that white metal is second. "Yellow Gold" and "Non-Rhodiumized White Gold" are about equal in mean price, in last is pink gold with mean of 15000 Dollars that is about one of third of Platinium
5.  In all categories, diamond is the most popular gem in the making of jewelry. Exceedingly over 100 ring types include diamonds, in most cases more than one piece of diamond. This also rules for other categories of jewelry such as earrings, necklaces, and bracelets. Variety of the gems used in rings and bracelets are more than earrings and necklaces. Furthermore, Sapphires are also a popular gem used in ring production.
6. Earrings, Necklaces, and Rings with Rubies(gem) has a huge difference in the price of jewelry, but Emeralds(gem) in Bracelets shows the is a key factor in price determination. A closer look at necklaces reveals us that Tsavorite garnet has third place in price.
7. This plot shows us the mean price of products with gems on them As we could have predicted products that have Rubies on them are the most expensive jewelry in Cartier products. the next ranks belong to Tsavorite garnets, Emeralds, and the Chrysoprase. The middle gems on the above figure are equal in mean price
8. Comparing all those scores scored by the machine learning algorithms, it is clear that XgBoost Classifier is having the upper hand in case of this dataset and after this, we can use Decision Tree algorithm, which is also having good score as compared to the other deployed algorithms

****************************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
