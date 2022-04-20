#testformybug
from bs4 import BeautifulSoup
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials


def load_cache():
    try:
        cache_file = open("song_dict.json", 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache

def save_cache(cache):
    cache_file = open("song_dict.json", 'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()


cid="f"
secret="f"
auth_manager=SpotifyClientCredentials(client_id=cid,client_secret=secret)
sp=spotipy.Spotify(auth_manager=auth_manager)

url = "Top Artists – Billboard"
f = open("Top Artists – Billboard.html", 'rb')
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')
name = soup.find_all("h3", id="title-of-a-story")
namelist = []
for i in name[0:100]:
    namelist.append(i.string.strip())

singer_list = []
for nm in namelist:
    singer_direct = {}
    singer_direct['name'] = nm
    results = sp.search(q='artist:' + nm, type='artist')
    nm_id = results['artists']['items'][0]['id']
    nm_url = f'spotify:artist:{nm_id}'
    song_dir_l = sp.artist_top_tracks(nm_url, country='US')
    song_dir_list = song_dir_l['tracks']
    temp_big_dir = {}
    top_song = []
    for i in range(10):
        song_name = song_dir_list[i]['name']
        song_small_id = song_dir_list[i]['id']
        song_feature = sp.audio_features(song_small_id)[0]
        
        temp_small_dir = {}
        temp_small_dir["danceability"] = song_feature["danceability"]
        temp_small_dir['energy'] = song_feature['energy']
        temp_small_dir['tempo'] = song_feature['tempo']
        temp_big_dir[song_name] = temp_small_dir
    top_song.append(temp_big_dir)

    
    singer_direct['songs'] = top_song
    singer_list.append(singer_direct)
save_cache(singer_list)



