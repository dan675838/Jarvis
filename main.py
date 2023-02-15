from vosk import Model, KaldiRecognizer
from name_audio import *
from sys import platform
import speech_recognition as sr
import pyaudio, wave, socket, os, time, datetime





 

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False



def start():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        play_sound(good_morning).play()
    else:
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
    


def jarvis_activate():
    
    model = Model(r"vosk_ru")
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    while True:

        data = stream.read(4096)
    
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            query = text[14:-3]
            print(query)
            return query
        

def run_jarvis_macos():
    while True:    
        command = jarvis_activate()
        if 'джарвис' in command:
            play_sound(yes_sir).play()
    


def run_jarvis_windows():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio, language="ru-RU"))
        except sr.UnknownValueError:
            play_sound(yes_repeat).play()


def main():
    print('Start')
    #start()
    if platform == 'darwin':    
            run_jarvis_macos()
    elif platform == 'win32':
        while True:
            run_jarvis_windows()
        


if __name__ == "__main__":
    main()

