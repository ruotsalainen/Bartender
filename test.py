from gpiozero import LED
from time import sleep

red = LED(17)
blue = LED(4)

while True:
    red.on()
    blue.off()
    sleep(1)
    red.off()
    blue.on()
    sleep(1/2)