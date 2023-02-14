import speech_recognition as sr
from mic_index import*
from name_audio import *
import pyaudio, wave

def start():
    play_sound(hello_jar).play()

class play_sound:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
    


def listen_windows():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        print(r.recognize_google(audio, language="ru-RU"))
    


def main():
    start()
    listen_windows()



if __name__ == "__main__":
    
    main()

