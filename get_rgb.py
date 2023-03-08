import colorgram
from colormap import rgb2hex


# input('What is the exact image name? Add .png or .jpeg etc\n')
image_name = "Untitled design.png"
color_list = []


def write_file(hex):
    with open("HexCodes.txt", "a")as file:
        file.write(f"{hex}\n")


def get_rgb(image_name):
    colors = colorgram.extract(image_name, 6)
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        hex = rgb2hex(r, g, b)
        write_file(hex)


get_rgb(image_name)
