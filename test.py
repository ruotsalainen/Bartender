from gpiozero import LED, PWMLED
from time import sleep

red = LED(17)
blue = PWMLED(4)

while True:
    red.on()
    blue.off()
    sleep(0.5)
    red.off()
    blue.on()
    sleep(0.5)