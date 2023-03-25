import pyttsx3
import os
import datetime
from gtts import gTTS
import engineio
import warnings
import calendar
import webbrowser
import speech_recognition as sr
import wikipedia
import wolframalpha
import random
import mysql.connector
import time
import smtplib
import requests

engineio = pyttsx3.init('sapi5')
client = wolframalpha.Client('P29A7R-A25WR2RW6J')
voices = engineio.getProperty('voices')
engineio.setProperty('voice', voices[len(voices)-1].id)
rate = engineio.getProperty('rate')
engineio.setProperty('rate', 200)
engineio.setProperty('voice', voices[0].id)
vol = engineio.getProperty('volume')
engineio.setProperty('volume', 1)
command = ['hey', 'hello', 'yo']
reply = ['welcome', 'hello', "what 's app"]
db = mysql.connector.connect(host='localhost', user='root', passwd='tiger')
con = db.cursor()


def speak(text):
    engineio.say(text)
    engineio.runAndWait()


def wishme():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Sir!')
        speak('My Name is FRIDAY, Your virtual assistant!')
        speak('How May I help you')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Sir!')
        speak('My Name is FRIDAY, Your virtual assistant!')
        speak('How May I help you')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening Sir!')
        speak('My Name is FRIDAY, Your virtual assistant!')
        speak('How May I help you')


def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']

    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    return ''


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user Said {query}\n")

    except Exception as e:
        speak("Sorry sir! I didn\'t get that! Try typing the command!")
        query = str(input('Command: '))
    return query


