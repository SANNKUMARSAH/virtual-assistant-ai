import webbrowser
from tts import speak
import utils

def execute_command(text):

    if "time" in text:
        speak(utils.get_time())

    elif "open youtube" in text:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in text:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open github" in text:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "search" in text:
        query = text.replace("search", "").strip()
        if query:
            speak("Searching " + query)
            webbrowser.open("https://www.google.com/search?q=" + query)

    elif "note" in text:
        speak("What should I write?")
        note = input("Note: ")
        utils.save_note(note)
        speak("Note saved")

    else:
        speak("I searched the web for you")
        webbrowser.open("https://www.google.com/search?q=" + text)
