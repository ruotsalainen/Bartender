from gpiozero import Button, PWMLED
from time import sleep
import random


red = PWMLED(17)
blue = PWMLED(4)
player1 = Button(27)
player2 = Button(18)

time = random.uniform(5, 10)
sleep(time)
red.on()

while True:
    if player1.is_active:
        print("Player 1 wins!")
        break
    if player2.is_active:
        print("Player 2 wins!")
        break

red.off()
