from time import sleep
from drinks import drink_list


# menu component that contains menu functionality
class Menu():
    def __init__(self):
        self.in_drink_menu = True
        self.current_drink = 0

    def init_menu(self, lcd):
        self.whitespace = int((20-len(drink_list[0]["name"]))/2)
        lcd.cursor_pos = (1, self.whitespace)
        lcd.write_string(drink_list[self.current_drink]["name"])

    def draw_menu(self):
        pass


    def advance_button_pressed(self):
        if self.in_drink_menu:
            # TODO
            pass

    def select_button_pressed(self):
        if self.in_drink_menu:
            # TODO
            pass

    def config_button_pressed(self):
        if self.in_drink_menu:
            # TODO
            pass