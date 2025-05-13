import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()


# fetch top 100 songs from a day in the past, based on a user input and store them in a list
URL = "https://www.billboard.com/charts/hot-100"
user_choice = input("Which year do you want to travel to? Use the following format YYYY-MM-DD: ")
endpoint = f"{URL}/{user_choice}"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"}

response = requests.get(url=endpoint, headers=header)
response.raise_for_status()
music_url = response.text

soup = BeautifulSoup(music_url, "lxml")
song_titles = soup.select(selector="li ul li h3")
top_songs = [title.getText().strip() for title in song_titles]

# authenticate my spotify app
authmanager = SpotifyOAuth(client_id=os.environ["SPOTIFY_ID"], client_secret=os.environ["SPOTIFY_SECRET"], redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"], scope="playlist-modify-private", show_dialog=True,  cache_path="./token.txt", username="izmyname")

sp = spotipy.Spotify(auth_manager=authmanager)

sp.current_user()

user_id = sp.current_user()["id"]

# get songs' URI
songs_uris = []
year = user_choice[:4:]
for song in top_songs:
    try:
        songs_uris.append(sp.search(q=f"track:{song} year:{year}", type="track", limit=1)['tracks']['items'][0]["uri"])
    except IndexError:
        continue

# create playlist and songs to it
my_playlist = sp.user_playlist_create(user=user_id, name=f"{user_choice} Billboard 100", public=False, collaborative=False, description=f'100 best songs from {year}')
playlist_id = my_playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=songs_uris)
