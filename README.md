# 🎧 Spotify Music Organiser

This script automatically organizes your **Liked Songs** on Spotify by genre and creates one playlist per group using the Spotify Web API and the `spotipy` library.

---

## 🚀 What It Does

- Fetches all songs from your Liked Songs library.
- Retrieves genres for each artist via the Spotify API.
- Groups songs into **genre categories** like Pop, Rock, Chill, etc.
- Creates a new playlist for each group and adds the songs automatically.

---

## 📂 Genre Structure

Genres are grouped as follows (you can customize these in the code):

| Group           | Recognized Subgenres                                          |
|----------------|---------------------------------------------------------------|
| Pop            | pop, synthpop, indie pop, dance pop, pop argentino            |
| Rock           | rock, classic rock, indie rock, alternative rock              |
| Latin          | reggaeton, trap latino, latin pop, urbano latino              |
| Chill          | lo-fi, chill, downtempo, ambient, sleep                       |
| Electronic     | edm, house, techno, electronic, electro                       |
| Hip Hop / Rap  | hip hop, rap, trap, boom bap                                  |
| R&B / Soul     | r&b, neo soul, soul                                           |
| Unknown        | Anything not recognized in the above                          |

---

## 🛠 Requirements

- Python 3.7+
- A Spotify Developer account
- Python dependencies:

```bash
pip install spotipy
````
---

## 🔐 Setup
Go to Spotify Developer Dashboard
Create a new app and copy your:

CLIENT_ID

CLIENT_SECRET

REDIRECT_URI (e.g. http://127.0.0.1:8888/callback)

Paste those values into the script:
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "your_redirect_uri"

---

## ▶️ How to Use
Make sure you have liked some songs in Spotify.
Run the script with:

python spotify_organiser.py
It will generate playlists named like:

My Songs - Pop
My Songs - Rock
My Songs - Chill
...
Each playlist will contain your Liked Songs matching that genre group.

---

## 📌 Notes
Artists without genre data will be grouped under Unknown.

The script respects Spotify's API limits:

50 songs per fetch

100 songs per playlist batch insert

You can run the script multiple times. It will create new playlists each time.

---

## 🧠 Customization
You can edit the genre groups in the GENRE_GROUPS dictionary at the top of the script.

GENRE_GROUPS = {
    "Your Group Name": ["keyword1", "keyword2", ...],
    ...
}
Feel free to rename or add your own genre clusters.

---

## 📝 License
This project is licensed under the MIT License.

If you found this helpful, consider giving it a ⭐ on GitHub!

