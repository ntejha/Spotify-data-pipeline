# Spotify Data Analytics

We get data from Spotify API's using python and then load it as a csv. then we visualize it using matplotlib.

The same data recieved from the Spotify API, we directly load it into MySQL. then we do ETL (Extract, Transform and Load) for analytics.

## Intializations 

In order to make this project work, we should do some pre-requistes : 

- Go to https://developer.spotify.com/dashboard
    - Create an app
    - Give it it's name
    - then in redirect url, enter : http://localhost:8889/callback
    - then click  on WebAPI, Web Playback SDK, Android, Ads API, IOS.
    - Then enter save.
    - click Settings
    - Copy and save the client id and cliend secret.

- Open terminal to this directory, create a virtual environment and do ```pip install -r requirements.txt```
