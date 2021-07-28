from gtts import gTTS
import sys
import vlc
import os

tts = gTTS(sys.argv[1])
tts.save('message.mp3')

os.system("cvlc message.mp3")




