from gpiozero import OutputDevice
from time import sleep

buzzer = OutputDevice(pin=23)

while True:
    buzzer.toggle()
    sleep(1)