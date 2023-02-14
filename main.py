from vosk import Model, KaldiRecognizer
import speech_recognition as sr
from name_audio import *
import pyaudio, wave, socket
from sys import platform
import time

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    if 'Микрофон' in name:
        macos_mic = index

host_name = "one.one.one.one"  

def is_connected(hostname):
    try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
        host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except Exception:
        pass # we ignore any errors, returning False
    return False

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
    
def listen_macos():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=macos_mic)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        print(r.recognize_google(audio, language="ru-RU"))
    
def listen_macos_offline():
    model = Model(r"vosk_ru")
    r = KaldiRecognizer(model, 8000)
    mic = sr.Microphone(device_index=macos_mic)

def listen_windows():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        print(r.recognize_google(audio, language="ru-RU"))
    
def listen_windows_offline():
    model = Model(r"vosk_ru")

def main():
    #start()

    if platform == 'darwin':
        if is_connected():
            listen_macos()
        else:
            listen_macos_offline()
    elif platform == 'win32':
        if is_connected():
            listen_windows()
        else:
            listen_windows_offline()





if __name__ == "__main__":
    main()

