from time import sleep
from frame import Frame

class Menu(Frame):
    def __init__(self):
        super.__init__()

    def hello(self, lcd):
        lcd.cursor_pos = (1, 7)
        lcd.write_string("Hello!")
        sleep(1)
        lcd.cursor_pos = (2, 3)
        lcd.write_string("I am Giovanni.")
        sleep(2)