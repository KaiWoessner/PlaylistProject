import pandas as pd
import random as rand

import spotipy
from spotipy.oauth2 import SpotifyOAuth

fin_tracks = pd.read_csv("fin_tracks.csv")

SPOTIPY_CLIENT_ID = '9e6da8e7a7434b409e7c30ad4091e88d'
SPOTIPY_CLIENT_SECRET = 'ef0ba456de6f49ecbb364a0fa8e0f18e'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Create a Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-read-playback-state,user-modify-playback-state,playlist-modify-private'))

def create_playlist_and_add_tracks(playlist_name, track_ids):
    # Create a new private playlist
    playlist = sp.user_playlist_create(sp.me()['id'], playlist_name, public=False)

    # Add the tracks to the playlistPop
    sp.playlist_add_items(playlist['id'], track_ids)

def play_track(track_id):
    devices = sp.devices()
    if not devices['devices']:
        print("No active devices found.")
        return
    
    print("Now playing:", idv_song["name"], "-", idv_song["main_artist"])

    sp.start_playback(uris=['spotify:track:' + track_id])

# Get user input for the desired genre
years = input("Year Range (XXXX - XXXX):")

filt_merge_feat = fin_tracks

if "-" in years:
    year = years.split("-")
    
    start_year = year[0]
    end_year = year[1]

    filt_merge_feat = filt_merge_feat[filt_merge_feat["year"] >= int(start_year)]
    filt_merge_feat = filt_merge_feat[filt_merge_feat["year"] <= int(end_year)]

genre_keywords = ['POP', 'FOLK', 'ROCK', 'EMO', 'SOUL', 'INDIE', 'HIP HOP', 'TRAP', 'JAZZ', 'METAL', 'ALTERNATIVE', 'R&B', 'DANCE', 'TECHNO', 'BLUES', 'CLASSICAL', 'COUNTRY', 'FUNK']
print("Genre choices:", " ".join(genre_keywords))

playlist_name = "My Random Playlist"
playlist_tracks = []

count = 0
while True:
    
    song_genre = input("Choose Genre (q to exit, r for repeat): ").lower()

    if song_genre == "r" and count == 0:
        print("No song to choose. Exiting.")
        break
    if song_genre == "q":
        # If the user decides not to generate another song, create the playlist and exit the loop
        if playlist_tracks:
            create_playlist_and_add_tracks(playlist_name, playlist_tracks)
            print(f"Playlist '{playlist_name}' created with {len(playlist_tracks)} songs.")
            sp.pause_playback()
        print("Exiting.")
        break
    
    if song_genre != "r":
        filt_merge_feat['is_equal'] = filt_merge_feat['genre_categories'].apply(lambda x: song_genre in x)
        songs = filt_merge_feat[filt_merge_feat["is_equal"]].reset_index(drop=True)

    rand_idx = rand.randint(0, len(songs) - 1)
    idv_song = songs.iloc[rand_idx]

    # Play the selected track on the user's Spotify application
    play_track(idv_song["id"])

    # Ask the user if they want to add the song to the playlist
    add_to_playlist = input("Do you want to add this song to the playlist? (y/n): ").lower()

    if add_to_playlist == "y":
        playlist_tracks.append(idv_song["id"])
        print("'" + idv_song["name"] + "'", "added to the playlist.")
        
    count+=1