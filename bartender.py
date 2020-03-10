import sys

from RPLCD.i2c import CharLCD
from gpiozero import Button
from multiprocessing.dummy import Pool
from time import sleep, time

from menu import Menu
from system import System
from tasks import system_tasks
from drinks import drink_list
from pumps import pumps_list

BOUNCE = 0.2
FLOWRATE = 3.3  # ml/sec

BUTTON_SELECT_PIN = 17
BUTTON_ADVANCE_PIN = 27
BUTTON_TASKS_PIN = 22


class Bartender(Menu):
    def __init__(self):
        super().__init__()

        # declaring buttons Button(GPIOpin)
        self.button_select = Button(BUTTON_SELECT_PIN)
        self.button_advance = Button(BUTTON_ADVANCE_PIN)
        self.button_tasks = Button(BUTTON_TASKS_PIN)

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
            # returns the list of ingredients for the selected drink OR the task_id
            selection_details = self.select_button_pressed()
            if self.in_drink_menu:
                self.make_drink(selection_details)
            else:
                self.execute_task(selection_details)
        if self.button_tasks.is_active:
            # returns drink menu/task menu item0 and padding
            string_to_lcd, padding = self.tasks_button_pressed()
            self.clear(self.lcd)
            self.lcd.cursor_pos = (1, padding)
            self.lcd.write_string(string_to_lcd)

        sleep(BOUNCE)

    def make_drink(self, ingredients):
        self.lcd.cursor_pos = (2, 2)
        self.lcd.write_string("Coming right up!")
        sleep(2)
        self.lcd.cursor_pos = (2, 2)
        self.lcd.write_string("                ")
        self.run_threads(ingredients)

    # executes a task based on id
    def execute_task(self, task_id):
        if task_id == 900:
            self.clear(self.lcd)
            self.lcd.cursor_pos = (1, 5)
            self.lcd.write_string("Flushing!")
            sleep(2)
            current_task_name = system_tasks[self.current_task]["task"]
            padding = int((20-len(current_task_name))/2)
            self.lcd.cursor_pos = (1, padding)
            self.lcd.write_string(current_task_name)
        elif task_id == 901:
            self.goodbye(self.lcd)

    def run_threads(self, ingredients):
        pool = Pool(6)
        pool.map(self.run_pump, ingredients)
        pool.close()
        pool.join()
        print("Drink ready")

    def run_pump(self, ingredient):
        timeout = ingredient["amount"] / FLOWRATE
        for pump in pumps_list:
            if pump["value"] == ingredient["ingredient"]:
                pump_pin = pump["pin"]
                # TODO
                # toggle relay on
                print(pump["name"] + " on pin " + str(pump_pin) + " is running")
                sleep(timeout)
                # toggle relay off
                print(pump["name"] + " off")

    def run(self):
        self.draw_frame(self.lcd, 0.05)
        # self.cheers(self.lcd)
        # self.hello(self.lcd)
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
