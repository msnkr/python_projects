from tkinter import *
import subprocess
from tpblite import TPB, CATEGORIES


BACKGROUND_COLOR = "#363535"
TEXT_COLOR = "#D6D4D5"


t = TPB('https://tpb.party')
results_dict = {}
magnet = ""


def stream(torrent):
    subprocess.call(
        [r"c:\Users\Digital\AppData\Roaming\npm\webtorrent.cmd", torrent.magnetlink, "--vlc"])


def show_options(results):
    canvas = Canvas(window, width=560, height=200, bg="white")
    canvas.pack()

    for result in results:
        result_btn = Button(
            canvas, text=results[result].title, command=lambda: stream(results[result]), padx=5, pady=5)
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
window.config(width=600, height=400, padx=20,
              pady=20, background=BACKGROUND_COLOR)

search_label = Label(window, text="Search", fg=TEXT_COLOR,
                     background=BACKGROUND_COLOR, padx=5, pady=5)
search_label.pack()

search_entry = Entry(window, fg=TEXT_COLOR,
                     background=BACKGROUND_COLOR)
search_entry.pack()

search_btn = Button(window, text="Search", command=results,
                    fg=TEXT_COLOR, background=BACKGROUND_COLOR, padx=5, pady=5)
search_btn.pack()

quit_btn = Button(window, text="Quit", command=window.destroy,
                  fg=TEXT_COLOR, background=BACKGROUND_COLOR, padx=5, pady=5)
quit_btn.pack()


window.mainloop()
