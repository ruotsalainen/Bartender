from gpiozero import LED, PWMLED
from time import sleep
from signal import pause

red = PWMLED(17)
blue = PWMLED(4)

red.value = 1
blue.value = 1
red.value = 0.5
blue.value = 0.5
red.value = 0
blue.value = 0

pause()