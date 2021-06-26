# 🧬 DNA Sequencing Classification 

A genome is a complete collection of DNA in an organism. All living species possess a genome, but they differ considerably in size. The human genome, for instance, is arranged into 23 chromosomes, which is a little bit like an encyclopedia being organized into 23 volumes. And if you counted all the characters (individual DNA “base pairs”), there would be more than 6 billion in each human genome. So it’s a huge compilation. A human genome has about 6 billion characters or letters. If you think the genome(the complete DNA sequence) is like a book, it is a book about 6 billion letters of “A”, “C”, “G” and “T”. Now, everyone has a unique genome. Nevertheless, scientists find most parts of the human genomes are alike to each other. As a data-driven science, genomics extensively utilizes machine learning to capture dependencies in data and infer new biological hypotheses. Nonetheless, the ability to extract new insights from the exponentially increasing volume of genomics data requires more powerful machine learning models. By efficiently leveraging large data sets, deep learning has reconstructed fields such as computer vision and natural language processing. It has become the method of preference for many genomics modeling tasks, including predicting the influence of genetic variation on gene regulatory mechanisms such as DNA receptiveness and splicing.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-22/DNA%20Sequencing%20Classification/Images/dna1.jpg)

## :diamond_shape_with_a_dot_inside: Goal
In this project, we will understand how to interpret a DNA structure and how machine learning algorithms can be used to build a prediction model on DNA sequence data.

## :diamond_shape_with_a_dot_inside: Dataset
The datasets that I am going to use are,
1. Human DNA Data
2. Chimpanzee DNA Data
3. Dog DNA Data
4. DNA Fasta format for BioPython
You can get all the datasets from the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-22/DNA%20Sequencing%20Classification/Dataset) folder.


## :diamond_shape_with_a_dot_inside: What Have I done :question:
1. Importing all the required libraries. Check [`requirements.txt`](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-22/DNA%20Sequencing%20Classification/requirements.txt).
2. Upload the dataset and the Jupyter Notebook file.

:heavy_check_mark: Then I followed these steps -

3. How is data sequence represented?
4. DNA data handling using BioPython
5. Ordinal encoding DNA sequence data
6. One-hot encoding DNA sequence data
7. K-mer counting
8. Loading and visualizing DNA data
9. Classification Models
    - Human DNA Dataset
        - Multinomial Naive Bayes
        - Random Forest Classifier
        - Decision Tree Classifier
        - K-Nearest Neighbours Classifier
        - Model Comparison
    - Chimpanzee DNA Dataset
        - Multinomial Naive Bayes
        - Random Forest Classifier
        - Decision Tree Classifier
        - K-Nearest Neighbours Classifier  
        - Model Comparison
    - Dog DNA Dataset
        - Multinomial Naive Bayes
        - Random Forest Classifier
        - Decision Tree Classifier
        - K-Nearest Neighbours Classifier
        - Model Comparison
    - More Interesting models!
        - Predicting Chimpanzee DNA using Human dataet trained model
        - Predicting Dog DNA using Human dataset trained model
        - Model Comparison
10. Conclusion

## :diamond_shape_with_a_dot_inside: Libraries used
1. Numpy
2. Seaborn
3. Pandas
4. Matplotlib
5. Sklearn
6. BioPython

## :diamond_shape_with_a_dot_inside: Visualization of the DNA Data
:large_orange_diamond: **Visualizing the Human DNA Data** -

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-22/DNA%20Sequencing%20Classification/Images/dna2.png)

:large_orange_diamond: **Visualizing the Human DNA Data** -

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-22/DNA%20Sequencing%20Classification/Images/dna3.png)

:large_orange_diamond: **Visualizing the Human DNA Data** -

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-22/DNA%20Sequencing%20Classification/Images/dna4.png)

## :diamond_shape_with_a_dot_inside: Model Comparison
I have deployed four classification algorithms for each of the three dataset [Human, Chimpanzee and Dog]. Now let's compare all of them!

------------------------------------

### :large_orange_diamond: Model Comparison on `Human DNA Dataset`

I have deployed four classification algorithms for the Human DNA Dataset. Now let's check the accuracy of the models and find out which model is highly efficient!

