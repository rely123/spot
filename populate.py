import json, sqlite3

conn = sqlite3.connect("db_topsongs.sqlite3")

with open("songs.json",'r', encoding="utf8") as j:
	data = json.load(j)

	for x in data["feed"]["results"]:
		gender = x['genres']
		str_gender = json.dumps({"genres": gender})

		conn.execute("INSERT INTO songs_song (songId, name, releaseDate, kind, url, artistName, artistId, artistUrl, artworkUrl100, genres) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (x['id'], x['name'], x['releaseDate'], x['kind'], x['url'], x['artistName'], x['artistId'], x['artistUrl'], x['artworkUrl100'], str_gender))
		conn.commit()	

print("Datos cargados con exito.")
conn.close() 