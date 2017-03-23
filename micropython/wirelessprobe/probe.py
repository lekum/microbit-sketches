import radio
from microbit import button_a, button_b, display, Image

radio.on()

display.show(Image.HAPPY)

while True:

    if button_a.was_pressed():
        radio.send("A-pressed")
    if button_b.was_pressed():
        radio.send("B-pressed")
