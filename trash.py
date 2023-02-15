import speech_recognition as sr


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    if 'Микрофон MacBook' in name:
        macos_mic = index

def listen_macos():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=macos_mic)
    with mic as source:
        audio = r.listen(source)
        print(r.recognize_google(audio, language='ru-RU'))

listen_macos()

