import radio
from microbit import display, Image, compass, button_a, button_b, sleep

def direction():
    """
    Send the direction which the probe is pointing to:
    direction_N, direction_NE, direction_E...
    """
    display.show(Image.ARROW_N)

    while True:
        sleep(100)
        if button_b.is_pressed():
            break # Back to the menu mode
        heading = compass.heading()
        if (heading > 343) or (heading <= 22):
            needle = "N"
        elif 22 < heading <= 67:
            needle = "NE"
        elif 68 < heading <= 113:
            needle = "E"
        elif 114 < heading <= 159:
            needle = "SE"
        elif 160 < heading <= 205:
            needle = "S"
        elif 206 < heading <= 251:
            needle = "SW"
        elif 252 < heading <= 297:
            needle = "W"
        elif 298 < heading <= 343:
            needle = "W"
        radio.send("dir_{}".format(needle))

def menu_mode():
    """
    Principal menu mode
    """
    while True:
        display.show(Image.HAPPY)
        radio.send("ready")

        if button_a.is_pressed():
            direction()

if __name__ == "__main__":
    radio.on()
    compass.calibrate()
    menu_mode()
