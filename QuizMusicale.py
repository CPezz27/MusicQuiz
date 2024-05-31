# Generare un programma-quiz che, dati due autori estratti a caso dal file 'data/authors.json', li proponga all'utente
# domandandogli chi dei due ha pubblicato più album.
# L'utente dovrà rispondere con 1 o 2 e il sistema dirgli se ha vinto o meno e chiedergli se vuole continuare.
# Gli indovinelli continuano finché l'autore non scrive stop come risposta alla seconda domanda.
# Gestire tramite eccezioni l'inserimento di un valore non corretto (dunque né 1, né 2, né stop).
#
# Utilizzare le API di Deezer per capire qual è la risposta corretta e restituire un feedback all'utente.
# L'api richiede l'id dell'artista che è fornito nel file indicato precedentemente ('data/authors.json')

import random
import requests
import json


def get_album(artistid):
    url = "https://api.deezer.com/artist/{}".format(artistid)
    response = requests.get(url)
    nb_album = response.json()["nb_album"]
    return nb_album


a = True

with open('data/authors.json', 'r') as f:
    artists = json.load(f)

while a:

    artists_name = artists.keys()
    artists_random = random.sample(artists_name, 2)

    key1 = artists_random[0]
    key2 = artists_random[1]

    artist1id = artists[key1]
    artist2id = artists[key2]

    nb_album1 = get_album(artist1id)
    nb_album2 = get_album(artist2id)

    x = int(input("Scegliere quale artista ha più album tra '{}' (1) e '{}' (2): ".format(artists_random[0],
                                                                                          artists_random[1])))
    if x == 1 or x == 2:
        print("Hai selezionato '{}'".format(x))
        if (x == 1 and nb_album1 >= nb_album2) or (x == 2 and nb_album1 <= nb_album2):
            print("Complimenti, hai indovinato!")
            print("{} ha {} album, mentre {} ha {} album".format(artists_random[0], nb_album1 ,artists_random[1],
                                                                 nb_album2))
        elif (x == 1 and nb_album1 < nb_album2) or (x == 2 and nb_album1 > nb_album2):
            print("Mi dispiace, la risposta non è corretta.")
            print("{} ha {} album, mentre {} ha {} album".format(artists_random[0], nb_album1, artists_random[1],
                                                                 nb_album2))
    elif x not in ["1", "2"]:
        raise Exception("Risposta non accettata.")

    y = input("Vuoi continuare(Y/N) ").strip().lower()
    if y != "y":
        a = False

print("Grazie per aver giocato!")
