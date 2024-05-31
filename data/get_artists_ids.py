import requests
import json

DEEZER_SEARCH_ARTIST_API = "https://api.deezer.com/search/artist"

# edit this list
to_be_searched_artits = ["Elio e le storie tese", "Queen", "Eminem", "Al Bano", "Mina", "Ghali", "Muse", "The Beatles",
                         "The Rolling Stones", "Micheal Jackson", "I Prevail", "Oasis", "Pink Floyd", "Billie Eilish",
                         "Drake", "Panetty", "Naska", "Daft Punk", "Dargen d'Amico", "Rancore", "Squallor", "Bazzi"
                         "Gigi d'Alessio", "Mozart", "Bethoveen", "Tony 2Milly", "Tredici Pietro", "Ariana Grande",
                         "Bruce Springsteen", "Cardi B", "David Bowie", "Dua Lipa", "Elton John", "Frank Sinatra",
                         "Jimi Hendrix", "Johnny Cash", "Kendrick Lamar", "Lady Gaga", "Led Zeppelin", "Whitney Houston",
                         "Luciano Pavarotti", "Madonna", "Nirvana", "Radiohead", "Rihanna", "The Weeknd", "U2", "Zucchero"]

results = {}

for artist in to_be_searched_artits:
    r = requests.get(DEEZER_SEARCH_ARTIST_API, params={"q":artist, "strict":"on"}).json()

    if len(r["data"])  == 0:
        print("No match found for '",artist,"'")
    elif len(r["data"]) > 1:
        print("Multiple matches found for '",artist,"'. I selected the most popular match. Checkout their pic:",r["data"][0]["picture_big"])
        results[artist] = r["data"][0]["id"]
    else:
        print("Exactly one match found for '", artist, "'")
        results[artist] = r["data"][0]["id"]

print("")
print("")
print("Final id map:")
# copy paste the result of the "print" into authors.json
print(json.dumps(results))
