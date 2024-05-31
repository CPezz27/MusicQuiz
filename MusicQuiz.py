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

    x = int(input("Choose which artist has more albums between '{}' (1) and '{}' (2): ".format(artists_random[0],
                                                                                          artists_random[1])))
    if x == 1 or x == 2:
        print("You have selected '{}'".format(x))
        if (x == 1 and nb_album1 >= nb_album2) or (x == 2 and nb_album1 <= nb_album2):
            print("You did it!")
        elif (x == 1 and nb_album1 < nb_album2) or (x == 2 and nb_album1 > nb_album2):
            print("Not correct.")
        print("{} has {} albums, while {} has {} albums".format(artists_random[0], nb_album1, artists_random[1],
                                                             nb_album2))
    elif x not in ["1", "2"]:
        raise Exception("Response not accepted.")

    y = input("Do you want to continue?(Y) ").strip().lower()
    if y != "y":
        a = False

print("Thank you for playing!")
