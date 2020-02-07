from gpiozero import Button, PWMLED
from time import sleep
from signal import pause

red = PWMLED(17)
blue = PWMLED(4)
button1 = Button(18)
button2 = Button(27)

def blue_on():
    blue.on()
    sleep(2)

def red_on():
    red.on()
    sleep(2)

button1.when_activated = blue_on

button2.when_activated = red_on

pause()