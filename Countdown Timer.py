import time
import os
import winsound

def countdown(ars):
    print(ars)
    hours=int(ars[0])
    minutes=int(ars[1])
    seconds=int(ars[2])

    total_seconds = hours * 3600 + minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    sound_file = "buzzer.wav"
    os.name == "nt"
    print("Time's up")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)




countdown(input("Enter time in format HH:MM:SS ").split(":"))
