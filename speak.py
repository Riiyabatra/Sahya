from gtts import gTTS
import pyglet
import time, os

def tts(text):
    file = gTTS(text)
    filename='temp.mp3'
    file.save(filename)

    music=pyglet.media.load(filename,streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)
tts("hi how are you")
