import speech_recognition as sr
from time import ctime
import webbrowser
import time
r=sr.Recognizer() #backbone of our program going to recognize the voice

def record_audio(ask=False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            print(ask)
        audio=r.listen(source) #captures our audio
        voice_data=''
        try:
            voice_data=r.recognize_google(audio) #converting audio into text
            
        except sr.UnknownValueError:
            print('Sorry,I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down') 
        return voice_data           

def respond(voice_data):
    if 'what is your name' in voice_data:
        print("My name is Natasha")
    if 'what is my name' in voice_data:
        print("Your name is Kaustubh")    
    if 'what time is it' in voice_data:
        print(ctime())    
    if 'search' in voice_data:
        search=record_audio('What do you want to search for?')
        print('Search Succesfull Opening Up...') 
        url='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location=record_audio('What is the location?')
        print('Search Succesfull Opening Up...') 
        url='https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)    
    if 'exit' in voice_data:
        exit()    

time.sleep(1)
print("How can I help U?")
while 1:
    voice_data=record_audio()
    respond(voice_data)    