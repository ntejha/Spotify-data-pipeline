import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

client_id_mine = os.getenv("spotify_clientID")
client_secret_mine = os.getenv("spotify_client_secret")
password = os.getenv("sql_password")

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id_mine,  # Replace with your Client ID
    client_secret=client_secret_mine  # Replace with your Client Secret
))

# MySQL Database Connection
db_config = {
    'host': 'localhost',           # Change to your MySQL host
    'user': 'root',       # Replace with your MySQL username
    'password': password,   # Replace with your MySQL password
    'database': 'spotify_db'       # Replace with your database name
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Full track URL (example: Shape of You by Ed Sheeran)
track_url = "https://open.spotify.com/track/28rtWBDUGP8JLEuJ57cwdv"

# Extract track ID directly from URL
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details
track = sp.track(track_id)

# Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}

# Insert data into MySQL
insert_query = """
INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s)
"""
cursor.execute(insert_query, (
    track_data['Track Name'],
    track_data['Artist'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration (minutes)']
))
connection.commit()

print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

# Close the connection
cursor.close()
connection.close()