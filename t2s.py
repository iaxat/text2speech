# This project is about text to speech conversion

import os
import subprocess
from gtts import gTTS
# Importing libraries required for this project
# Import gTTS will help in converting a string to audio
# Import os is for comversion of an audio file to playable
# Import os is also for file handling
 
def t2s():
    # The text that you want to convert to audio 
    my_file = open('file','r')
    
    # Language in which you want to convert 
    language = 'en'
    
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=my_file, lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
  
    # Playing the converted file 

t2s()