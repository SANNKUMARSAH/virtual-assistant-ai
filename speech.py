import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5)

        text = r.recognize_google(audio)
        print("You said:", text)
        return text

    except Exception:
        try:
            return input("Type command: ")
        except KeyboardInterrupt:
            return ""
