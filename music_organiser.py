#!usr/bin/python

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = ""

# Mapear subgéneros a categorías amplias
GENRE_GROUPS = {
    "Pop": ["pop", "synthpop", "indie pop", "dance pop", "pop argentino"],
    "Rock": ["rock", "classic rock", "indie rock", "alternative rock"],
    "Latino": ["reggaeton", "trap latino", "latin pop", "urbano latino"],
    "Chill": ["lo-fi", "chill", "downtempo", "ambient", "sleep"],
    "Electrónica": ["edm", "house", "techno", "electronic", "electro"],
    "Hip Hop / Rap": ["hip hop", "rap", "trap", "boom bap"],
    "R&B / Soul": ["r&b", "neo soul", "soul"],
    "Unknown": []
}

def get_group_from_genres(genres):
    genres = [g.lower() for g in genres]
    for group, keywords in GENRE_GROUPS.items():
        for g in genres:
            if any(k in g for k in keywords):
                return group
    return "Unknown"

def get_all_saved_tracks(sp):
    tracks = []
    limit = 50
    offset = 0
    while True:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        items = results['items']
        if not items:
            break
        tracks.extend([item['track'] for item in items])
        offset += limit
    return tracks

def batch_add_tracks(sp, playlist_id, tracks):
    for i in range(0, len(tracks), 100):
        sp.playlist_add_items(playlist_id, tracks[i:i+100])
        time.sleep(0.2)

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-library-read playlist-modify-public playlist-modify-private",
        cache_path=".cache"
    ))

    user_id = sp.current_user()['id']
    tracks = get_all_saved_tracks(sp)
    print(f"Total canciones guardadas: {len(tracks)}")

    grouped_tracks = {group: [] for group in GENRE_GROUPS.keys()}

    for idx, track in enumerate(tracks, start=1):
        artist_id = track['artists'][0]['id']
        artist_info = sp.artist(artist_id)
        genres = artist_info.get('genres', [])
        group = get_group_from_genres(genres)
        grouped_tracks[group].append(track['id'])

        if idx % 50 == 0:
            print(f"Procesadas {idx} canciones...")
        time.sleep(0.1)

    for group, track_ids in grouped_tracks.items():
        if not track_ids:
            continue
        print(f"Creando playlist para grupo '{group}' con {len(track_ids)} canciones")
        playlist = sp.user_playlist_create(user_id, f"Mis canciones - {group}")
        batch_add_tracks(sp, playlist['id'], track_ids)

if __name__ == "__main__":
    main()
