from speech import listen
from tts import speak
import commands

def main():
    speak("Virtual Assistant started")

    while True:
        speak("I am listening")
        command = listen()

        if not command:
            continue

        cmd = command.lower().strip()

        if "exit" in cmd or "quit" in cmd or "stop" in cmd:
            speak("Goodbye")
            break

        commands.execute_command(cmd)

if __name__ == "__main__":
    main()
