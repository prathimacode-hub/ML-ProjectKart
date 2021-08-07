# Named Entity Recognition

Named-entity recognition is a information extraction that seeks to locate and classify named entities in an unstructured text into pre-defined categories such as person names, organizations, 
locations, medical codes, time expressions, quantities, monetary values, percentages, etc. 

## Goal
The Goal of this project is to use Deep Learning methods to identify Named Entities 

## Dataset 
The dataset is available in Kaggle, Here is the Link: https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus, Also I have made the CSV file available in Dataset folder

## What Have I done

1. Import all the required libraries
2. Load the dataset in Pandas Dataframe
3. Analyze the length of sentences and Process the Data
4. Experimented with Various deep learning models such as LSTM, GRU, Bidirectional GRU, Bidirectional LSTM
5. Evaluate the metric(Accuracy)

## Libraries I have used

1. Pandas
2. Livelossplot
3. Matplotlib
4. Scikit-learn
5. Tensorflow

## Model Comparison
We have  used four different deep learning models, here is the accuracy

|Name of the Model|Accuracy Score|
|:---:|:---:|
|LSTM|0.9812|
|GRU|0.982|
|Bidirectional GRU|0.985|
|Bidirectional LSTM|0.9845|

## Conclusion

From the above comparision, we can notice that accuracies of all the deep learning models are mostly same and it performs best, we can use LSTM/GRU as a final model, since it is much faster to train, we can use this model

## Sean Benhur

You can connect with me here on [LinkedIn](https://www.linkedin.com/in/seanbenhur/) and Twitter(https://twitter.com/seanbenhur)
