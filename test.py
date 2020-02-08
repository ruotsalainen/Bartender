from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep
import sys
from drinks import drink_list
from config import config_options

button_select = Button(17)
button_advance = Button(27)
button_config = Button(22)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

BOUNCE = 0.5



current_drink = 0
modified = True

def next_drink():
    global modified
    global current_drink
    modified = True

    if current_drink == len(drink_list)-1:
        current_drink = 0
    else:
        current_drink += 1

def make_drink():
    global modified
    global current_drink
    modified = True

    lcd.write_string("coming right up!")
    sleep(2)

def open_config():
    current_option = 0
    while True:
        sleep(1)
        lcd.write_string(config_options[current_option].get("task"))

        if button_advance.is_active:
            if current_drink == len(config_options)-1:
                current_option = 0
            else:
                current_option += 1

        if button_select.is_active:
            if current_option == 0:
                lcd.clear()
                lcd.write_string("Flushing the system")
            if current_option == 1:
                exit()
        
        if button_config.is_active:
            break


while True:
    if modified:
        lcd.clear()
        drink_name = drink_list[current_drink].get("name")
        whitespace = int((20-len(drink_name))/2)
        lcd.cursor_pos = (1, whitespace)
        lcd.write_string(drink_name)
        sleep(BOUNCE)
        modified = False
    if button_select.is_active:
        next_drink()

    if button_advance.is_active:
        lcd.cursor_pos = (2, 2)
        make_drink()
    
    if button_config.is_active:
        open_config()
        modified = True

