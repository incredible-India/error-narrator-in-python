from pygame import mixer
import gtts
import os

mixer.init()

try :
    print("hello world !")



except Exception as error :
    k=gtts.gTTS(
        text = str(error),lang = "en" ,
        slow =False
    )
    k.save('error.mp3')
    mixer.music.load('error.mp3')
    mixer.music.play()
    while True:
        s=input()
        mixer.music.stop()
