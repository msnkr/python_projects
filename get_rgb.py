import colorgram
from colormap import rgb2hex


def write_file(hex):
    with open(file_name + ".txt", "a")as file:
        file.write(f"{hex}\n")


def get_rgb(image_name):
    colors = colorgram.extract(image_name, 6)
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        hex = rgb2hex(r, g, b)
        write_file(hex)


try:
    image_name = input("Enter the file name: ")
    get_rgb(image_name)
except FileNotFoundError:
    print("File cannot be found. Enter the correct name and make sure image is in the same folder as program.")
