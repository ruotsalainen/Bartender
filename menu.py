from time import sleep
from drinks import drink_list
from config import config_options
from system import System

# menu component that contains menu functionality
class Menu(System):
    def __init__(self):
        super().__init__()
        self.in_drink_menu = True
        self.current_drink = 0
        self.current_option = 0

    def init_menu(self, lcd):
        self.whitespace = int((20-len(drink_list[self.current_drink]["name"]))/2)
        lcd.cursor_pos = (1, self.whitespace)
        lcd.write_string(drink_list[self.current_drink]["name"])

    def advance_button_pressed(self):
        if self.in_drink_menu:
            self.current_drink += 1
            return drink_list[self.current_drink]["name"]
        else:
            self.current_option += 1
            return config_options[self.current_option]["task"]

    def select_button_pressed(self):
        if self.in_drink_menu:
            return drink_list[self.current_drink]["ingredients"]
        else:
            return config_options[self.current_option]["task_id"]

    def config_button_pressed(self):
        if self.in_drink_menu:
            self.in_drink_menu = not self.in_drink_menu
            self.current_option = 0
            return config_options[self.current_option]["task"]
        else:
            self.in_drink_menu = not self.in_drink_menu
            self.current_drink = 0
            return drink_list[self.current_drink]["name"]
