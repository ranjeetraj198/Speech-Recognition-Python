# First:- Install speech recognition for recognising your voice (pip install speechrecognition)
# Second:- Install pyaudio for using microphone  (pip install pyaudio)
# Third:- Install gtts package for converting your text to voice    (pip install gTTS)
# Fourth:- Install playsound for listening your data    (pip install playsound)


import speech_recognition as sr
from gtts import gTTS
import playsound

def voice():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak anything : ")
        audio = r1.listen(source)
        try:
            text = r1.recognize_google(audio)
            print(f'You Said : {text}')

            #Saving your voice data in txt format in your system
            file1 = open("voice_data.txt","a+")
            file1.write(text + "\n")
            file1.close()

            #Reading your txt on python terminal
            file1 = open("voice_data.txt","r")
            print("Reading File : \n", file1.read())
            file1.close()

            #listening your text variable from your system
            file2 = gTTS(text=text, lang="en", slow=False)
            file2.save("voice_data.mp3")
            playsound.playsound("voice_data.mp3")

        except:
            print("Could not recognise your voice. Please try again.")
    return

voice()
