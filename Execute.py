import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import requests
import os
import smtplib
import pyjokes
import PyPDF2
import pywhatkit
import random
from requests import get
import os
import pyautogui

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')  #get all the voices 
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) #setting voice Id (men/women)


def speak(audio):
    engine.say(audio)   
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Im Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanathraip@gmail.com', 'Sanath7925')
    server.sendmail('sanathraip@gmail.com', to, content)
    server.close()
    

def pdf_reader():
    book = open('02. B.E.P Problems-Dr. JPM.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Sir please  enter the page number i have to read")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
        #WIKIPIDEA
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") 
            try:
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry please pronounce it correctly")

        #OPEN YOUTUBE
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        #OPEN INSTRAGRAM
        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")
        
        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        #OPEN FACEBOOK
        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
            
        elif 'facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        #OPEN STACKOVERFLOW
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            
        #OPEN GEEK FOR GEEKS
        elif 'open geeks' in query:
            speak("opening geeks")
            webbrowser.open("https://www.geeksforgeeks.org/")
        
        #OPEN GITHUB       
        elif 'github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
           
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        
        #OPEN GOOGLE   
        elif 'open google' in query:
            speak('Okay!')
            speak("opening google")
            webbrowser.open("google.com")
             
        elif 'google' in query:
            speak('Okay!')
            speak("opening google")
            webbrowser.open("google.com") 

        #PLAY MUSIC 
        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'music' in query:
            music_dir = 'F:\\music2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'romantic music' in query:
            music_dir = 'F:\\Music1'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        #SHOW TIME
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'jarvis time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

     

        #SENDING MAILS
        elif 'email to sanath' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "skcreation7925@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry SK. I am not able to send this email")    

        #TAKE SCREENSHOT TO
        elif "take screenshot" in query:
            speak("Sir, Please tell me the name for the screenshot file")
            name = takeCommand().lower()
            speak("Taking Screenshot...!")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("ScreenShot Saved...!")
            

        #IP ADDRESS
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
            
        # JOKE
        #elif "Tell me a joke" in query:
        #    joke = pyjokes.get_joke()
        #   speak(joke)
            
        # SHUTDOWN
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
            
        # RESTART
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
            
        # SLEEP
        elif "shutdown" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        #CMD OPEN
        elif 'open command prompt' in query or 'open CMD' in query:
            speak('Okay!')
            os.system('start cmd')
        
            
