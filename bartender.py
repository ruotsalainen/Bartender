import sys

from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep

from menu import Menu
from system import System

BOUNCE = 0.1
BUTTON_SELECT_PIN = 17
BUTTON_ADVANCE_PIN = 27
BUTTON_CONFIG_PIN = 22

class Bartender(Menu, System):
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
        
        sleep(BOUNCE)

    def run(self):
        self.draw_frame(self.lcd, 0.05)
        sleep(2)
        self.cheers(self.lcd)
        self.hello(self.lcd)
        try:
            while True:
                self.startInterrupts()
        except KeyboardInterrupt:
            self.goodbye(self.lcd)
            self.lcd.backlight_enabled = False
            self.lcd.close()


bartender = Bartender()
bartender.run()