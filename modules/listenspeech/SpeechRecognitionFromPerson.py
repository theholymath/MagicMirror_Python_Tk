# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:08:43 2018

@author: Ryan-Windows-PC
"""

# https://github.com/jeysonmc/python-google-speech-scripts/blob/master/stt_google.py
# https://realpython.com/python-speech-recognition/

from Tkinter import *
import locale
import time
import json
import threading
from PIL import Image, ImageTk
from contextlib import contextmanager
LOCALE_LOCK = threading.Lock()

import speech_recognition as sr

ui_locale = '' # e.g. 'fr_FR' fro French, '' as default
time_format = 12 # 12 or 24
date_format = "%b %d, %Y" # check python doc for strftime() for options

# globals for formatiing 
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

@contextmanager
def setlocale(name): #thread proof function to work with locale
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

class SpeechRecognitionFromPerson(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.config(bg='black')
        self.title = 'GetSpeechFromPerson' # 'News' is more internationally generic
        self.wordsLbl = Label(self, text=self.title, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.wordsLbl.pack(side=TOP, anchor=W)
        self.wordsContainer = Frame(self, bg="black")
        self.wordsContainer.pack(side=TOP)
        self.get_speech()
        
    def get_speech(self):
        # remove all children
        for widget in self.wordsContainer.winfo_children():
            widget.destroy()
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
            print("Say something!")
            audio = r.listen(source)
        
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            what_I_said = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))