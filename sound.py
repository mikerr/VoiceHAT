#!/usr/bin/env python
import time, pygame

pygame.init()

# load and  playback sound from disk
pygame.mixer.music.load('test.wav')
pygame.mixer.music.play() 
time.sleep(5)
pygame.mixer.music.stop()

