from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
from dotenv import load_dotenv

load_dotenv()

client_id_mine = os.getenv("spotify_clientID")
client_secret_mine = os.getenv("spotify_client_secret")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = client_id_mine,
    client_secret= client_secret_mine
))

track_url = "https://open.spotify.com/track/28rtWBDUGP8JLEuJ57cwdv"

track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

track = sp.track(track_id) 
print(track)

track_data = {
    "Track_Name" : track['name'],
    "Artist" : track['artists'][0]['name'],
    "Album" : track["album"]["name"],
    "Popularity" : track["popularity"],
    "Duration (minutes)" : track["duration_ms"]/60000
}

print(f"\nTrack Name: {track_data['Track_Name']}")
print(f"\nArtist: {track_data['Artist']}")
print(f"\nAlbum: {track_data['Album']}")
print(f"\nPopularity: {track_data['Popularity']}")
print(f"\nDuration: {track_data['Duration (minutes)']:.2f} minutes")

df = pd.DataFrame([track_data])
print("\n Track data as Dataframe")
print(df)

df.to_csv('spotify_track_data.csv', index=False)

features = ['Popularity','Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8,5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track_Name']}'")
plt.ylabel('Value')
plt.savefig("output.png")  # Save the plot as an image
plt.show(block=True)

