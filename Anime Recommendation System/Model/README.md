# Anime Recommendation System

In this project we will be working on an Anime Dataset . Our prime aim will be to create a function or model to recommend anime based on the respective anime we have inputted.For this we have created a function , which works in a manner , that it looks at correlation between various anime series , based on factors like rating,genre etc.
Since originally dataset was quite heavy to process , so we have done a deep cleaning of dataset , in which anime who's rating arent mentioned , or those who have been given -1 rating and eventually those who are minimum rated by 2000 people are considered , so as to reduce processing time.

## Dataset

Dataset can be downloaded from [here](https://www.kaggle.com/CooperUnion/anime-recommendations-database)

**WHAT I HAVE DONE**
-Used Kaggle API , to easy to run and remote running of dataset
-Performed a thorough cleaning of the dataset provided , so as to gain best substantial results and reduce processing time.
-Used Graphic visualization to deeply understand the data and analyze the same
-Created a function , which returns value based on the input anime name and thus calculating correlation with other anime present in our dataset.


**LIBRARIES NEEDED**
- numpy
- pandas
- seaborn
- matplotlib

**CONCLUSION**
All in all , we implemented a recommendation system to suggest best anime , based on user input .Once , the user inputs an anime of his choice , he/she gets a list of suggested animes with their correlation coeffiecient to give the best suggestion result.In the code , we also implemented by giving of two manually given anime inputs plus their results produced.




