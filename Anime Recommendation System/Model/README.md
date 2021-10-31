# Anime Recommendation System

## Description
In this project we will be working on an Anime Dataset . Our prime aim will be to create a function or model to recommend anime based on the respective anime we have inputted.For this we have created a function , which works in a manner , that it looks at correlation between various anime series , based on factors like rating,genre etc.
Since originally dataset was quite heavy to process , so we have done a deep cleaning of dataset , in which anime who's rating arent mentioned , or those who have been given -1 rating and eventually those who are minimum rated by 2000 people are considered , so as to reduce processing time.

## Dataset

Dataset for the same can be downloaded from [here](https://www.kaggle.com/CooperUnion/anime-recommendations-database)<br>
Total anime in dataset : 9924 <br>
Total rows : 6337234<br>
Anime considered for making Recommendation system : 861<br>
Minimum no of Ratings considered while creating function : 2000 <br>
Rows considered for making model : 4335993 <br>

**WHAT I HAVE DONE**
- Used Kaggle API , to easy to run and remote running of dataset
- Performed a thorough cleaning of the dataset provided , so as to gain best substantial results and reduce processing time.
- Used Graphic visualization to deeply understand the data and analyze the same
- Created a function , which returns value based on the input anime name and thus calculating correlation with other anime present in our dataset.

**WORKING**

- So , the function which we have created , takes 2 parameters i.e df_recom and the anime which we want to find recommendation based on.
- In the next step the df_recom function creates a pivot table which basically plots a pivot table of all the anime in the dataset.
- Moving ahead the function then uses the pivot table to find correlation betweem different values of anime. 
- Once the correlation is taken out , we sort all the values in ascending order to make the highest correlation values anime get on top.
- After we have sorted we can use the head() function to view the highest correlation anime and this is how we get our recommendation.

**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib

**OUTPUT IMAGES**

<img src = "https://github.com/photon149/ML-ProjectKart/blob/fe8ee7460ed4ac8935f94ff416b36b95121353ac/Anime%20Recommendation%20System/Images/g1.png">
<img src = "https://github.com/photon149/ML-ProjectKart/blob/fe8ee7460ed4ac8935f94ff416b36b95121353ac/Anime%20Recommendation%20System/Images/g2.png">
<img src = "https://github.com/photon149/ML-ProjectKart/blob/fe8ee7460ed4ac8935f94ff416b36b95121353ac/Anime%20Recommendation%20System/Images/g3.png">
<img src = "https://github.com/photon149/ML-ProjectKart/blob/fe8ee7460ed4ac8935f94ff416b36b95121353ac/Anime%20Recommendation%20System/Images/g4.png">

**CONCLUSION**
<br>
All in all , we implemented a recommendation system to suggest best anime , based on user input .Once , the user inputs an anime of his choice , he/she gets a list of suggested animes with their correlation coeffiecient to give the best suggestion result.In the code , we also implemented by giving of two manually given anime inputs plus their results produced.



