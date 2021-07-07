# Text Summarization
Summarization is the task of condensing a piece of text to a shorter version, reducing the size of the initial text while at the same time preserving key informational elements and the meaning of content. Since manual text summarization is a time expensive and generally laborious task, the automatization of the task is gaining increasing popularity and therefore constitutes a strong motivation for academic research.

There are important applications for text summarization in various NLP related tasks such as text classification, question answering, legal texts summarization, news summarization, and headline generation. Moreover, the generation of summaries can be integrated into these systems as an intermediate stage which helps to reduce the length of the document.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-44/Text%20Summarization/Images/txt1.png)

## Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset : https://www.kaggle.com/pariza/bbc-news-summary. I have uploaded the same in [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-44/Text%20Summarization/Dataset) folder too, you can access that!

### Goal
The goal of this project is to create a model which will summarize the articles given by the users. In addition I will be creating a Python function to make the model more user friendly!
***********************
## What Have I done?
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-44/Text%20Summarization/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.
3. Data Pre-processing
4. Data Cleaning
5. Model creation
    - Spliting the dataset
    - Visualizing the attributes
    - Vectorization
    - Final Model Creation
    - Inference
6. Additional! Creating a Python function
7. Conclusion

***********************
## Libraries used
1. Numpy
2. Pandas
3. Matplotlib
4. Sklearn 
5. Seaborn
6. Tensorflow
7. nltk

******************************
## Data Visualization
- **Visualizing the Dataset based on Article and Summary**

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-44/Text%20Summarization/Images/txt2.png) ![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-44/Text%20Summarization/Images/txt3.png)
******************************
## Model Inference
![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-44/Text%20Summarization/Images/txt4.png)

********************************
## Conclusion
* Text Summarization models are one of the hot topics of the deep learning model deployment.
* **Recurrent Neural Network** is the best choice for this kind of topics.
* Here we have used **Long Short Term Memory**, which shows the validation loss of 6.49 only, which shows the accuracy of the model.
* After inference, the model's validation loss decreased, and it is only 4.58.
* LSTM on Inference is the best model to be fitted with this dataset.
* Hence, the **Text Summarization Model** successfully deployed and working properly.
* Last but not the least, the python function is made with **Sequence to Sequence Model**, which makes the function user friendly!

************************************
## Author
Code Contributed by, Abhishek Sharma, 2021 @abhisheks008 #LGMSOC21
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
