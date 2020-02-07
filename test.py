from gpiozero import Button, PWMLED
from time import sleep
from signal import pause
from random import random
from math import floor


red = PWMLED(17)
blue = PWMLED(4)
player1 = Button(27)
player2 = Button(18)

i = 0

def winner_1():
    global i
    print("player1 won")
    red.off()
    i += 1

def winner_2():
    global i
    print("player2 won")
    red.off()
    i += 1

for i in range(10):

    value = floor(random()*10)
    print(value)
    sleep(value)
    red.on()

    player1.wait_for_active = winner_1
    player2.wait_for_active = winner_2

print("game over")

