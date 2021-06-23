# Song Genre Classification
Spotify, with a net worth of $26 billion, is reigning the music streaming platform today. It currently has millions of songs in its database and claims to have the right music score for everyone. Spotify’s Discover Weekly service has become a hit with the millennials. Needless to say, Spotify has invested a lot in research to improve the way users find and listen to music. Machine Learning is at the core of their research. From NLP to Collaborative filtering to Deep Learning, Spotify uses them all. Songs are analyzed based on their digital signatures for some factors, including tempo, acoustics, energy, danceability, etc.

The task at hand is to categorize songs into certain categories (trap, rap, pop etc) based off of given values such as danceability, acousticness and other metrics that can be readily obtained via Spotify's organize playlist.  

Note that both sets of data use the same metrics available off of Spotify's organize playlist feature. These metrics are as follows:
1. **Genre** - the genre of the track
2. **Year** - the release year of the recording. Note that due to vagaries of releases, re-releases, re-issues and general madness, sometimes the release years are not what you'd expect.
3. **Added** - the earliest date you added the track to your collection.
4. **Beats Per Minute** (BPM) - The tempo of the song.
5. **Energy** - The energy of a song - the higher the value, the more energtic. song
6. **Danceability** - The higher the value, the easier it is to dance to this song.
7. **Loudness** (dB) - The higher the value, the louder the song.
8. **Liveness** - The higher the value, the more likely the song is a live recording.
9. **Valence** - The higher the value, the more positive mood for the song.
10. **Length** - The duration of the song.
11. **Acousticness** - The higher the value the more acoustic the song is.
12. **Speechiness** - The higher the value the more spoken word the song contains.
13. **Popularity** - The higher the value the more popular the song is.
14. **Duration** - The length of the song.

![](https://github.com/abhisheks008/ML-ProjectKart/blob/patch-13/Song%20Genre%20Classification/Images/spo1.png)

## Goal
The Goal of this project is to build the classification model using the Spotify dataset.

## Dataset
Here to build this model we are going to use, two datasets so that we have a large amount of data to train and test the classification models.
1. Spotify Mega Dataset :  https://www.kaggle.com/iamsumat/spotify-top-2000s-mega-dataset
2. Spotify 2010-2019 songs Dataset : https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year

I have also uploaded these two datasets in the [`Dataset`](https://github.com/abhisheks008/ML-ProjectKart/tree/patch-13/Song%20Genre%20Classification/Dataset) folder, you can access from there too.

