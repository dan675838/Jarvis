from vosk import Model, KaldiRecognizer
import speech_recognition as sr
from name_audio import *
import pyaudio, wave, socket, os, datetime
from sys import platform
from signal import signal, SIGPIPE, SIG_DFL

r = sr.Recognizer()


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    if 'Микрофон MacBook' in name:
        macos_mic = index
    elif 'Микрофон Dekstop' in name:
        windows_mic = index

 

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
    


def jarvis_activate(mic_index):
    try:
        with sr.Microphone(device_index=mic_index) as source:
            audio = r.listen(source)
            request = r.recognize_google(audio, language='ru-RU')
            print(request)
    except:
        pass
    return request
        

def run_jarvis_macos(mic_index):
    command = jarvis_activate(mic_index)
    if 'Джарвис' in command:
        play_sound(yes_sir).play()
    

# def listen_macos_offline():
#     model = Model(r"vosk_ru")
#     rec = KaldiRecognizer(model, 8000)
#     p = pyaudio.PyAudio()
#     stream = p.open(
#         format=pyaudio.paInt16, 
#         channels=1, 
#         rate=8000, 
#         input=True, 
#         frames_per_buffer=8000
#         )
#     stream.start_stream()

#     while True:
#         data = stream.read(4000)
#         if len(data) == 0:
#             break
    
#         print(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult())
#     print(rec.FinalResult())


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


# def listen_windows_offline():
#     model = Model(r"vosk_ru")


def main():
    #start()
    if platform == 'darwin':    
        while True:
            run_jarvis_macos(macos_mic)
    elif platform == 'win32':
        while True:
            run_jarvis_windows(windows_mic)
        


if __name__ == "__main__":
    main()

