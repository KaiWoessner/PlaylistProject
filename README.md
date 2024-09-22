In this project, I used a music dataset containing over 1.2 million songs, the `Spotify API`, `Tkinter`, and a `Sklearn` machine learning model to create a Spotify playlist based on the user’s song interests.

The dataset contains 1.2 million songs of Spotify IDs, title, artists, and a set of song traits measured numerically.
The song traits analyzed are:  
- Key
- Loudness
- Speechiness
- Acousticness
- Instrumentalness
- Tempo
- Dancibility
  
The `Spotify API` is used to connect the computer to the user's Spotify account. Here is a link to the documenation: [Spotify API Documentation](https://developer.spotify.com/documentation/web-api).
The built-in cosine similarity `Sklearn` machine learning algorithm is then used to identify similar songs that the user likes or dislikes. 
Cosine similarity measures the similarity of two vectors by calculating the angle between them. 
If the second vector is identical to the first, the second vector is given a similarity score of 1 and if they are opposite, the second vector is given a similarity score of -1.
 <br/>
<p align="center">
  <img src="/images/PlaylistName.png" width="500"/><br/>
  When the program runs, a `Tkinter` UI appears and prompts the user to enter a title for the playlist. 
</p>
<br/>
<p align="center">
  <img src="/images/SongsLeft1.png" width="500"/><br/>
  A song then begins to play and the user is prompted to answer whether they like the current song. After each decision, the amount of possible playlist songs decreases.  
</p>
<br/>
<p align="center">
  <img src="/images/PlaylistCreated.png" width="400"/>
  <img src="/images/FinalPlaylist.png" width="400"/><br/>
  This process continues until there are about 700 songs left, then a playlist of the top 20 most similar songs to the user's likes is created in Spotify.
</p>
