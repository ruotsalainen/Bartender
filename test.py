from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep
import sys
from Bartender.drinks import drink_list

button_right = Button(17)
button_left = Button(27)

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

    if current_drink == 7:
        current_drink = 0
    else:
        current_drink += 1

def make_drink():
    global modified
    global current_drink
    modified = True

    lcd.write_string("coming right up!")
    sleep(2)

try:
    while True:
        if modified:
            lcd.clear()
            drink_name = drink_list[current_drink].get("name")
            whitespace = int((20-len(drink_name))/2)
            lcd.cursor_pos = (1, whitespace)
            lcd.write_string(drink_name)
            sleep(BOUNCE)
            modified = False

        if button_right.is_active:
            next_drink()

        if button_left.is_active:
            lcd.cursor_pos = (2, 2)
            make_drink()
except KeyboardInterrupt:
    lcd.close()
    
