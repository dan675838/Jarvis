# import speech_recognition as sr


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     if 'Микрофон MacBook' in name:
#         macos_mic = index

# def listen_macos():
#     r = sr.Recognizer()
#     mic = sr.Microphone(device_index=macos_mic)
#     with mic as source:
#         audio = r.listen(source)
#         print(r.recognize_google(audio, language='ru-RU'))

# listen_macos()
from main import *


model = Model(r"vosk_ru")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
    


def fff():
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            text = text[14:-3]
            print(text)
            return text

def ff():
    while True:
        command = fff()
        if 'джарвис' in command:
            play_sound(yes_sir).play

def main():
        ff()

main()