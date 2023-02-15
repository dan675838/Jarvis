
# from vosk import Model, KaldiRecognizer
# import os
# import pyaudio

# model = Model(r"vosk_ru") # полный путь к модели
# rec = KaldiRecognizer(model, 16000)
# p = pyaudio.PyAudio()
# stream = p.open(
#     format=pyaudio.paInt16, 
#     channels=1, 
#     rate=8000, 
#     input=True, 
#     frames_per_buffer=8000
# )
# stream.start_stream()

# while True:
#     data = stream.read(4000)
#     if len(data) == 0:
#         break

#     print(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult())

# print(rec.FinalResult())

import speech_recognition as sr
from name_audio import *
from signal import signal, SIGPIPE, SIG_DFL  



def listen_macos():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('слушаю')
        audio = r.listen(source)
        print('Обработка...')     
        print(r.recognize_google(audio, language='ru-Ru'))

def test():
    r = sr.Recognizer()
    jackhammer = sr.AudioFile('/Users/daniilyushvaev/Desktop/Jarvis/audio/hello_jar.wav')
    with jackhammer as source:
        
        audio = r.record(source)

        print(r.recognize_google(audio, language='ru-RU')) 


def main():
    #signal(SIGPIPE,SIG_DFL)
    listen_macos()
    test()

if __name__ == "__main__":
    main()