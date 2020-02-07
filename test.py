from gpiozero import Button, PWMLED
from time import sleep
import random
from signal import pause


red = PWMLED(17)
blue = PWMLED(4)
player1 = Button(27)
player2 = Button(18)

player1_score = 0
player2_score = 0

def game():
    global player1_score
    global player2_score

    time = random.uniform(5, 10)
    sleep(time)
    red.on()

    while True:
        if player1.is_active:
            print("Player 1 wins!")
            player1_score += 1
            break
        if player2.is_active:
            print("Player 2 wins!")
            player2_score += 1
            break

    red.off()

game()
