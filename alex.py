import speech_recognition as sr
import constants

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    while True:
        try:
            audio = r.listen(source)
        except Exception as e:
            print("icecream like big gay mike bloomberg")
        print("gay")
        try:
            text = r.recognize_google(audio)
        except Exception as e:
            print("mike bloomberg likes big gay icecream")