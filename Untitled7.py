#!/usr/bin/env python
# coding: utf-8

# In[15]:


get_ipython().system('pip install pipwin')
get_ipython().system('pipwin install pyaudio')
get_ipython().system('pip install SpeechRecognition pyttsx3 openai gtts')
get_ipython().system('pip install torch transformers')



# In[12]:


get_ipython().system('pip install --upgrade openai')


# In[2]:


import speech_recognition as sr
import pyttsx3
import openai
from transformers import AutoModelForCausalLM, AutoTokenizer



# In[28]:


pip install transformers torch


# In[24]:


openai.api_key = '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'


# In[25]:


recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""
        
# Test the function
recognize_speech()


# # Text to speech 

# In[31]:


pip install pyttsx3


# In[12]:


# importing the pyttsx library 
import pyttsx3 

# initialisation 
engine = pyttsx3.init() 

# testing 
engine.say("My first code on text-to-speech") 
engine.say("Thank you") 
engine.runAndWait() 


# In[17]:


import pyttsx3 

def onStart(): 
    print('starting') 

def onWord(name, location, length): 
    print('word', name, location, length) 

def onEnd(name, completed): 
    print('finishing', name, completed) 

engine = pyttsx3.init() 

engine.connect('started-utterance', onStart) 
engine.connect('started-word', onWord) 
engine.connect('finished-utterance', onEnd) 

sen = "fortune favours the brave"


engine.say(sen) 
engine.runAndWait() 


# In[ ]:




