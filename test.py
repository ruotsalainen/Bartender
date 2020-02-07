from gpiozero import Button, PWMLED
from time import sleep
from signal import pause
from random import random
from math import floor


red = PWMLED(17)
blue = PWMLED(4)
player1 = Button(27)
player2 = Button(18)

player1_score = 0
player2_score = 0

def winner_1():
    global player1_score

    print("player1 won")
    player1_score +=1
    red.off()
    if player1_score == 5:
        print("player1 won")
    else:
        main()

def winner_2():
    global player2_score

    print("player2 won")
    player2_score +=1
    red.off()
    if player2_score == 5:
        print("player2 won")
    else:
        main()

def main():

    value = floor(random()*10)
    print(value)
    sleep(value)
    red.on()

    player1.when_activated = winner_1
    player2.when_activated = winner_2
    pause()


if __name__ == "__main__":
    main()
