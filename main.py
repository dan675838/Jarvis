from vosk import Model, KaldiRecognizer
from name_audio import *
from sys import platform
import speech_recognition as sr
import pyaudio, wave, socket, os, time, datetime, json
import pyautogui as pg
from pynput.keyboard import Key, Controller

kb = Controller()

with open("frazes.json", "r") as read_file:
    data = json.load(read_file)



def translate(text):
    a = []
    request = text
    for key, value in data.items():
        for i in value:
            if i in text :
                request = request.replace(i, '')
                a.append(key)
    return [a, request]

def VUP():
    kb.press(Key.media_volume_up)

def VDOWN():
    kb.press(Key.media_volume_down)

def mute():
    kb.press(Key.media_volume_mute)

def pause():
    kb.press(Key.media_play_pause)

def next():
    kb.press(Key.media_next)

def previous():
    kb.press(Key.media_previous)    

def say(text):
    os.system('say' + text)
 

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False




def changekey(): 
    for i in range(2):     
        with pg.hold('ctrl'):
            pg.press('space')



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
            text = text[14:-3]
            print(text)
            return text
        



def run_jarvis_macos():
    while True:    
        text = jarvis_activate()
        text1 = translate(text)
        command = text1[0]
        request = text1[1]
        print(command)
        print(request)   
        if 'VUP' in command:
            VUP()
        if 'VDOWN' in command:
            VDOWN()
        if 'mute' in command:
            mute()
        if 'pause' in command:
            pause()
        if 'ask' in command:
            play_sound(yes_sir2).play()
        if 'changekey' in command:
            changekey()
        if 'say' in command:
            say(request)
        if 'pcstop' in command:
            play_sound(exit_diagnostic).play()
            exit()
    


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

