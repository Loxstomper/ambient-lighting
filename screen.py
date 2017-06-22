#!/bin/python3

from PIL import ImageEnhance
# windows
#from PIL import ImageGrab
# linux
from mss.linux import MSS as mss

# windows
#img = ImageGrab.grab()

# linux
sct = mss()

for filename in sct.save():
    print(filename)

# calc avg

#pixels = list(img.getdata())
#print(pixels)
