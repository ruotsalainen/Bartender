import sys

from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep

from menu import Menu
from system import System

BOUNCE = 0.2
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
            # returns the writable string, and a padding value
            string_to_lcd, padding = self.advance_button_pressed()
            self.clear(self.lcd)
            self.lcd.cursor_pos = (1, padding)
            self.lcd.write_string(string_to_lcd)
        if self.button_select.is_active:
            print(self.select_button_pressed())
        if self.button_config.is_active:
            print(self.config_button_pressed())
        
        sleep(BOUNCE)

    def run(self):
        self.draw_frame(self.lcd, 0.05)
        #self.cheers(self.lcd)
        self.hello(self.lcd)
        self.init_menu(self.lcd)
        try:
            while True:
                self.startInterrupts()
        except KeyboardInterrupt:
            self.goodbye(self.lcd)
            self.lcd.backlight_enabled = False
            self.lcd.close()


bartender = Bartender()
bartender.run()