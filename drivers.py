# drivers.py 
# use motors attached to the drivers pins on voiceHAT

from gpiozero import PWMOutputDevice
import time

# AIY VoiceHAT GPIOs
servos = (26,6,13,5,12,24)
drivers = (4,17,22,27)

motor = PWMOutputDevice(drivers[0])

while True:
        motor.on()
        time.sleep(1)

        motor.off()
        time.sleep(1)

        # speed value 0.0 - 1.0
        motor.value = 0.5
        time.sleep(1)

        motor.value = 0.0
        time.sleep(1)
