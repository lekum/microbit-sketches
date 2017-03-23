import radio
from microbit import display, Image, pin0, pin1, pin2, compass, accelerometer


def direction():
    compass.calibrate()
    display.show(Image.ARROW_N)

    while True:
        gesture = accelerometer.current_gesture()
        if gesture == "shake":
            break # Back to the menu mode
        needle = ((15 - compass.heading()) // 30) % 12
        radio.send("direction_")

def menu_mode():

    display.show(Image.HAPPY)

    while True:
        if pin0.is_touched():
            direction()
        if pin1.is_touched():
            acceleration()
        if pin2.is_touched():
            telesketch()

if __name__ == "__main__":
    menu_mode()
