# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 07:01:15 2018

@author: Ryan-Windows-PC
"""
import numpy as np

from Tkinter import *
import locale
import time
import threading
import traceback
import requests
import json
from PIL import Image, ImageTk
from contextlib import contextmanager
LOCALE_LOCK = threading.Lock()

# globals for formatiing 
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

class Phrases(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.phrase = 'This is a mirror'
        
        #self.wordFrm = Frame(self, bg="black")
        #self.wordFrm.pack(side=BOTTOM, anchor=CENTER)
        
        self.wordLbl = Label(self, font=('Helvetica', medium_text_size), 
                             wraplength=1000,fg="white", bg="black")
        self.wordLbl.pack(side=BOTTOM)
        
        with open('modules/phraseDisplay/sayings.txt') as f:
            self.quotes = f.readlines()
        
        self.get_phrase()

    def get_phrase(self):
        self.quote = np.random.choice(self.quotes)
        self.quote = self.quote.replace("-","\n-")
        
        self.wordLbl.config(text=self.quote)
        
        self.after(10000, self.get_phrase)

