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

# # listen_macos()


# from main import *
# import pyttsx3


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices)


# model = Model(r"vosk_ru")
# recognizer = KaldiRecognizer(model, 16000)
# mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()
    


# def fff():
#     while True:
#         data = stream.read(4096)
#         if recognizer.AcceptWaveform(data):
#             text = recognizer.Result()
#             text = text[14:-3]
#             print(text)
#             return text

# def ff():
#     while True:
#         command = fff()
#         if 'джарвис' in command:
#             play_sound(yes_sir2).play

# def main():
#         ff()

# # main()
# import json

# with open("frazes.json", "r") as read_file:
#     data = json.load(read_file)

# def json_check(word, key,znach):
#     if word in znach:  
#         return key     
    
# add = []
# for x, y  in data.items():
#    json_check('джарвис', x, y)

# import pyautogui as pg
# while True: 
 
#     pg.press('f12')

# import pyautogui as pg
# for i in range(2):      
#     with pg.hold('ctrl'):
#         pg.press('space')
# while True:
# #         pg.press('f12')
 
# from pynput import keyboard

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# import keyboard as kb

# while True:
#     kb.send('Key.media_volume_up')


# from pynput.keyboard import Key, Controller
# import time
# keyboard = Controller()
# keyboard.press(Key)