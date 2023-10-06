from tkinter import *
import subprocess
from tpblite import TPB, CATEGORIES


BACKGROUND_COLOR = "#363535"
TEXT_COLOR = "#D6D4D5"


t = TPB('https://tpb.party')
results_dict = {}
magnet = ""
torrent_buttons = []


def stream(torrent):
    # subprocess.call(
    #     [r"c:\Users\Digital\AppData\Roaming\npm\webtorrent.cmd", torrent.magnetlink, "--vlc"])
    print("The file is loading")


def show_options(results):
    results_dict = {}
    torrent_buttons = []
    for result in results:
        result_btn = Button(
            canvas, text=results[result].title, command=lambda: stream(results[result]))
        result_btn.config(highlightbackground=BACKGROUND_COLOR,
                          highlightthickness=1, highlightcolor=BACKGROUND_COLOR, background="white", fg=BACKGROUND_COLOR)
        result_btn.grid(row=len(torrent_buttons), column=0,
                        columnspan=2, padx=5, pady=5)
        torrent_buttons.append(result_btn)


def results():
    search = search_entry.get()
    torrents = t.search(
        f"{search}", category=CATEGORIES.VIDEO.MOVIES)

    for index, torrent in enumerate(torrents):
        if index <= 10:
            results_dict[index] = torrent

    show_options(results_dict)


window = Tk()
window.title("Uggh")
window.config(width=800, height=400, padx=10,
              pady=10, background=BACKGROUND_COLOR)

search_label = Label(window, text="Search", fg=TEXT_COLOR,
                     background=BACKGROUND_COLOR, padx=5, pady=5)
search_label.grid(row=0, column=0, columnspan=2)

search_entry = Entry(window, fg=TEXT_COLOR,
                     background=BACKGROUND_COLOR)
search_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

search_btn = Button(window, text="Search", command=results,
                    fg=TEXT_COLOR, background=BACKGROUND_COLOR, padx=10, pady=5)
search_btn.grid(row=2, column=0, padx=5, pady=5)

quit_btn = Button(window, text="Quit", command=window.destroy,
                  fg=TEXT_COLOR, background=BACKGROUND_COLOR, padx=10, pady=5)
quit_btn.grid(row=2, column=1, padx=5, pady=5)

canvas = Canvas(window, bg="white", width=400, height=200)
canvas.grid(row=3, column=0, columnspan=2)

window.rowconfigure(3, weight=0)

window.mainloop()
