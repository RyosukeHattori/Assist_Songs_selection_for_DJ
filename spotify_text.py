import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

client_id = '55e915e6dc2549b29feb68ef4e611e2a'
client_secret = '086669968e7e4892bc08c8d39308afaf'
username="21ulbu67tca2mhvh2jiy3g4da"

def recognized_sportipy(client_id = '55e915e6dc2549b29feb68ef4e611e2a', client_secret = '086669968e7e4892bc08c8d39308afaf', 
username="21ulbu67tca2mhvh2jiy3g4da"):


    token = util.prompt_for_user_token(
    username="21ulbu67tca2mhvh2jiy3g4da",
    scope='user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public', 
    client_id = '55e915e6dc2549b29feb68ef4e611e2a',
    client_secret = '086669968e7e4892bc08c8d39308afaf',
    redirect_uri="http://localhost:8889/callback"
)
sp = spotipy.Spotify(auth=token)