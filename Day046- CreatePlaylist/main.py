import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date=input("Enter Date(YYYY-MM-DD) to view list of song of that week: ")

response=requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
soup=BeautifulSoup(response.text,"html.parser")

song_list=soup.select(selector="li h3")

songs=[song.getText().strip() for song in song_list][:101]

CLIENT_ID=""
CLIENT_SECRET=""

# Spotify Authentication
sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id=sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year=date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist=sp.user_playlist_create(user=user_id,name=f"{date} Billboard Hot 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# paste the url in terminal when web page (example.com) open
