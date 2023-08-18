# buttons.py
# wait for button press on VoiceHAT

from gpiozero import Button

button = Button(23)

print ("Waiting for button")
button.wait_for_press()
print ("button pressed")
