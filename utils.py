import datetime

def get_time():
    now = datetime.datetime.now()
    return now.strftime("Time is %H:%M on %A")

def save_note(text):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")
