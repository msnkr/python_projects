from tkinter import *
from tpblite import TPB, CATEGORIES


t = TPB('https://tpb.party')


def results():
    search = input("What do you want to search for?: ")
    torrents = t.search(
        f"{search}", category=CATEGORIES.VIDEO.MOVIES)
    results = {}
    magnet = ""

    for index, torrent in enumerate(torrents):
        results[index + 1] = torrent

    for key in results:
        print(key + 1,  results[key].title)

    selection = int(input("Which one? "))
    for key in results:
        if selection == key:
            magnet = results[key].magnetlink

    return magnet


results()
