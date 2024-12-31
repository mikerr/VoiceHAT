#!/usr/bin/env python

# very simple local voice assistant 
# just tells the time when asked "whats the time, tel me the time etc"

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
    return answer

device_info = sd.query_devices(None, "input")
samplerate = int(device_info["default_samplerate"])
        
model = Model(lang="en-us")

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
            stream.stop()
            process = subprocess.Popen(['espeak','-a 50','--stdin'], stdin=subprocess.PIPE )
            process.stdin.write(answer.encode('utf-8'))
            process.stdin.flush()
            process.stdin.close()

            process.wait()
            stream.start()
