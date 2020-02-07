from gpiozero import LED, PWMLED
from time import sleep

red = PWMLED(17)
blue = PWMLED(4)

while True:
    red.pulse()
    blue.pulse()