import radio
from microbit import display

radio.on()

while True:

    incoming = radio.receive()
    if incoming == "A-pressed":
        display.show("A")
    if incoming == "B-pressed":
        display.show("B")
