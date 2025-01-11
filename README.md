# VoiceHAT
Using the AIY VoiceHAT from a standard RaspberryPi OS (raspbian) install


![](voiceHAT.png)

Button on GPIO 23

LED on GPIO 25

Installation & Requirements
===========================
Install the overlay & reboot
    echo "dtoverlay=googlevoicehat-soundcard" | sudo tee -a /boot/firmware/config.txt

Install demo requirements
    pip3 install vosk sounddevice
    sudo apt-get install libportaudio2 espeak



buttonled.py - read the button and light the LED

motors.py - run motors attached to the drivers

servos.py - move servos 

sound.py - test sound in python

testsound.sh - record and immediately playback 3 seconds of sound

voiceassistant.py - simple offline voice assistant, using vosk and espeak