passwd='Ahmed123@22'

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query.lower():
            speak("Seaching please wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak('ok sir, opening youtube')
            webbrowser.open('youtube.com')
            time.sleep(10)

        elif 'open gmail' in query:
            speak('ok sir, opening youtube')
            webbrowser.open('www.gmail.com')
            time.sleep(10)

        elif 'open google' in query.lower():
            speak('ok sir, opening google')
            webbrowser.open('google.com')
            time.sleep(10)

        elif 'open instagram' in query:
            speak('ok sir, opening instagram')
            webbrowser.open('www.instagram.com')
            time.sleep(10)

        elif 'open discord' in query:
            speak('ok sir, opening discord')
            webbrowser.open('www.discord.com')
            time.sleep(10)

        elif 'open reddit' in query:
            speak('ok sir, opening reddit')
            webbrowser.open('www.reddit.com')
            time.sleep(10)

        elif 'open pinterest' in query:
            speak('ok sir, opening pinterest')
            webbrowser.open("www.pinterest.com")
            time.sleep(10)

        elif 'play music' in query:
            music_folder = 'C:\\Users\\keane\\Music'
            music = ['Really Love','Osas.mp3']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            time.sleep(20)

        elif 'open crunchyroll' in query:
            speak('ok sir, opening crunchyroll')
            webbrowser.open('www.crunchyroll.com')
            time.sleep(10)

        elif "convert currency" in query:

            api_key = 'S80I2IDHP41FI8V7'
            speak("enter currency code to covert from ")
            from_c = takecommand().lower()
            speak("enter currency code to covert to ")
            to_c = takecommand().lower()
            f = from_c.upper()
            t = to_c.upper()
            speak("enter the amount:")
            amt = float(takecommand())
            base = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
            main = base + '&from_currency=' + f + '&to_currency=' + t + '&apikey=' + api_key
            response = requests.get(main)
            result = response.json()
            key=result['Realtime Currency Exchange Rate']
            rate=key['5. Exchange Rate']
            rate=float(rate)
            print(rate)
            print(type(rate))
            print()
            print('Realtime Exchange Rate')
            print(f'1{f}:{rate} {t}')
            print()
            print('Converted Amount ')
            print(f'{amt} {f}:{float(rate) * amt} {t}')


        elif 'open whatsapp' in query:
            speak('ok sir, opening whatsapp')
            webbrowser.open('web.whatsapp.com')
            time.sleep(10)

        elif 'open vox cinemas' in query:
            speak("ok sir, opening vox cinemas")
            webbrowser.open("https://uae.voxcinemas.com/")
            time.sleep(10)

        elif 'open zoom' in query:
            speak("ok sir, opening zoom")
            webbrowser.open("www.zoom.us")
            time.sleep(10)

        elif 'order food' in query:
            speak("ok sir, opening several websites for you ")
            webbrowser.open("www.mcdonalds.com")
            webbrowser.open("uae.kfc.me")
            webbrowser.open("www.zomato.com")
            webbrowser.open("www.talabat.com")
            webbrowser.open("www.swiggy.com")
            webbrowser.open("www.deliveroo")
            time.sleep(10)

        elif 'open staz play' in query:
            speak("ok sir, opening staz play")
            webbrowser.open("https://arabia.starzplay.com/")
            time.sleep(10)

        elif 'open prime video' in query:
            speak('ok sir, primevideo')
            webbrowser.open('www.primevideo.com')
            time.sleep(10)

        elif 'open netflix' in query:
            speak('ok sir, opening netflix')
            webbrowser.open('www.netflix.com')
            time.sleep(10)

        elif 'open microsoft teams' in query:
            speak('ok sir, opening microsoft teams')
            webbrowser.open('www.teams.microsoft.com')
            time.sleep(10)

        elif 'open google meet' in query:
            speak('ok sir, open Google meet')
            webbrowser.open('www.meet.google.com')
            time.sleep(10)

        elif 'open krunker' in query:
            speak('ok sir, opening krunker')
            webbrowser.open('www.krunker.com')
            time.sleep(10)

        elif 'open code' in query:
            speak('ok sir, opening the code')
            codepath = "C:\\Users\\Dhia\\AppData\\Local\\Programs\\Python\\Python36\\FRIDAY project.py"
            os.startfile(codepath)

        elif "open tic tac toe" in query:
            speak("ok sir, opening tic tac toe")
            Game = "C:\\Users\\Dhia\\AppData\\Local\\Programs\\Python\\Python36\\tic tac toe.py"
            os.startfile(Game)
            time.sleep(10)

        elif "open calculator" in query:
            speak("ok sir, opening calculator")
            calc = "C:\\Users\\Dhia\\AppData\\Local\\Programs\\Python\\Python36\\Calculator.py"
            os.startfile(calc)
            time.sleep(10)

        elif "play songs" in query:
            speak('okay')
            print()

        elif "current time" in query:
            speak(datetime.datetime.now())

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'hello' in query:
            speak('Hello Sir')

        elif "open gmail" in query:
            speak('okay')
            webbrowser.open_new("gmail.com")
            time.sleep(10)

        elif 'send mail' in query:
            speak('Who is the recipient? ')
            recipient = takecommand()
            speak('okay, Enter the email address')
            receiver=input(str("Enter email address:"))

            if 'receiver' in recipient:
                try:
                    speak('What should I say? ')
                    content = takecommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls() 
                    server.login("ahmedmadhih777@gmail.com", passwd)
                    server.sendmail('ahmedmadhih777@gmail.com', receiver, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
            

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            quit()

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            quit()

        elif 'search from database' in query:
            speak('Which database sir')
            database = takecommand().lower()
            con.execute(f'use {database}')
            speak('say table name')
            table = takecommand().lower()
            try:
                con.execute(f'select * from {table}')
                re = con.fetchall()
                for c in re:
                    print(c)

            except:
                speak('table not found')

        elif query in command:
            w = random.randint(0, 2)
            speak(reply[w])

        elif "wait for some time" in query:
            time.sleep(10)

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it. ')
                    speak('WOLFRAM-ALPHA says -')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')


def assistantResponse(text):
    print(text)

    myobj = gTTS(text=text, lang='en', slow=False)

    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')


def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer']

    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False


def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


while True:

    text = recordAudio()
    response = ''

    if (wakeWord(text) == True):

        response = response + greeting(text)

        if ('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if ('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + meridiem + ' .'

        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        assistantResponse(response)


