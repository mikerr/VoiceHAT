#!/usr/bin/env python
# light up the big button LED when pressed

import time
from gpiozero import LED, Button

led = LED(25)
button = Button(23)

button.when_pressed = led.on
button.when_released = led.off

while True:
    # time.sleep(1)


    print ("Waiting for button")
    button.wait_for_press()
    print ("button pressed")
