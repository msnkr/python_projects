from tkinter import *
import subprocess
from tpblite import TPB, CATEGORIES


t = TPB('https://tpb.party')
results_dict = {}
magnet = ""


def stream(title):
    if title in results_dict:
        print(True)


def show_options(results):
    canvas = Canvas(window, width=560, height=200, bg="white")
    canvas.pack()

    for result in results:
        result_btn = Button(
            canvas, text=results[result].title, command=lambda: stream(result_btn.cget("text")))
        result_btn.config(highlightbackground="white",
                          highlightthickness=None, highlightcolor="white", background="white")
        result_btn.pack()


def results():
    search = search_entry.get()
    torrents = t.search(
        f"{search}", category=CATEGORIES.VIDEO.MOVIES)

    for index, torrent in enumerate(torrents):
        results_dict[index] = torrent

    show_options(results_dict)


window = Tk()
window.title("Uggh")
window.config(width=600, height=400, padx=20, pady=20)

search_label = Label(window, text="Search")
search_label.pack()

search_entry = Entry(window)
search_entry.pack()

search_btn = Button(window, text="Search", command=results)
search_btn.pack()

quit_btn = Button(window, text="Quit", command=window.destroy)
quit_btn.pack()


window.mainloop()
