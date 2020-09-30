import speech_recognition as sr

r = sr.Recognizer()

keyWord = 'alex'

with sr.Microphone(device_index=4) as source:
    print('ALEX: Please start speaking..\n')
    while True: 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if keyWord.lower() in text.lower():
                print('ALEX: Keyword detected in the speech.\n')
                while True:
                    print('ALEX: Please speak command..')
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        if "nevermind" in text.lower():
                            print(text.lower())
                            print('ALEX: cum')
                            break
                        elif "weather" in text.lower():
                            print(text.lower())
                            print('ALEX: fuck you')
                            break
                        else:
                            print(text.lower())
                            print('ALEX: cock')
                    except Exception as e:
                        print('ALEX: Please repeat..')
            elif text.lower() == "quit":
                exit()
            else:
                print(text.lower())
        except Exception as e:
            # print('Please speak again.')
            pass
