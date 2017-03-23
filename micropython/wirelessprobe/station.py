import radio
from microbit import display, Image

radio.on()

def decode_direction(dirstring):
    needle = int(distring.split("direction_")[1])
    display.show(Image.ALL_CLOCKS[needle])

while True:

    incoming = radio.receive()

    if incoming.startsWith("direction_"):
        decode_direction(incoming)
