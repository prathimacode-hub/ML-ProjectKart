**TEXT CLASSIFICATION**

**GOAL**

The goal of this project is cto classify texts and label them as positive, negative or neutral. Texts classified as negative are further classified as suicidal or non-suicidal.

**DATASET**

You don't need to downlaod any dataset
- For Suicide_tendency_model, I have used dataset present online on github. Link : https://raw.githubusercontent.com/laxmimerit/twitter-suicidal-intention-dataset/master/twitter-suicidal_data.csv
- For fetching live tweets, one needs to create a csv file containing credentials to access twitter tokens, demonstration of which is shown in this particular youtube video:  https://youtu.be/ujId4ipkBio

**DESCRIPTION**

I have created two models namely twitter sentiment analysis and suicide tendancy model. I have created suicide tendancy model using Linear SVC which can identify tendency of commiting suicide or indication of facing stress, depression, etc. from the text with an accuracy of about 93%. Then I saved this model in '.sav' format. I have imported this saved model in twitter sentiment analysis model which can fetch live tweets from twitter and classify them into positive, negative and neutral tweets using textblob library.
Tweets labeled as negative are passed through the imported suicide tendency model which can further identifies if any suicidal thoughts faced by the user of a particular tweet.

**WHAT I HAD DONE**

- Load the dataset for detecting suicidal tendency, link for which is specified above
- clean the text, by removing hashtags, links, etc.
- Created a Pipeline for vectorizing the text and applying Liner SVC
- Saved the state of model in '.sav' format
- Created a CSV file specifying login credentials and API tokens for fetching live tweets
- fetch live tweets
- Cleaned tweets by removing hashtags, links, etc.
- Classified tweets using textblob
- Tweets labeled negtive were further passed through the suicide tendency model saved and identified if a tweet indicates suicidal thoughts.

**MODELS USED**

- Linear SVC

**LIBRARIES NEEDED**

- tweepy
- textblob
- pipeline
- wordcloud
- pandas
- numpy
- matplotlib
- TfidfVectorizer

**ACCURACIES**

- Accuracy of Suicide Tendency model is 93%. </br>
![image](https://user-images.githubusercontent.com/59737567/138963243-7342ef1b-5098-4bda-9876-a7a0355d83ed.png)

- Tweets that are identified to be suicidal are filtered out.
![image](https://user-images.githubusercontent.com/59737567/138963043-b7e159a2-97e1-4142-ad22-b4eec48a8532.png)

**CONCLUSION**

Thus the model developed can be used to identify the suicidal thoughts on social media and other discussion forums, which can further be useful in reavhng out help to the users.

**Nikita Emberi**

[@NikitaEmberi](https://github.com/NikitaEmberi)
