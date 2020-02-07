from gpiozero import LED, PWMLED
from time import sleep
from signal import pause

red = PWMLED(17)
blue = PWMLED(4)

selection = input("valitse testi 1, 2, 3")
if selection == 1:
    while True:
        red.value = 1
        blue.value = 1
        sleep(0.2)
        red.value = 0.5
        blue.value = 0.5
        sleep(0.2)
        red.value = 0
        blue.value = 0
        sleep(0.2)
elif selection == 2:
    red.blink()
    blue.blink()
elif selection == 3:
    while True:
        red.on()
        for i in range(1, 11):
            blue.value = i/10
            sleep(0.1)
        blue.on()
        for i in range(1, 11):
            red.value = i/10
            sleep(0.1)