|Name of the model|Accuracy Score|
|:---:|:---:|
|Multinomial Naive Bayes Algorithm|0.98|
|Random Forest Classifier|0.92|
|Decision Tree Classifier|0.82|
|K-Nearest Neighbours Classifier|0.82|

**:heavy_check_mark: It is clearly visible that Multinomial Naive Bayes algorithm is perfectly suited for the Human DNA Dataset with an accuracy of more than 98%!**

---------------------------------------

### :large_orange_diamond: Model Comparison on `Chimpanzee DNA Dataset`

I have deployed four classification algorithms for the Chimpanzee DNA Dataset. Now let's check the accuracy of the models and find out which model is highly efficient!

|Name of the model|Accuracy Score|
|:---:|:---:|
|Multinomial Naive Bayes Algorithm|0.91|
|Random Forest Classifier|0.85|
|Decision Tree Classifier|0.77|
|K-Nearest Neighbours Classifier|0.68|

**:heavy_check_mark: It is clearly visible that Multinomial Naive Bayes algorithm is perfectly suited for the Human DNA Dataset with an accuracy of more than 91%!**

----------------------------------------

### :large_orange_diamond: Model Comparison on `Dog DNA Dataset`

I have deployed four classification algorithms for the Chimpanzee DNA Dataset. Now let's check the accuracy of the models and find out which model is highly efficient!

|Name of the model|Accuracy Score|
|:---:|:---:|
|Multinomial Naive Bayes Algorithm|0.69|
|Random Forest Classifier|0.59|
|Decision Tree Classifier|0.51|
|K-Nearest Neighbours Classifier|0.32|

**:heavy_check_mark: It is clearly visible that Multinomial Naive Bayes algorithm is perfectly suited for the Human DNA Dataset with an accuracy of more than 69%!**

--------------------------------------

## :arrow_forward: Some more Classification Model!
For 3 different datasets I have deployed four models for each of the datasets. But among all those deployed models, the model which is trained using the Human Dataset, is the best model. The Multinomial Naive Bayes Algorithm on the Human Dataset is the fitted algorithm.

|Name of the model|Accuracy Score|
|:---:|:---:|
|Multinomial Naive Bayes Algorithm on Human dataset|0.98|
|Multinomial Naive Bayes Algorithm on Chimpanzee dataset|0.91|
|Multinomial Naive Bayes Algorithm on dog dataset|0.69|

As the model trained on the human dataset is having higher accuracy, so I choose that model for further proceedings!

Now let's make something different with this highly fitted algorithm.

1. **Predicting Chimpanzee DNA using the Multinomial Naive Bayes (Human Model)**
2. **Predicting Dog DNA using the Multinomial Naive Bayes (Human Model)**

### :large_orange_diamond: Model Comparison
Now let's compare these two models -

|Name of the model|Accuracy Score|
|:---:|:---:|
|**Predicting Chimpanzee DNA using the Multinomial Naive Bayes (Human Model)**|0.99|
|**Predicting Dog DNA using the Multinomial Naive Bayes (Human Model)**|0.93|

----------------

## :diamond_shape_with_a_dot_inside: Conclusion
- **For Human dataset, Multinomial Naive Bayes algorithm is the best fitted algorithm.**
- **For Chimpanzee dataset, Multinomial Naive Bayes algorithm is the best fitted algorithm.**
- **For Dog dataset, Multinomial Naive Bayes algorithm is the best fitted algorithm.**

Multinomial Naive Bayes algorithm trained on the Human dataset, predicts Chimpanzee and Dog DNA dataset more accurately than other trained models, by the accuracy of 99%. Because the Chimpanzee and humans share the same genetic hierarchy. The performance of the dog is not quite as good which is because the dog is more diverging from humans than the chimpanzee.

:heavy_check_mark: Hence the best fitted model for all the three datasets is,
**Multinomial Naive Bayes Algorithm trained on Human Dataset**



Hooray!! The models are deployed successfully!

********************************************************************

## :diamond_shape_with_a_dot_inside: Author
**Code Contributed by, *Abhishek Sharma*, 2021 @abhisheks008 #LGMSOC21**
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
