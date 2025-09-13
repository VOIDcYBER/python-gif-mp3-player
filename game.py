#  -------------------------       This program only works on Windows         -------------------------------
import requests
import pygame
import os
import subprocess



# GIF downloaded
# 👇
link2="Your GIF link"
gif=requests.get(link2)
gif.raise_for_status()

with open("gif.gif","wb") as f:
    f.write(gif.content)
print("GIF downloaded")




# Music downloaded
# 👇
link="Your Music link"
sound=requests.get(link)
sound.raise_for_status()

with open("play.mp3","wb") as f:
    f.write(sound.content)
print("Music downloaded")

    
 
# Play the GIF with the default player while playing audio in the background

masir=os.getcwd()     

subprocess.run(["start","gif.gif"],shell=True)  #Playing GIF
    
pygame.mixer.init()                                  
pygame.mixer.music.load(os.path.join(masir, "play.mp3"))        
pygame.mixer.music.play(-1)                     #Play Music
input("Enter Stop")


