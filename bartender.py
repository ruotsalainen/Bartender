import sys

from RPLCD.i2c import CharLCD
from gpiozero import Button, OutputDevice
from time import sleep

from drinks import drink_list
from config import config_options
import ring

# declaring buttons Button(GPIOpin)
button_select = Button(17)
button_advance = Button(27)
button_config = Button(22)

# declaring buzzer
buzzer = OutputDevice(pin=23)

# creating an object of the class CharLCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

# button bounce to avoid accidental multi inputs
BOUNCE = 0.5

# current drink in the drink list
current_drink = 0

# to avoid unnecessary rewrite to lcd
modified = True


def main():
	ring.draw_ring(lcd)
	greeting()
	drink_menu()

# advance to the next drink in the list
def next_drink():
    global modified
    global current_drink
    modified = True

    if current_drink == len(drink_list)-1:
        current_drink = 0
    else:
        current_drink += 1

# makes the drink
def make_drink():
    global modified
    modified = True

    lcd.write_string("Coming right up!")
    sleep(2)

# opens the config menu
def open_config():
    global modified
    modified = True
    current_option = 0
    while True:
        if modified:
            clear()
            task_name = config_options[current_option].get("task")
            whitespace = int((20-len(task_name))/2)
            lcd.cursor_pos = (1, whitespace)
            lcd.write_string(task_name)
            sleep(BOUNCE)
            modified = False

        if button_advance.is_active:
            modified = True
            if current_option == len(config_options)-1:
                current_option = 0
            else:
                current_option += 1

        if button_select.is_active:
            modified = True
            if current_option == 0:
            	clear()
                lcd.cursor_pos = (1, 0)
                lcd.write_string("Flushing the system")
                sleep(2)
            if current_option == 1:
                clear()
                lcd.cursor_pos = (1, 7)
                lcd.write_string("Ciao!")
                sleep(2)
                lcd.backlight_enabled = False
				lcd.clear()
                exit()

        if button_config.is_active:
            modified = True
            break

# system greeting at startup
def greeting():
	lcd.cursor_pos = (1, 7)
	lcd.write_string("Hello!")
	sleep(1)
	lcd.cursor_pos = (2, 3)
	lcd.write_string("I am Giovanni.")
	sleep(2)

def clear():
	for row in range(1,3):
		for col in range(1, 18):
			lcd.cursor_pos = (row, col)
			lcd.write_string(" ")

def drink_menu():
	global modified
	global current_drink


	while True:
	    if modified:
	        clear()
	        drink_name = drink_list[current_drink].get("name")
	        whitespace = int((20-len(drink_name))/2)
	        lcd.cursor_pos = (1, whitespace)
	        lcd.write_string(drink_name)
	        sleep(BOUNCE)
	        modified = False
	    if button_advance.is_active:
	        next_drink()

	    if button_select.is_active:
	        lcd.cursor_pos = (2, 2)
	        make_drink()
	
	    if button_config.is_active:
	        clear()
	        open_config()
	        modified = True

if __name__ == "__main__":
    main()
