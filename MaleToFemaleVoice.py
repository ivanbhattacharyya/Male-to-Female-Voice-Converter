import pyttsx3
import speech_recognition as sr


r = sr.Recognizer()

# downloaded the audio file in wav format from : https://www.youtube.com/watch?v=WH7hUgdQV3I
with sr.AudioFile('male voice.wav') as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('Working on....')
        print(text)
    except:
        print('Sorry try again.')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text)
engine.runAndWait()



