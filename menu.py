from time import sleep
from drinks import drink_list
from tasks import system_tasks
from system import System

# menu component that contains menu functionality
class Menu(System):
    def __init__(self):
        super().__init__()
        self.in_drink_menu = True
        self.current_drink = 0
        self.current_task = 0

    def init_menu(self, lcd):
        padding = int((20-len(drink_list[self.current_drink]["name"]))/2)
        lcd.cursor_pos = (1, padding)
        lcd.write_string(drink_list[self.current_drink]["name"])

    def advance_button_pressed(self):
        if self.in_drink_menu:
            self.current_drink += 1
            current_drink_name = drink_list[self.current_drink]["name"]
            padding = int((20-len(current_drink_name))/2)
            return current_drink_name, padding
        else:
            self.current_task += 1
            current_task_name = system_tasks[self.current_task]["task"]
            padding = int((20-len(current_task_name))/2)
            return current_task_name, padding

    def select_button_pressed(self):
        if self.in_drink_menu:
            return drink_list[self.current_drink]["ingredients"]
        else:
            return system_tasks[self.current_task]["task_id"]

    def tasks_button_pressed(self):
        if self.in_drink_menu:
            self.in_drink_menu = not self.in_drink_menu
            self.current_task = 0
            padding = int((20-len(system_tasks[self.current_task]["task"]))/2)
            return system_tasks[self.current_task]["task"], padding
        else:
            self.in_drink_menu = not self.in_drink_menu
            self.current_drink = 0
            padding = int((20-len(drink_list[self.current_drink]["name"]))/2)
            return drink_list[self.current_drink]["name"], padding
