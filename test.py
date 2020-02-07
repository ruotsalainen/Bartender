from gpiozero import LED, PWMLED
from time import sleep

red = PWMLED(17)
blue = PWMLED(4)

while True:
    for i in range(1, 11):
        red.value = i/10
        blue.value = i/10
        sleep(0.2)