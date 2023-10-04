from tkinter import *
from tpblite import TPB, CATEGORIES


t = TPB('https://tpb.party')
torrents = t.search(
    "Resident evil", category=CATEGORIES.VIDEO.MOVIES)


for index, torrent in enumerate(torrents):
    print(index, torrent)
