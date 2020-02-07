from gpiozero import LED, PWMLED
from time import sleep
from signal import pause

red = PWMLED(17)
blue = PWMLED(4)

red.pulse()
blue.pulse()