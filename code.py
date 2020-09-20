import random
from random import choice
import pyaudio
import speech_recognition as sr
from string import punctuation
from random import choice, sample, shuffle




choices = ["The cat runs.", "The ice cream is melting.", "Iron Man can beat Batman."]

def easyt(choices):
    sel = choice(choices)
    sel_stripped = sel.lower().translate(str.maketrans('', '', punctuation))
    sel_list = sel_stripped.split()
    sel_user = input(f"Unscramble: {', '.join(sample(sel_list, len(sel_list)))}\n")
    print('Correct! ' if sel_user == sel_stripped else 'Incorrect. ', end='')
    print(f'The phrase was: "{sel}"')
    play(choices)

easyt(choices)



choicest = ["python is object orented programming lanuage","are you going to file your tax returns soons?","it is a law thermodymamics"]

def meduimt(choices):
    sel = choice(choicest)
    sel_stripped = sel.lower().translate(str.maketrans('', '', punctuation))
    sel_list = sel_stripped.split()
    sel_user = input(f"Unscramble: {', '.join(sample(sel_list, len(sel_list)))}\n")
    print('Correct! ' if sel_user == sel_stripped else 'Incorrect. ', end='')
    print(f'The phrase was: "{sel}"')
    play(meduimt)

play(meduimt)





choicest = ["The quick brown fox jumped over the large dog.", "The housing crash was caused by big banks giving out bad loans to almost every.", "Amazon's stock price nearly doubled since the crash "]

def hardt(choices):
    sel = choice(choicest)
    sel_stripped = sel.lower().translate(str.maketrans('', '', punctuation))
    sel_list = sel_stripped.split()
    sel_user = input(f"Unscramble: {', '.join(sample(sel_list, len(sel_list)))}\n")
    print('Correct! ' if sel_user == sel_stripped else 'Incorrect. ', end='')
    print(f'The phrase was: "{sel}"')
    hardt(choicest)

hardt(choices)
        
        



def easy():
    x = ["ability", "airport", "android", "between", "brother","cameras","fathers","mothers"]
    four = random.choice(x)
    mix = list(four)
    random.shuffle(mix)
    print(mix)

    answer = input("what is the right order?m ")
    
    if answer == (four):
        print("right")
        easy()
    elif answer == ("stop"):
            print("good job")
    #elif answer != ("bill" or "duck" or "bear" or "bank" or  "wood" or "ruby" or "bing" or "said"):
     #   print("wrong")
      #  easy()
        
    else:
        if answer != ("bill" or "duck" or "bear" or "bank" or  "wood" or "ruby" or "bing" or "said"):
            print("wrong")
            easy()

def medium():
    x = ["ability", "airport", "android", "between", "brother","cameras","fathers","mothers"]
    seven = random.choice(x)
    mix = list(seven)
    
    random.shuffle(mix)
    
    print (mix)

    answer = input("what is the right order?m ")
    
    if answer == (seven):
        print("right")
        easy()
    elif answer == ("stop"):
            print("good job")
    elif answer != ("ability" or "airport" or "android" or "between" or "brother" or"cameras" or"fathers" or"mothers"):
        print("wrong")
        easy()
        
    else:
        if answer != ("ability" or "airport" or "android" or "between" or "brother" or"cameras" or"fathers" or"mothers"):
            print("wrong")

def hard():
    
    x = ["abdominal", "abduction","autopsies", "babycakes", "babyfood","backboard","backboned","bachelors"]
    ten = random.choice(x)
    mix = list(ten)
    #y(split(four))
    random.shuffle(mix)
    #print(list)
    print (mix)

    answer = input("what is the right order?m ")
    #if answer == "bill" or "duck" or "bear" or "bank" or  "wood" or "ruby" or "bing" or "said":
     #   easy()
    if answer == (ten):
        print("right")
        easy()
    elif answer == ("stop"):
            print("good job")
    elif answer != ("abdominal"or "abduction"):
    # or "autopsies" or "babycakes" or "babyfood"or "backboard" or "backboned" or "bachelors"):
        print("wrong")
        easy()
        
    else:
        if answer != ("ability" or "airport"):
        # or "android" or "between" or "brother" or"cameras" or"fathers" or"mothers"):
            print("wrong")
writing():
    dif = input("how hard do you want ")

    if dif == ("easy"):
        easy()
    elif dif == ("medium"):
        medium()
    elif dif == ("hard"):
        hard()
    else:
        print("wtf")

speech():

    dif = input("how hard do you want ")

    if dif == ("easyt"):
        easy()
    elif dif == ("mediumt"):
        medium()
    elif dif == ("hardt"):
        hard()
    else:
        print("wtf")




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

print("would you like speech or writing pratices")
    if text == ("speech"):
        speech()
    elif text == ("writing"):
        writing()
    else:
        print("tf")
