from gpiozero import Button, PWMLED
from time import sleep
from signal import pause
from random import random
from math import floor


red = PWMLED(17)
blue = PWMLED(4)
player1 = Button(27)
player2 = Button(18)

def winner_1():
    print("player1 won")

def winner_2():
    print("player2 won")

value = floor(random()*10)
print(value)
sleep(value)
red.on()

player1.when_activated = winner_1
player2.when_activated = winner_2

pause()