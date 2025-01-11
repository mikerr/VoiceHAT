#!/usr/bin/env python

# very simple local voice assistant 
# Can ask :
# "whats the time", "tell me the time"
# "whats the date"

# requirements: 
# pip3 install vosk sounddevice
# sudo apt-get install libportaudio2 espeak 

import sounddevice, queue
import json, subprocess, datetime
import vosk

q = queue.Queue()
def callback(indata, frames, time, status):
    q.put(bytes(indata))

def read_question (sentence):
    answer = ""
    today = datetime.datetime.now()
    if ("time" in sentence):
        now = today.strftime("%H %M")
        answer = "the time is " + now
    if ("date" in sentence):
        now = today.strftime("%B %d")
        answer = "the date is " + now
    return answer

def speak(sentence):
        p = subprocess.Popen(['espeak','-a 50','--stdin'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
        p.stdin.write(sentence.encode('utf-8'))
        p.stdin.flush()
        p.stdin.close()
        p.wait()

device_info = sounddevice.query_devices(None, "input")
samplerate = int(device_info["default_samplerate"])

speak("hello")
stream = sounddevice.RawInputStream(samplerate=samplerate, blocksize = 8000, dtype="int16", channels=1, callback=callback)
stream.start()

vosk.SetLogLevel(-1)
model = vosk.Model(lang="en-us")
rec = vosk.KaldiRecognizer(model, samplerate)
        
print("Press ctrl-c to stop the recording")
while True:
  try:
    data = q.get()
    if rec.AcceptWaveform(data):
        jres = json.loads(rec.Result())
        question = jres["text"]
        if (question != ""):
            print(question)
        answer = read_question(question)
        if (answer != "") :
            # stop listening while we are speaking
            stream.stop()
            speak(answer)
            # start listening again
            stream.start()
  except:
    exit(0)

