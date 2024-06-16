from gtts import gTTS
import os
import time

def text_to_speech(text):
    print("Dev --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    statbuf = os.stat("res.mp3")
    mbytes = statbuf.st_size / 1024
    duration = mbytes / 200
    if os.name == 'nt':  
        os.system('start res.mp3')
    elif os.uname().sysname == 'Darwin':  
        os.system('afplay res.mp3')
    else:  
        os.system('mpg123 res.mp3')  
    time.sleep(duration)
    os.remove("res.mp3")
