import speech_recognition as sr
import pyaudio
import random
import keyboard as kb
from string import punctuation
from random import choice, sample, shuffle

import os
import time
import pyttsx3
import webbrowser as wb
from time import ctime


def easy():
    x = ["duck", "bear", "water", "apple", "pair","pear","xbox","blue"]
    four = random.choice(x)
    mix = list(four)
    random.shuffle(mix)
    print(mix)
    answer = input("what is the right order? ")
    if answer == four:
        print("right")
        easy()
    elif answer == ("stop"):
        print("good job")


choicest = ["The quick brown fox jumped over the large dog.", "The housing crash was caused by big banks giving out bad loans to almost every.", "Amazon's stock price nearly doubled since the crash "]


def easyt():
    sel = choicesel = choice(["The cat runs.", "The ice cream is melting.", "Iron Man can beat Batman." "The ice cream is melting", "You got a friend in me", "Thats all folks", "dont panic"])
    sel_stripped = sel.lower().translate(str.maketrans('', '', punctuation))
    sel_list = sel_stripped.split()
    sel_user = input(f"Unscramble: {', '.join(sample(sel_list, len(sel_list)))}\n")
    print('Correct! ' if sel_user == sel_stripped else 'Incorrect. ', end='')
    print(f'The phrase was: "{sel}"')
    play(choices)


def hardt():
    sel = choicesel = choice(["ice cream is melting", "you got a friend in me", "that is all folks", "dont panic"])
    sel_stripped = sel.lower().translate(str.maketrans('', '', punctuation))
    sel_list = sel_stripped.split()
    sel_user = input(f"Unscramble: {', '.join(sample(sel_list, len(sel_list)))}\n")
    print('Correct! ' if sel_user == sel_stripped else 'Incorrect. ', end='')
    print(f'The phrase was: "{sel}"')
    hardt()

def meduimt():
    sel = choicesel = choice(["python is object orented programming lanuage","are you going to file your tax returns soons?","it is a law thermodymamics"])
    sel_stripped = sel.lower().translate(str.maketrans('', '', punctuation))
    sel_list = sel_stripped.split()
    sel_user = input(f"Unscramble: {', '.join(sample(sel_list, len(sel_list)))}\n")
    print('Correct! ' if sel_user == sel_stripped else 'Incorrect. ', end='')
    print(f'The phrase was: "{sel}"')
    play(meduimt)




    #print("speak the sentence in the right order :")
#hardt(choicest)
r = sr.Recognizer()
def record_audio(ask = False):
    if ask:
        print(ask)
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        voice_data = ''

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(voice_data))

        if text == ("hard"):
            print("speak in the correct order")
            hardt() and record_audio(ask = False)
        elif text == ("medium"):
            print("speak in the correct order")
            mediumt() and record_audio(ask = False)
        elif text == ("easy"):
            print("speak in the correct order")
            easyt() and record_audio(ask = False)


    except:
        wr = input("for writing: easy, medium, or hard")
        if wr == ("easy"):
            easy()
        elif wr == ("medium"):
            medium()
        elif wr == ("hard"):
            hard()

    return voice_data


voice_data = record_audio()
#respond(voice_data)
record_audio(ask = False)
