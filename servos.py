from gpiozero import Servo,AngularServo
import time

#AIY VoiceHAT GPIOs
servos = (26,6,13,5,12,24)
drivers = (4,17,22,27)

servo = AngularServo(servos[0],min_angle=-90,max_angle=90)

while True:
        servo.angle = -90
        time.sleep(0.1)

        servo.detach()
        time.sleep(1)

        servo.angle = 90
        time.sleep(0.1)

        servo.detach()
        time.sleep(1)
