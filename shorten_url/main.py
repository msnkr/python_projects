import pyshorteners

s = pyshorteners.Shortener()


def shorten(url):
    return s.tinyurl.short(url)


url = input("Enter the url: ")
if url != "q":

    result = shorten(url)
    print(result)
else:
    print("Goodbye")
