import time
import board
import neopixel

R = (50, 0, 0)
G = (0, 50, 0)
B = (0, 0, 50)

COLORS = (R, G, B)

pixels = neopixel.NeoPixel(board.GP22, 1)

while True:
    for color in COLORS:
        pixels[0] = color
        time.sleep(1)
