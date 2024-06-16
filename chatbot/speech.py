import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        audio = recognizer.listen(mic)
    try:
        text = recognizer.recognize_google(audio)
        print("Me  --> ", text)
    except sr.UnknownValueError:
        text = "ERROR"
        print("Me  -->  ERROR")
    return text
