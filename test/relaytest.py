#!/usr/bin/python

# A simple Python application for controlling a relay board from a Raspberry Pi
# The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# The relay is connected to one of the Pi's GPIO ports, then is defined as an Output device
# in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

import sys
import time

import gpiozero

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 17

# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay1 = gpiozero.OutputDevice(26, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(16, active_high=True, initial_value=False)
relay3 = gpiozero.OutputDevice(6, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(5, active_high=True, initial_value=False)
relay5 = gpiozero.OutputDevice(25, active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(24, active_high=True, initial_value=False)


def set_relay(status):
    if status:
        print("Setting relay: ON")
        relay1.on()
    else:
        print("Setting relay: OFF")
        relay1.off()
        relay2.off()


def toggle_relay():
    print("toggling relay")
    relay1.toggle()
    relay2.toggle()
    relay3.toggle()
    relay4.toggle()
    relay5.toggle()
    relay6.toggle()


def main_loop():
    # start by turning the relay off
    set_relay(False)
    while 1:
        # then toggle the relay every second until the app closes
        toggle_relay()
        # wait a second 
        time.sleep(1)


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # turn the relay off
        set_relay(False)
        print("\nExiting application\n")
        # exit the application
        sys.exit(0)