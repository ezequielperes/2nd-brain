from audioplayer import AudioPlayer
from datetime import datetime
from time import sleep
tocou = False

while True:
    hour = datetime.now().hour
    minutes = datetime.now().minute
    print(f'\r{hour:02d}:{minutes:02d}', end='')
    sleep(1)

    if minutes == 11 and not tocou:
        AudioPlayer("aula 8 ex.21.mp3").play(block=True)
        tocou = True