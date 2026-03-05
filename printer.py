from sys import stdout
from time import sleep

def printer(entry):
    for char in entry:
        stdout.write(char)
        stdout.flush()
        sleep(0.07)