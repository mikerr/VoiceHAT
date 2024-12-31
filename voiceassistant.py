#!/usr/bin/env python

# very simple local voice assistant 
# Can ask :
# "whats the time", "tell me the time"
# "whats the date"

# pip3 install vosk

import queue
import sounddevice as sd
import json
import subprocess

from datetime import datetime
from vosk import Model, KaldiRecognizer

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def read_question (sentence):
    answer = ""
    if ("time" in sentence):
        today = datetime.now()
        currenttime = today.strftime("%H %M")
        answer = "the time is " + currenttime
    if ("date" in sentence):
        today = datetime.now()
        now = today.strftime("%B %d")
        answer = "the date is " + now
    return answer

def speak(sentence):
        process = subprocess.Popen(['espeak','-a 50','--stdin'], stdin=subprocess.PIPE )
        process.stdin.write(sentence.encode('utf-8'))
        process.stdin.flush()
        process.stdin.close()

        process.wait()

device_info = sd.query_devices(None, "input")
samplerate = int(device_info["default_samplerate"])
        
model = Model(lang="en-us")

speak("hello")

stream = sd.RawInputStream(samplerate=samplerate, blocksize = 8000, 
            dtype="int16", channels=1, callback=callback)

print("#" * 80)
print("Press Ctrl+C to stop the recording")
print("#" * 80)


rec = KaldiRecognizer(model, samplerate)
        
stream.start()
while True:
    data = q.get()
    if rec.AcceptWaveform(data):
        jres = json.loads(rec.Result())
        question = jres["text"]
        print(question)
        answer = read_question(question)
        if (answer != "") :
            # stop listening while we are speaking
            stream.stop()
            speak(answer)
            # start listening again
            stream.start()
