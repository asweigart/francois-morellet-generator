"""Francois Morellet Generator
By Al Sweigart al@inventwithpython.com

Generates art in the style of the 1960 piece by Francois Morellet,
"Random Distribution of 40,000 Squares Using the Odd and Even Numbers of a Telephone Directory"."""

__version__ = '0.1.0'

import random
from PIL import Image, ImageColor

def generate_morellet(scale=1, width=200, height=200, colors=None):
    if colors is None:
        colors = ['red', 'blue']

    for i, v in enumerate(colors):
        colors[i] = ImageColor.getcolor(v, 'RGB')

    im = Image.new('RGB', (width, height), colors[0])
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y), random.choice(colors))

    if scale != 1:
        im = im.resize((width * scale, height * scale), Image.NEAREST)

    return im

#generate_morellet().show()
#for i in range(9):
#    generate_morellet(5).save('morellet' + str(i+1) + '.png')