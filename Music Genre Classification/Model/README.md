<h1> Music Genre Classification </h1>
<h2> Abstract </h2>
<p> Music is a popular art form that is listened by billions of people everyday.Irrespective of what culture we're from everyone loves music.
  Music Genre Classification is one many branches of Music Information Retrieval.From here we can performs other musical tasks on data like music generation,
  track separation,recommender systems etc.We have many music genres and out of which we are going to predict 10 music genres in this project,which are
  <ol>
    <li> Blues </li>
    <li> Classical </li>
    <li> Country </li>
    <li> Disco </li>
    <li> Hiphop </li>
     <li>Jazz </li>
      <li>Metal </li>
      <li>Pop </li>
      <li> Reggae </li>
     <li>  Rock </li> </ol> </p>
  <h2> Dataset </h2>
  <p> The data set which is used here is the popular GTZAN dataset collected from kaggle.Here is the link to the dataset 
  https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification.</p>
  <h2> Goal </h2>
  <p> The goal of this project is to create a model which will classify all the 10 genres based on the song selected.The song can be selected from the dataset
  or any other source.The song format must be in .wav format and for 30 sec in duration. </p>
  <h2> What Have I Done? </h2>
  <ol>
  <li> Importing all the libraries required for the project. Check requirements.txt .</li>
   <li> Upload the dataset </li>
   <li> Data Cleaning </li>
    <li> Exploratory Data Analysis performed on a features_3_sec.csv file which is present in the dataset </li>
    <li> Audio Data Visualization </li>
    <ul>
      <li> Applying Fast Fourier Transform which allows us to decompose an audio signal into its individual frequency </li>
      <li> plotting the Mel Spectogram which is the visual representation of an audio signal </li>
    </ul>
  <li> Principle Component Analysis which is used to visualize the group of genres </li>
  <li> Classifier model creation </li>
  <ul>
    <li>Spliting the dataset </li>
    <li>Feature Scaling </li>
    <li>Feature Importance using Permutation Feature Importance </li>
    <li>Deploying Models</li>
    <ul>
      <li> Random Forest Classifier </li>
      <li> KNN Classifier </li>
      <li> XG Boost Classifier </li>
      <li> Cat Boost Classifier </li>
      <li> Convoutional Neural Network </li>
      <li> Logistic Regression </li>
    </ul>
  </ul>
    <li>Model Tuning  </li>
  <li>Comparing the best models after Hypertuning using RandomisedSearchCV and GridSearchCV </li>
    <li>Performance Metrics </li>
    <li> Model Evaluation </li>
    <li> Conclusion </li>
    </ol>
    <h2> Libraries Used </h2>
    <ol>
  <li> Pandas </li>
  <li> numpy </li>
  <li> Librosa </li>
  <li> sklearn </li>
  <li> Matplotlib </li>
  <li> Seaborn </li>
  </ol>
    <h2> Model Comparison </h2>
    <table>
<thead>
<tr>
<th align="center">Name of the Model</th>
<th align="center">Accuracy</th>
<th align="center">Precision Score</th>
<th align="center">Recall Score</th>
<th align="center">f1-Score</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Logistic Regression</td>
<td align="center">0.68</td>
<td align="center">0.68</td>
<td align="center">0.69</td>
<td align="center">0.68</td>
</tr>
<tr>
<td align="center">Random Forest Classifier</td>
<td align="center">0.87</td>
<td align="center">0.87</td>
<td align="center">0.87</td>
<td align="center">0.87</td>
</tr>
<tr>
<td align="center">XG Boost Classifier</td>
<td align="center">0.88</td>
<td align="center">0.88</td>
<td align="center">0.88</td>
<td align="center">0.88</td>
</tr>
<tr>
<td align="center">Cat Boost Classifier</td>
<td align="center">0.89</td>
<td align="center">0.89</td>
<td align="center">0.89</td>
<td align="center">0.89</td>
</tr>
<tr>
<td align="center">KNN Classsifier</td>
<td align="center">0.89</td>
<td align="center">0.89</td>
<td align="center">0.89</td>
<td align="center">0.89</td>
</tr>
<tr>
<td align="center">Convolutional Neural Network</td>
<td align="center">0.75</td>
<td align="center">0.75</td>
<td align="center">0.74</td>
<td align="center">0.75</td>
</tr>
</tbody>
</table>
<h2> FrontEnd/UI </h2>
<a href="#"><img src="https://github.com/Raghavi20/ML-ProjectKart/blob/main/Music%20Genre%20Classification/Images/PIC1.jpeg" class="pic1"></a>

<a href="#"><img src="https://github.com/Raghavi20/ML-ProjectKart/blob/main/Music%20Genre%20Classification/Images/PIC2.JPG" class="pic2"></a>

<a href="#"><img src="https://github.com/Raghavi20/ML-ProjectKart/blob/main/Music%20Genre%20Classification/Images/PIC3.JPG" class="pic3"></a>

<h2> Conclusion </h2>
<b> Comparing the metrics the models have achieved by the Machine Learning Algorithms,majority of them have achieved good accuracy.
  But Catboost and KNN have achieved the highest accuracy </b>
  <br>
<b> Best Fitted Models Ranking : </b>
<ol>
  <li>Catboost classifier </li>
  <li>KNN Classifier</li>
  <li>XG Boost Classifier</li>
  <li>Random Forest Classifier</li>
  <li>Convolutional Network</li>
  <li>Logistic Regression</li>
  </ol>
<h2> Author </h2>
<p>Code Contributed by, D.Lakshmi Raghavi, 2021 @Raghavi20 #LGMSOC21 </p>
  
      
    
  
  
