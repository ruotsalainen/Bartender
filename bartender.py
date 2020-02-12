import sys

from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep

from Bartender.menu import Menu

BOUNCE = 0.5
BUTTON_SELECT_PIN = 17
BUTTON_ADVANCE_PIN = 27
BUTTON_CONFIG_PIN = 22

class Bartender(Menu):
    def __init__(self):
        super().__init__()

        # declaring buttons Button(GPIOpin)
        self.button_select = Button(17)
        self.button_advance = Button(27)
        self.button_config = Button(22)

        # creating an object of the class CharLCD
        self.lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
                    cols=20, rows=4, dotsize=8,
                    charmap='A02',
                    auto_linebreaks=True,
                    backlight_enabled=True)

    def startInterrupts(self):
        if self.button_advance.is_active:
            print("button_advance active")
        if self.button_select.is_active:
            print("button_select is active")
        if self.button_config.is_active:
            print("button_config is active")

    def run(self):
        try:
            while True:
                self.startInterrupts()
        except KeyboardInterrupt:
            self.lcd.close()


bartender = Bartender()
bartender.run()