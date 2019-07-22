import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=2)
    print("Speak anything : ")
    audio = r.listen(source)
    print("After audio")
try:
    print("You said : "+r.recognize_google(audio))
except:
    print("Sorry could not recognize your voice")