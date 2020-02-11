import sys

from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep

from drinks import drink_list
from config import config_options
import ring


BOUNCE = 0.5
BUTTON_SELECT_PIN = 17
BUTTON_ADVANCE_PIN = 27
BUTTON_CONFIG_PIN = 22

class Bartender():
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


        # current drink in the drink list
        self.current_drink = 0

        # to avoid unnecessary rewrite to lcd
        self.modified = True

    # starting point
    def run(self, lcd, greeting, drink_menu):
        ring.draw_ring(lcd)
        greeting()
        drink_menu()

    # system greeting at startup
    def greeting(self, lcd):
        lcd.cursor_pos = (1, 7)
        lcd.write_string("Hello!")
        sleep(1)
        lcd.cursor_pos = (2, 3)
        lcd.write_string("I am Giovanni.")
        sleep(2)

    # clear screen, leave ring
    def clear(self, lcd):
        for row in range(1,3):
            for col in range(1, 19):
                lcd.cursor_pos = (row, col)
                lcd.write_string(" ")


    # advance to the next drink in the list
    def next_drink(self):
        self.modified = True

        if current_drink == len(drink_list)-1:
            current_drink = 0
        else:
            current_drink += 1

    # makes the drink
    def make_drink(self):
        global modified
        modified = True

        self.lcd.write_string("Coming right up!")
        sleep(2)

    # opens the config menu
    def open_config(self):
        modified = True
        current_option = 0

        while True:
            if modified:
                self.clear(self)
                task_name = config_options[current_option].get("task")
                whitespace = int((20-len(task_name))/2)
                self.lcd.cursor_pos = (1, whitespace)
                self.lcd.write_string(task_name)
                sleep(BOUNCE)
                modified = False

            if self.button_advance.is_active:
                modified = True
                if current_option == len(config_options)-1:
                    current_option = 0
                else:
                    current_option += 1

            if self.button_select.is_active:
                modified = True
                if current_option == 0:
                    self.clear(self)
                    self.lcd.cursor_pos = (1, 5)
                    self.lcd.write_string("Plumbing!")
                    sleep(2)
                if current_option == 1:
                    self.clear(self)
                    self.lcd.cursor_pos = (1, 7)
                    self.lcd.write_string("Ciao!")
                    sleep(2)
                    self.lcd.backlight_enabled = False
                    self.lcd.clear()
                    exit()

            if self.button_config.is_active:
                modified = True
                break

    # opens the drink menu
    def drink_menu(self):
        ring.draw_ring(self.lcd)
        self.greeting(self.lcd)

        while True:
            if modified:
                self.clear(self)
                drink_name = drink_list[self.current_drink].get("name")
                whitespace = int((20-len(drink_name))/2)
                self.lcd.cursor_pos = (1, whitespace)
                self.lcd.write_string(drink_name)
                sleep(BOUNCE)
                modified = False
            if self.button_advance.is_active:
                self.next_drink()

            if self.button_select.is_active:
                self.lcd.cursor_pos = (2, 2)
                self.make_drink()
        
            if self.button_config.is_active:
                self.clear(self)
                self.open_config()
                modified = True

bartender = Bartender()
bartender.drink_menu()